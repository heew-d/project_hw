from flask import Flask, jsonify, render_template, request
from flask import make_response
from flask import Response
from flask import Request
from multiprocessing import Process
import serial
import requests


app = Flask(__name__)

# PORT
# ser = serial.Serial('/dev/cu.usbserial-130', 9600)
# ser = serial.Serial('/dev/cu.bluetooth-incoming-port', 9600)
ser = serial.Serial('/dev/cu.Vehicle', 9600)

# def serial_start():
#     ser = serial.Serial('/dev/cu.usbserial-1230', 115200)
    # stop_flag = False
    # while not stop_flag:
    #     if ser.readable():
    #         res = ser.readline()
    #         res_decode = res.decode()
    #         print(res_decode)

@app.route('/')
def home():
    # return 'Hello, World!'
    return render_template('view.html')
    # Response(serial_start())
    # return render_template('view.html')
    # arduino = serial.Serial('/dev/cu.usbserial-1230', 115200)
    # y = arduino.readline()
    # return y

@app.route('/view')
def view():
    return render_template('view.html')

@app.route('/btn1')
def btn1():
    print('btn1')
    # 시리얼 통신
    if ser.writable():
        ser.write("1".encode('utf-8'))
    return render_template('view.html')

@app.route('/btn2')
def btn2():
    print('btn2')
    # 시리얼 통신
    if ser.writable():
        ser.write("2".encode('utf-8'))
    
    return render_template('view.html')


@app.route('/btn3')
def btn3():
    print('btn3')
    # 시리얼 통신
    if ser.writable():
        ser.write("3".encode('utf-8'))
    
    return render_template('view.html')   

@app.route('/btn4')
def btn4():
    print('btn4')
    # 시리얼 통신
    if ser.writable():
        ser.write("4".encode('utf-8'))
    
    return render_template('view.html')  

@app.route('/msg', methods=['GET'])
def test_get():
    msg_receive = request.args.get('msg')

    print(msg_receive)
    if ser.writable():
        # while msg_receive == previous:
        ser.write(msg_receive.encode('utf-8'))
            
    return render_template('view.html')
    
def run():
     app.run(host='127.0.0.1', port=9999)

if __name__ == '__main__':
    # app.run(debug=True)
    # app.run(host='127.0.0.1', port=9999)
    # serial_start()
    p1 = Process(target=run)
    p1.start()