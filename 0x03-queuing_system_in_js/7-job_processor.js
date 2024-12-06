import kue from 'kue';

// Blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
  // Start tracking job progress
  job.progress(0, 100);

  // Check if the phone number is blacklisted
  if (blacklistedNumbers.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  // Simulate job progress
  job.progress(50, 100);

  // Log sending notification
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

  // Mark the job as done
  done();
}

// Create the queue
const queue = kue.createQueue();

// Process jobs from the 'push_notification_code_2' queue
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;

  // Call sendNotification function
  sendNotification(phoneNumber, message, job, done);
});
