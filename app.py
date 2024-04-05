from flask import Flask, request, jsonify, send_from_directory
from chatbot import get_chatbot_response
import win32file
import platform
import waitress



app = Flask(__name__) 

@app.route("/")
def index():
  return app.send_static_file("index.html")


@app.route("/chat", methods=["POST"])
def chat():
  user_input = request.get_json()["message"]  # Get user input from JSON payload
  response = get_chatbot_response(user_input)
  return jsonify({"response": response})  # Send chatbot response as JSON

if __name__ == "__main__":
  waitress.serve(app, host= "0.0.0.0", port=5000)  # Run the Flask app in debug mode
