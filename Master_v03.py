#2017/08/17 DP: envio de datos por puerto serial
# empaquetamiento de datos
#ToDo: Definir formato de trama de datos
# Verificar funcionamiento de 2 o mas joysticks
# Ojo verificar uso de sys.stdout.flush() luego de los prints para liberar buffers

import time
import pygame
import serial
import struct
import sys

#Inicializo la trama con cabecera 240 y fin 240, los demas datos corresponden a la velocidad 0 de los motores
dataSerial = [240,100,100,100,100,100,100,247]

serialPort1 = serial.Serial('COM15', timeout=None, baudrate= 1000000)  # open serial port
print("Inicializando puerto\n")
time.sleep(5)

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

# This is a simple class that will help us print to the screen
# It has nothing to do with the joysticks, just outputting the
# information.
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



checksum=[]
# def calc_checksum(string):
#     '''
#     Calculates checksum for sending commands to the ELKM1.
#     Sums the ASCII character values mod256 and takes
#     the Twos complement
#     '''
#     sum= 0
#
#     for i in range(len(string)) :
#         sum = sum + ord(string[i])
#
#     temp = sum % 256  #mod256
#     rem = temp ^ 256  #inverse
#     cc1 = hex(rem)
#     cc = cc1.upper()
#     p=len(cc)
#     return cc[p-2:p]

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


#            for i in range( axes ):
            axisLeft = joystick.get_axis(1)
            axisRight = joystick.get_axis(3)
    #            textPrint.print(screen, "Axis {} value: {:>6.3f}".format(i, axis) )

            textPrint.Print(screen, "Axis left {} value: {:>6.3f}".format(1, axisLeft))
            textPrint.Print(screen, "Axis right {} value: {:>6.3f}".format(3, axisRight))

            velLeft = int(100.0 - (axisLeft * 100.0))

            velRight = int(100.0 - (axisRight * 100.0))


            if axisLeft==0:

                velLeft=101

            if axisRight==0:

                velRight=101

            Shot=joystick.get_button(1)

            if (i==0):
                dataSerial[1] = velLeft
                dataSerial[2] = velRight

            # try:
            #     dataSerial.append(velLeft)
            #     dataSerial.append(velRight)
            #
            # except serial.SerialException:
            #     continue


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

        #
        # packet=[]
        # for i in range(len(dataSerial)):
        #
        #     packet.append(hex(dataSerial[i]))
        #
        # print(packet)
        #
        # pack = ""
        # for i in packet:
        #
        #     pack=pack+i
        #
        # pack2 = pack.replace('0','\\')
        # print(pack2)
        # #
        #
        # checksum = 0
        # for el in pack2:
        #
        #     checksum ^= ord(el)
        # print("checksum: ", hex(checksum))


        # checksum=sum(dataSerial)
        #
        # dataSerial.extend((checksum // 256, checksum % 256))

        # dataSerial.append(checksum)

        #dataSerial.append(checksum)

        #NumElements=len(dataSerial)

        dfSerial=struct.pack("8B", *dataSerial)

        # Limit to 20 frames per second
        clock.tick(20)


        try:
            serialPort1.write(dfSerial)
            print(dfSerial)

        except serial.SerialException:
            print("errorException")
            continue


        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        #read_val = serialPort.read()
    #print(read_val)
        #print("valor leido", read_val)


# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
serialPort1.close()
#serialPort2.close()
pygame.quit ()