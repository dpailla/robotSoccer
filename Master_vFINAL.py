#DEFINICION DE LA TRAMA
# Byte[0]: 240 o 0xF0
# Byte[1]: Robot1 Motor Left
# Byte[2]: Robot1 Motor Right
# Byte[3]: Robot2 Motor Left
# Byte[4]: Robot2 Motor Right
# Byte[5]: Robot3 Motor Left
# Byte[6]: Robot3 Motor Right
# Byte[7]: 247 o 0xF7

import time
import pygame
import struct
import socket
import sys

#Inicializo la trama con cabecera 240 y fin 240, los demas datos corresponden a la velocidad 0 de los motores
dataSerial = [240,100,100,100,100,100,100,247]

#SOCKETS
Robot1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Robot2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Robot3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Robot1.settimeout(50)
# Robot2.settimeout(50)
# Robot3.settimeout(50)

#CONEXION ROBOTS
#ROBOT 1
#try:
Robot1.connect(("192.168.1.5",123))
# except socket.error:
#     pass
print("Robot1 Conectado")
time.sleep(1)

# try:
Robot2.connect(("192.168.1.6",123))
# except socket.error:
#     pass
#
print("Robot2 Conectado")

time.sleep(1)

# try:
Robot3.connect(("192.168.1.4",123))
print("Robot3 Conectado")

# except socket.error:
#     pass

time.sleep(2)
print("listos!")
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

class TextPrint:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def Print(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, [self.x, self.y])
        self.y += self.line_height

    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15

    def indent(self):
        self.x += 10

    def unindent(self):
        self.x -= 10


pygame.init()

# Set the width and height of the screen [width,height]
size = [500, 700]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initialize the joysticks
pygame.joystick.init()

# Get ready to print
textPrint = TextPrint()


axis_data = None
# -------- Main Program Loop -----------
while done==False:


    # EVENT PROCESSING STEP
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
        #if event.type == pygame.JOYAXISMOTION and (event.axis == 1 or event.axis == 3):
        #    axis_data[event.axis] = round(event.value, 2)
        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        if event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")


        # DRAWING STEP
        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(WHITE)
        textPrint.reset()

        # Get count of joysticks
        joystick_count = pygame.joystick.get_count()

        textPrint.Print(screen, "Number of joysticks: {}".format(joystick_count) )
        textPrint.indent()

#ojo        dataSerial = [254]

        # For each joystick:
        for i in range(joystick_count):
            joystick = pygame.joystick.Joystick(i)
            joystick.init()

            textPrint.Print(screen, "Joystick {}".format(i) )
            textPrint.indent()

            # Get the name from the OS for the controller/joystick
            name = joystick.get_name()
            textPrint.Print(screen, "Joystick name: {}".format(name) )

            # Usually axis run in pairs, up/down for one, and left/right for
            # the other.
            axes = joystick.get_numaxes()
            textPrint.Print(screen, "Number of axes: {}".format(axes) )
            textPrint.indent()

             #LISTA PARA PAQUETE DE DATOS CON CABECERA
            axisLeft = joystick.get_axis(1)
            axisRight = joystick.get_axis(3)

            textPrint.Print(screen, "Axis left {} value: {:>6.3f}".format(1, axisLeft))
            textPrint.Print(screen, "Axis right {} value: {:>6.3f}".format(3, axisRight))

            velLeft = int(100.0 - (axisLeft**3 * 100.0))

            velRight = int(100.0 - (axisRight**3 * 100.0))


            if axisLeft==0:

                velLeft=101

            if axisRight==0:

                velRight=101

            Shot=joystick.get_button(1)

            if (i==0):
                dataSerial[1] = velLeft
                dataSerial[2] = velRight
            elif (i == 1):
                dataSerial[3] = velLeft
                dataSerial[4] = velRight
            elif (i == 2):
                dataSerial[5] = velLeft
                dataSerial[6] = velRight


            textPrint.unindent()

            buttons = joystick.get_numbuttons()
            #textPrint.print(screen, "Number of buttons: {}".format(buttons) )
            textPrint.indent()

            for i in range(buttons):
                button = joystick.get_button( i )
                #textPrint.print(screen, "Button {:>2} value: {}".format(i,button) )
            textPrint.unindent()

            # Hat switch. All or nothing for direction, not like joysticks.
            # Value comes back in an array.
            hats = joystick.get_numhats()
            #textPrint.print(screen, "Number of hats: {}".format(hats) )
            textPrint.indent()

            for i in range( hats ):
                hat = joystick.get_hat( i )
                #textPrint.print(screen, "Hat {} value: {}".format(i, str(hat)) )
            textPrint.unindent()
            textPrint.unindent()

        dfSerial=struct.pack("8B", *dataSerial)

        # Limit to 20 frames per second
        clock.tick(20)

        try:
            Robot1.send(dfSerial)
        except:
            pass

        try:
            Robot2.send(dfSerial)
        except:
            pass

        try:
            Robot3.send(dfSerial)
        except:
            pass

        print(dfSerial)

        pygame.display.flip()


Robot1.close()
Robot2.close()
Robot3.close()

pygame.quit ()