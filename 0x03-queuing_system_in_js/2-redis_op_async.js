import { createClient } from 'redis';
import { promisify } from 'util';

const run = async () => {
  // Create Redis client
  const client = createClient();

  // Handle connection errors
  client.on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err.message}`);
  });

  // Connect to Redis
  await client.connect();
  console.log('Redis client connected to the server');

  // Promisify the get function
  const getAsync = promisify(client.get).bind(client);

  // Function to set a new school value in Redis
  const setNewSchool = async (schoolName, value) => {
    try {
      const reply = await client.set(schoolName, value);
      console.log(reply); // Confirmation response
    } catch (err) {
      console.error(`Error setting school: ${err.message}`);
    }
  };

  // Function to display the value of a school using async/await
  const displaySchoolValue = async (schoolName) => {
    try {
      const value = await getAsync(schoolName);
      console.log(value);
    } catch (err) {
      console.error(`Error retrieving school value: ${err.message}`);
    }
  };

  // Example operations
  await displaySchoolValue('Holberton');
  await setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');

  // Disconnect the client
  await client.quit();
};

run().catch((err) => console.error(err));
