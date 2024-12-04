import { createClient, print } from 'redis';

const client = createClient()
  .on('error', (error) => {
    console.log('Redis client not connected to the server: ', error.message);
  })
  .on('connect', () => {
    console.log('Redis client connected to the server');
  });

function setNewSchool(schoolName, value, callback) {
  // Set value in redis
  client.set(schoolName, value, (error, response) => {
    if (error) {
      console.log(error);
    } else {
      print(response); // Confirmation message
    }
    // Call callback after set operation
    if (callback) callback();
  });
}

function displaySchoolValue(schoolName, callback) {
  // Read value from store
  client.get(schoolName, (error, reply) => {
    if (error) {
      console.log(error);
    } else {
      console.log(reply);
    }
    // Call callback after get operation
    if (callback) callback();
  });
}

// Wrap everything in the connect event to ensure Redis is connected
client.on('connect', () => {
  displaySchoolValue('Holberton', () => {
    setNewSchool('HolbertonSanFrancisco', '100', () => {
      displaySchoolValue('HolbertonSanFrancisco', () => {
        client.quit();  // Ensure client quits after all operations are done
      });
    });
  });
});
