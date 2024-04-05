// Function to send a message to the chatbot server API
function sendMessage(message) {
    // Replace with your actual API endpoint URL
    const url = "http://localhost:5000/chat";
  
    // Create a new XMLHttpRequest object (consider using Fetch API for newer browsers)
    const xhr = new XMLHttpRequest();
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
  
    // Convert the message to JSON (if your API expects it)
    const data = JSON.stringify({ message: message });
  
    // Handle the response from the chatbot server
    xhr.onload = function() {
      if (xhr.status === 200) {
        const response = JSON.parse(xhr.responseText);
        displayResponse(response.response);  // Call function to display response
      } else {
        console.error("Error sending message:", xhr.statusText);
        // Handle errors appropriately (e.g., display an error message to the user)
      }
    };
  
    // Send the message data to the server
    xhr.send(data);
  }
  
  // Function to display the chatbot's response on the webpage
  function displayResponse(message) {
    // Replace with your logic to display the response in your website's UI
    // (e.g., update a DOM element with the message content)
    const chatArea = document.getElementById("chat-area");
    const responseElement = document.createElement("p");
    responseElement.textContent = "Chatbot: " + message;
    chatArea.appendChild(responseElement);
  }
  
  // Example usage (replace with your logic to capture user messages)
  const userInput = document.getElementById("user-message");
  userInput.addEventListener("keyup", function(event) {
    if (event.keyCode === 13) { // Check if Enter key is pressed
      const message = userInput.value;
      sendMessage(message);
      userInput.value = ""; // Clear the input field after sending
    }
  });
  