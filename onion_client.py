import socket

def layer1(data):
    """
    adds "layer1" 10 times to the
    :param data:
    :return: data with 10xlayer1 added
    """
    data=data+"layer1"*10
    return data

def layer2(data):
    """
    adds "_____" 10 times to the
    :param data:
    :return: data with 10x_____ added
    """
    data=data+"_____"*10
    return data

def layer3(data):
    """
    adds "1111111" 10 times to the
    :param data:
    :return: data with 10x1111111 added
    """
    data=data+"1111111"*10
    return data

def layer4(data):
    """
    adds "HaHa" 10 times to the
    :param data:
    :return: data with 10xHaHa added
    """
    data=data+"HaHa"*10
    return data

def layer5(data):
    """
    adds "last" 10 times to the
    :param data:
    :return: data with 10xlast added
    """
    data=data+"last"*10
    return data

my_socket = socket.socket()

try:
	my_socket.connect(('127.0.0.1', 1450))
except Exception as e:
	print(str(e))
	my_socket.close()
	exit("The server is down")

while True:
    try:
        inp_user = input("insert text")
        inp_user = layer1(inp_user)
        print(inp_user)
        inp_user = layer2(inp_user)
        print(inp_user)
        inp_user = layer3(inp_user)
        print(inp_user)
        inp_user = layer4(inp_user)
        print(inp_user)
        inp_user = layer5(inp_user)
        print(inp_user)
        my_socket.send(str(len(inp_user)).zfill(4).encode())
        my_socket.send(inp_user.encode())
        data_len = int(my_socket.recv(4).decode())
        data = my_socket.recv(data_len).decode()
        print(data)

    except Exception as e:
        print(str(e))
        exit("error in receive or sending")
my_socket.close()