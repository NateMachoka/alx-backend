import { createClient, print } from 'redis';

const client = createClient();

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');

  // Create the hash with the key "HolbertonSchools" and the specified fields
  client.hset('HolbertonSchools',
    'Portland', 50,
    'Seattle', 80,
    'New York', 20,
    'Bogota', 20,
    'Cali', 40,
    'Paris', 2,
    print);

  // Retrieve and display the hash
  client.hgetall('HolbertonSchools', (err, result) => {
    if (err) {
      console.error(`Error fetching data: ${err.message}`);
    } else {
      console.log(result);
    }

    client.quit();
  });
});
