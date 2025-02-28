import socket

def run_client():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = "127.0.0.1"
    port = 8000

    client.connect((server_ip, port))

    try:
        while True:
            msg = ""

            while True: 
                if msg == "=":
                    # the recv system call is used to receive messages from a socket
                    response = client.recv(1024)
                    response = response.decode("ascii")
                    print(f"Received: { response }")

                    break  

                elif msg == "close":
                    break 

                else:
                    msg = input("Enter: ")
                    client.send(msg.encode("ascii"))

            if msg == "close":
                client.send(msg.encode("ascii"))
                response = client.recv(1024)
                response = response.decode("ascii")
                print(f"Received: { response }")

                break       

    except Exception as e:
        print(f"Error: { e }")
    
    finally:
        client.close()
        print("Connection to server closed")

if __name__ =="__main__":
    run_client()