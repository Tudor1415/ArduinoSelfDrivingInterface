import serial
import win32api
import pygame
import sys
import time
# from serial import Serial
pygame.init()
pygame.init()
BLACK = (0,0,0)
WIDTH = 400
HEIGHT = 400
windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

windowSurface.fill(BLACK)

Arduino_Serial = serial.Serial('com5',9600)
print (Arduino_Serial.readline())
print ("Use Z Q S D to navigate and E to exit!")
main = True
while main==True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
            main = False

        if event.type == pygame.KEYDOWN:
            # if event.key == ord('f'):
            #     Arduino_Serial.write(str.encode('1'))
            #     print ("forward-left")
            # elif event.key == ord('h'):
            #     Arduino_Serial.write(str.encode('2'))
            #     print ("forward-right")
            # elif event.key == ord('v'):
            #     Arduino_Serial.write(str.encode('3'))
            #     print ("backward-left")
            # elif event.key == ord('n'):
            #     Arduino_Serial.write(str.encode('4'))
            #     print ("backward-right")

            if event.key == ord('a'):
                Arduino_Serial.write(str.encode('l'))
                print ("left")
            elif event.key == ord('d'):
                Arduino_Serial.write(str.encode('r'))
                print ("right")
            elif event.key == ord('w'):
                Arduino_Serial.write(str.encode('f'))
                print ("forward")
            elif event.key == ord('s'):
                Arduino_Serial.write(str.encode('b'))
                print ("backward")


        if event.type == pygame.KEYUP:
            # if event.key == ord('a'):
            #     Arduino_Serial.write(str.encode('o1'))
            #     print('forward-left stop')
            # elif event.key == ord('d'):
            #     Arduino_Serial.write(str.encode('o1'))
            #     print('forward-right stop')
            # elif event.key == ord('w'):
            #     Arduino_Serial.write(str.encode('o1'))
            #     print('backward-left stop')
            # elif event.key == ord('s'):
            #     Arduino_Serial.write(str.encode('o1'))
            #     print('backward-right stop')
            if event.key == ord('f'):
                Arduino_Serial.write(str.encode('o'))
                print('left stop')
            elif event.key == ord('h'):
                Arduino_Serial.write(str.encode('o'))
                print('right stop')
            elif event.key == ord('v'):
                Arduino_Serial.write(str.encode('o'))
                print('forward stop')
            elif event.key == ord('n'):
                Arduino_Serial.write(str.encode('o'))
                print('backward stop')
            elif event.key == ord('e'):
                pygame.quit()
                sys.exit()
                main = True