const redis = require('redis');

const client = redis.createClient();

// Event listener for when the client is connected
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event listener for when an error occurs
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

// Function to publish messages after a delay
function publishMessage(message, time) {
  setTimeout(async () => {
    try {
      console.log(`About to send ${message}`);
      // Ensure the client is connected before publishing
      if (client.connected) {
        client.publish('holberton school channel', message, (err, reply) => {
          if (err) {
            console.error(`Failed to publish message: ${err}`);
          } else {
            console.log(`Message published: ${reply}`);
          }
        });
      } else {
        console.error('Redis client is not connected');
      }
    } catch (err) {
      console.error(`Error during publishing message: ${err}`);
    }
  }, time);
}

// Call the publishMessage
publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
