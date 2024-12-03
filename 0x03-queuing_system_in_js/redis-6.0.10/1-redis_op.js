import { createClient } from 'redis';

// Create Redis client
const client = createClient();

// Handle successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Handle connection errors
client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

// Connect to Redis
client.connect().catch((err) => {
  console.error(`Connection failed: ${err.message}`);
});

// Function to set a new school value in Redis
const setNewSchool = (schoolName, value, callback) => {
  client.set(schoolName, value, (err, reply) => {
    if (err) {
      console.error(`Error setting school: ${err.message}`);
    } else {
	redis.print(reply);
    }
    if (callback) callback();
  });
};

// Function to display the value of a school from Redis
const displaySchoolValue = (schoolName, callback) => {
  client.get(schoolName, (err, value) => {
    if (err) {
      console.error(`Error retrieving school value: ${err.message}`);
    } else {
      console.log(value);
    }
    if (callback) callback();
  });
};

// Example operations
displaySchoolValue('Holberton', () => {
  setNewSchool('HolbertonSanFrancisco', '100', () => {
    displaySchoolValue('HolbertonSanFrancisco');
  });
});
