from flask import Flask, render_template, request, redirect, url_for, Response, flash, jsonify
from neuralintents import BasicAssistant

app = Flask(__name__)

from train import assistant

@app.route("/send_message", methods=["POST"])
def send_message():
    message = request.form["message"]
    response = assistant.process_input(message)
    return jsonify({"response": response})

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000, debug=False) 