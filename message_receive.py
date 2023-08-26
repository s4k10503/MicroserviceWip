from flask import Flask, jsonify
import queue

app = Flask(__name__)

# Initialize an empty queue to store messages
app.config['shared_queue'] = queue.Queue()


@app.route('/receive_message', methods=['GET'])
def receive_message():
    """
    Receive message API endpoint.

    Tries to get a message from the shared queue and returns it.
    """
    try:
        message = app.config['shared_queue'].get_nowait()
    except queue.Empty:
        message = None

    return jsonify({'message_received': message})


if __name__ == '__main__':
    app.run(port=5002)
