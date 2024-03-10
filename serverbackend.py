from flask import Flask, render_template, request, redirect, url_for, Response, flash, jsonify
from neuralintents import BasicAssistant

app = Flask(__name__)

from train import assistant

# Add CORS headers to allow requests from all origins
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

@app.route("/send_message", methods=["POST"])
def send_message():
    message = request.form["message"]
    response = assistant.process_input(message)
    return jsonify({"response": response})

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000, debug=False)
