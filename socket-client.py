import socket 
import cv2
import numpy as np
import base64


# HOST = '127.0.0.1'
# HOST = '192.168.0.49'
HOST = '192.168.0.19'
PORT = 9999

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((HOST, PORT)) 

recivedBuf = b''

# 키보드로 입력한 문자열을 서버로 전송하고 
# 서버에서 에코되어 돌아오는 메시지를 받으면 화면에 출력합니다. 
# quit를 입력할 때 까지 반복합니다. 
while True: 

    # message = input('Enter Message : ')
    # if message == 'quit':
    #     break

    # client_socket.send(message.encode()) 

    # data = client_socket.recv(1024) 
    # print('Received from the server :', repr(data.decode())) 

    data = client_socket.recv(1024)
    # print('Received from the server :', len(data))
    # print('Received from the server :', data, data.find(b'\x20'))
    # print('Received from the server :', data.find(b'\x20'))

    space = data.find(b'\x20')

    # # if data.find(b'\xff\xd8') > -1:
    if space > -1:

        key = cv2.waitKey(16)
        if key == 27:
            break

        # 지금까지 받은 데이터를 출력
        recivedBuf += data[:space]
        # print('Received from the server :', len(recivedBuf))
        # print('Received from the server :', recivedBuf)

        buf = base64.b64decode(recivedBuf)
        buf = np.frombuffer(buf, dtype=np.uint8)

        # buf = np.frombuffer(recivedBuf, dtype=np.uint8)
        # print('Received from the server buf:', buf)

        img = cv2.imdecode(buf, cv2.IMREAD_COLOR)
        # img = cv2.imdecode(recivedBuf, cv2.IMREAD_COLOR)
        # print('Received from the server img:', img.shape)

        cv2.imshow('cam', img)
        # cv2.imshow('cam', buf)

        recivedBuf = b''
        recivedBuf += data[space+1:]

        continue


    recivedBuf += data
    # print('Received from the server :', len(recived))

client_socket.close()