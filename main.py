from multiprocessing import Process, Manager
from message_send import app as send_app
from message_receive import app as receive_app


def run_send_service(shared_queue):
    """
    Initialize and run the message sending service.
    """
    send_app.config['shared_queue'] = shared_queue
    send_app.run(port=5001)


def run_receive_service(shared_queue):
    """
    Initialize and run the message receiving service.
    """
    receive_app.config['shared_queue'] = shared_queue
    receive_app.run(port=5002)


if __name__ == "__main__":
    with Manager() as manager:
        # Create a shared queue for both services to use
        shared_queue = manager.Queue()

        # Start the services in separate processes
        p1 = Process(target=run_send_service, args=(shared_queue,))
        p2 = Process(target=run_receive_service, args=(shared_queue,))

        p1.start()
        p2.start()

        p1.join()
        p2.join()
