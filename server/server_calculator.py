import socket

def run_server():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = "127.0.0.1"
    port = 8000

    server.bind((server_ip, port))

    server.listen(0)
    print(f"Listening on { server_ip }: { port }")

    client_socket, client_address = server.accept()
    print(f"Accepted connection from { client_address[0] }: { client_address[1] }")

    sum = 0

    # receive data from client
    while True:

        addendum = client_socket.recv(1024).decode("ascii")

        if addendum == "_":
            break
        else:
            sum += int(addendum)

    response = str(sum).encode("ascii")
    client_socket.send(response)

    client_socket.close()
    print("Connection to client close")
    server.close()


if __name__ =="__main__":
    run_server()
        


