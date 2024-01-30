#!/usr/bin/node
const request = require('request');
// Get the API URL from the command line arguments
const apiUrl = process.argv[2];

// Make a GET request to the specified API URL
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error.message);
  } else {
    try {
      // Parse the JSON response
      const tasksData = JSON.parse(body);

      // Filter completed tasks
      const completedTasks = tasksData.filter(task => task.completed);

      // Create an object to store the count of completed tasks for each user ID
      const completedTasksByUser = {};

      // Count completed tasks for each user
      completedTasks.forEach(task => {
        const userId = task.userId.toString();
        completedTasksByUser[userId] = (completedTasksByUser[userId] || 0) + 1;
      });

      // Print the results
      console.log(completedTasksByUser);
    } catch (parseError) {
      console.error('Error parsing API response:', parseError.message);
    }
  }
});
