import socket

def run_server():

    while True:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_ip = "127.0.0.1"
        port = 8000

        server.bind((server_ip, port))

        server.listen(0)
        print(f"Listening on { server_ip }: { port }")

        client_socket, client_address = server.accept()
        print(f"Accepted connection from { client_address[0] }: { client_address[1] }")

        sum = 0

        while True:

            msg = client_socket.recv(1024).decode("ascii").strip()
            print(msg)

            if msg == "=":
                response = str(sum).encode("ascii")
                client_socket.send(response)

                sum = 0
            elif msg == "close":
                break
            else:
                sum += int(msg)

        client_socket.send("closed".encode("ascii"))
        client_socket.close()
        print(f"Connection to client { client_address[0] }: { client_address[1] } close")
        # server.close()

if __name__ =="__main__":
    run_server()
        


