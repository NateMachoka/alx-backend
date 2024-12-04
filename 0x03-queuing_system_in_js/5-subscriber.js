import { createClient } from 'redis';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

// Subscribe to the "holberton school channel"
client.subscribe('holberton school channel', (err, count) => {
  if (err) {
    console.error(`Error subscribing: ${err.message}`);
  } else {
    console.log(`Subscribed to ${count} channel(s)`);
  }
});

// Handle messages on the channel
client.on('message', (channel, message) => {
  console.log(`Received message: ${message}`);

  if (message === 'KILL_SERVER') {
    console.log('Received KILL_SERVER, unsubscribing and quitting');
    client.unsubscribe();
    client.quit();
  }
});
