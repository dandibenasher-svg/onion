import socket

def remove_layer1(data):
    """
    removes "layer1" 10 times
    :param data:
    :return: remove 10xlayer1 from data
    """
    data = data[:-60]
    return data

def remove_layer2(data):
    """
    removes "_____" 10 times
    :param data:
    :return: removes 10x_____ from data
    """
    data = data[:-50]
    return data

def remove_layer3(data):
    """
    removes "1111111" 10 times
    :param data:
    :return: removes 10x1111111 from data
    """
    data = data[:-70]
    return data

def remove_layer4(data):
    """
    removes "HaHa" 10 times
    :param data:
    :return: removes 10xHaHa from data
    """
    data = data[:-40]
    return data

def remove_layer5(data):
    """
    removes "last" 10 times
    :param data:
    :return: removes 10xlast from data
    """
    data = data[:-40]
    return data

SERVER_NAME = "DanielServer"
server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 1450))
server_socket.listen(3)



while True:
    (client_socket, client_address) = server_socket.accept()
    print(f"{client_address[0]} - connected")
    while True:
        try:
            data_len = int(client_socket.recv(4).decode())
            data = client_socket.recv(data_len).decode()
            data = remove_layer5(data)
            print(data)
            data = remove_layer4(data)
            print(data)
            data = remove_layer3(data)
            print(data)
            data = remove_layer2(data)
            print(data)
            data = remove_layer1(data)
            print(data)
            client_socket.send(str(len(data)).zfill(4).encode())
            client_socket.send(data.encode())
        except Exception as e:
            print(f"error in send & recv {str(e)}")
            break

    client_socket.close()