from flask import Flask, request, jsonify
import queue

app = Flask(__name__)

# Initialize an empty queue to store messages
app.config['shared_queue'] = queue.Queue()


@app.route('/send_message', methods=['POST'])
def send_message():
    """
    Send message API endpoint.

    Accepts JSON payload with 'message' field and puts it into a shared queue.
    """
    data = request.json
    message = data.get('message')

    # Put the message into the shared queue
    app.config['shared_queue'].put(message)

    return jsonify({'message_sent': message})


if __name__ == '__main__':
    app.run(port=5001)
