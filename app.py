from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY']='secret!'
socketapp = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

@socketapp.on('message')
def handle_message(message):
    print('received message: ' + message)

if __name__ == "__main__":
    print("starting")
    socketapp.run(app)
    # app.run()
    print("postrunline")
