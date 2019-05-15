from flask import Flask 
from flask_sockets import Sockets
import math

app = Flask(__name__) 
sockets = Sockets(app)

@sockets.route('/accelerometer') 
def echo_socket(ws):
	f=open("C:\\Users\\opraon\\Documents\\GitHub\\ArduinoSelfDrivingInterface\\aiModel\\speed_log.csv", "w")

	while True:
		vx = 0
		vy = 0
		vz = 0
		dt = 0.1
		message = ws.receive()
		print(message) 
		ws.send(message)
		# data = message.split(',')
		# vx += float(data[2]) * dt
		# vy += float(data[3]) * dt
		# vz += float(data[4]) * dt
		# speed = math.sqrt(vx**2 + vy**2 + vz**2)
		# print('Speed = ', speed, file = f)
	f.close()


@sockets.route('/gyroscope')
def echo_socket(ws):
	f=open("gyroscope.txt","a")
	while True:
		message = ws.receive()
		print(message)
		ws.send(message)
		print(message, file=f)
	f.close()
	
@sockets.route('/magnetometer')
def echo_socket(ws):
	f=open("magnetometer.txt","a")
	while True:
		message = ws.receive()
		print(message)
		ws.send(message)
		print(message, file=f)
	f.close()

@sockets.route('/orientation')
def echo_socket(ws):
	f=open("orientation.txt","a")
	while True:
		message = ws.receive()
		print(message)
		ws.send(message)
		print(message, file=f)
	f.close()

@sockets.route('/stepcounter')
def echo_socket(ws):
	f=open("stepcounter.txt","a")
	while True:
		message = ws.receive()
		print(message)
		ws.send(message)
		print(message, file=f)
	f.close()

@sockets.route('/thermometer')
def echo_socket(ws):
	f=open("thermometer.txt","a")
	while True:
		message = ws.receive()
		print(message)
		ws.send(message)
		print(message, file=f)
	f.close()

@sockets.route('/lightsensor')
def echo_socket(ws):
	f=open("lightsensor.txt","a")
	while True:
		message = ws.receive()
		print(message)
		ws.send(message)
		print(message, file=f)
	f.close()

@sockets.route('/proximity')
def echo_socket(ws):
	f=open("proximity.txt","a")
	while True:
		message = ws.receive()
		print(message)
		ws.send(message)
		print(message, file=f)
	f.close()

@sockets.route('/geolocation')
def echo_socket(ws):
	f=open("geolocation.txt","a")
	while True:
		message = ws.receive()
		print(message)
		ws.send(message)
		print(message, file=f)
	f.close()

	

@app.route('/') 
def hello(): 
	return 'Hello World!'

if __name__ == "__main__":
	from gevent import pywsgi
	from geventwebsocket.handler import WebSocketHandler
	server = pywsgi.WSGIServer(('0.0.0.0', 5000), app, handler_class=WebSocketHandler)
	server.serve_forever()
