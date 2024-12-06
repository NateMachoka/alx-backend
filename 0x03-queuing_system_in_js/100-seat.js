const express = require('express');
const redis = require('redis');
const kue = require('kue');
const { promisify } = require('util');

// Initialize Redis client and Kue queue
const redisClient = redis.createClient();
const queue = kue.createQueue();

// Promisify Redis methods
const getAsync = promisify(redisClient.get).bind(redisClient);
const setAsync = promisify(redisClient.set).bind(redisClient);

// Initialize server
const app = express();
const port = 1245;

// Set initial number of available seats to 50
let reservationEnabled = true;
setAsync('available_seats', 50);

// Function to reserve a seat (sets the number of available seats in Redis)
async function reserveSeat(number) {
  await setAsync('available_seats', number);
}

// Function to get the current available seats
async function getCurrentAvailableSeats() {
  const availableSeats = await getAsync('available_seats');
  return availableSeats;
}

// Routes
// Get available seats
app.get('/available_seats', async (req, res) => {
  const availableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: availableSeats });
});

// Reserve a seat
app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: "Reservations are blocked" });
  }

  const availableSeats = await getCurrentAvailableSeats();
  if (availableSeats <= 0) {
    reservationEnabled = false;
    return res.json({ status: "Reservations are blocked" });
  }

  // Create and queue the job for reservation
  const job = queue.create('reserve_seat', {
    availableSeats: availableSeats - 1
  }).save(err => {
    if (err) {
      return res.json({ status: "Reservation failed" });
    }
    res.json({ status: "Reservation in process" });
  });
});

// Process the reservation queue
app.get('/process', async (req, res) => {
  res.json({ status: "Queue processing" });

  // Process the queue
  queue.process('reserve_seat', async (job, done) => {
    const { availableSeats } = job.data;

    if (availableSeats < 0) {
      return done(new Error('Not enough seats available'));
    }

    // Update the available seats in Redis
    await reserveSeat(availableSeats);
    console.log(`Seat reservation job ${job.id} completed`);

    // If no more seats, disable reservations
    if (availableSeats === 0) {
      reservationEnabled = false;
    }

    done();
  });
});

// Start the server
app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
