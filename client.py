import requests


def main():
    """
    Main function to test both the send and receive services.
    """
    message_service_url = "http://localhost:5001/send_message"
    receive_service_url = "http://localhost:5002/receive_message"

    user_input = input("Enter a message to send: ")

    # Test sending a message
    try:
        response = requests.post(message_service_url, json={
                                 "message": user_input})
        print("Status Code:", response.status_code)
        print("Response Text:", response.text)
        print("Message sent:", response.json())
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

    # Test receiving a message
    try:
        response = requests.get(receive_service_url)
        print("Status Code:", response.status_code)
        print("Response Text:", response.text)
        print("Message received:", response.json())
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)


if __name__ == '__main__':
    main()
