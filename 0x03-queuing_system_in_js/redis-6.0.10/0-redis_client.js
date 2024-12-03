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
