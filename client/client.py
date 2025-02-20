import socket

def run_client():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = "127.0.0.1"
    port = 8000

    client.connect((server_ip, port))

    try:
        while True:

            msg = input("Enter: ")
            client.send(msg.encode("ascii")[:1024])

            if msg == "=":
                response = client.recv(1024)
                response = response.decode("ascii")
                print(f"Received: {response}")

                break

    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        client.close()
        print("Connection to server closed")

if __name__ =="__main__":
    run_client()