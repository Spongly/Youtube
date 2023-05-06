from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
    command = request.args.get("command")
    if command:
        subprocess.Popen(command.split())
    return "OK"

if __name__ == "__main__":
    app.run(host="localhost", port=8080)
