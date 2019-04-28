#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
from socket import *      # Import necessary modules

ctrl_cmd = ['forward', 'backward', 'left', 'right', 'stop', 'read cpu_temp']



HOST = '192.168.1.20'    # Server(PC) IP address
PORT = 21567
BUFSIZ = 1024             # buffer size
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)   # Create a socket
tcpCliSock.connect(ADDR)                    # Connect with the server

# =============================================================================
# The function is to send the command forward to the server, so as to make the
# car move forward.
# =============================================================================
def forward_fun(event):
	print ('forward')
	cmd = bytes('forward', 'utf-8')
	tcpCliSock.send(cmd)

def backward_fun(event):
	print ('backward')
	cmd = bytes('backward', 'utf-8')
	tcpCliSock.send(cmd)

def left_fun(event):
	print ('left')
	cmd = bytes('left', 'utf-8')
	tcpCliSock.send(cmd)

def right_fun(event):
	print ('right')
	cmd = bytes('right', 'utf-8')
	tcpCliSock.send(cmd)

def stop_fun(event):
	print ('stop')
	cmd = bytes('stop', 'utf-8')
	tcpCliSock.send(cmd)



# =============================================================================
# Exit the GUI program and close the network connection between the client
# and server.
# =============================================================================
def quit_fun(event):
	top.quit()
	cmd = bytes('stop', 'utf-8')
	tcpCliSock.send(cmd)
	tcpCliSock.close()



if __name__ == '__main__':
	main()

