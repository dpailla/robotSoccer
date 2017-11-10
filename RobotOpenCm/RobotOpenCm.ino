/*
* Nombre: Dennys Paillacho
* Fecha ultima actualizacion: 2017/11/10
* Programa OpenCM del robot soccer 
* 
* ID_ROBOT: ID del robot
* DATA_INDEX: indice donde empiezan los datos del robot
* DATA_SIZE: tamaño de la trama
* funciones creadas: parpadearMotores, parpadearLed
* 
*/
/* Serial device defines for dxl bus */
#define DXL_BUS_SERIAL1 1  //Dynamixel on Serial1(USART1)  <-OpenCM9.04
#define DXL_BUS_SERIAL2 2  //Dynamixel on Serial2(USART2)  <-LN101,BT210
#define DXL_BUS_SERIAL3 3  //Dynamixel on Serial3(USART3)  <-OpenCM 485EXP
/* Dynamixel ID defines */
#define ID_NUM 1
/* Control table defines */
#define GOAL_POSITION 30

//#include <DynamixelSerial1.h>
Dynamixel Dxl(DXL_BUS_SERIAL1);

#define MOTOR_LEFT 2
#define MOTOR_RIGHT 1
#define ID_ROBOT 2
#define DATA_INDEX 3
#define DATA_SIZE 8

int inData[DATA_SIZE];

int index=-1;
int dato;
int velLeft = 0;
int velRight = 0;
int dirLeft;
int dirRight;

void setup(){
  // Set up the built-in LED pin as an output:
    pinMode(BOARD_LED_PIN, OUTPUT);
//  Serial.begin(115200); // puerto de comunicacion de motores

  // Dynamixel 2.0 Baudrate -> 0: 9600, 1: 57600, 2: 115200, 3: 1Mbps 
//  Dxl.begin(3);

//TODO: modificar y comprobar velocidad de transmision de bus de motores

  Serial3.begin(115200); // puerto de comunicacion con el ESP
  
  Dxl.begin(3);
  Dxl.wheelMode(MOTOR_LEFT); //wheelMode() is to use wheel mode
  Dxl.wheelMode(MOTOR_RIGHT); //wheelMode() is to use wheel mode
  delay(100);

  // Movimiento de comprobacion
  //parpadearLed(10);
  delay(100);          // Wait for 0.1 second
  //Motores adelante
  Dxl.goalSpeed(MOTOR_LEFT, 100 | 0x400); 
  Dxl.goalSpeed(MOTOR_RIGHT, 100);
  delay(3000);
  //Motores atras
  Dxl.goalSpeed(MOTOR_LEFT, 100); 
  Dxl.goalSpeed(MOTOR_RIGHT, 100 | 0x400);
  delay(3000);
  Dxl.goalSpeed(MOTOR_LEFT, 0); 
  Dxl.goalSpeed(MOTOR_RIGHT, 0);
  delay(3000);
  Dxl.goalSpeed(MOTOR_LEFT, 100); 
  Dxl.goalSpeed(MOTOR_RIGHT, 100);
  delay(3000);
  Dxl.goalSpeed(MOTOR_LEFT, 0); 
  Dxl.goalSpeed(MOTOR_RIGHT, 0);
  delay(3000);
  Dxl.goalSpeed(MOTOR_LEFT, 100 | 0x400); 
  Dxl.goalSpeed(MOTOR_RIGHT, 100| 0x400);
  delay(3000);
  Dxl.goalSpeed(MOTOR_LEFT, 0); 
  Dxl.goalSpeed(MOTOR_RIGHT, 0);
  delay(3000);
//  Dxl.goalSpeed(MOTOR_LEFT, 400 | 0x400); //reverse
//  Dxl.goalSpeed(MOTOR_RIGHT, 400 | 0x400); //reverse
//  delay(500);
//  Dxl.goalSpeed(MOTOR_LEFT, 0); //reverse
//  Dxl.goalSpeed(MOTOR_RIGHT, 0); //reverse
//  parpadearLed(10);
}

void loop(){
//  while (Serial3.available()) {  
//     int iByte = Serial3.read();
//     if (iByte == 240){
//        digitalWrite(BOARD_LED_PIN, LOW);  // set to as LOW LED is turn-on
//        index = 0;
//     }
//     if (index>=0) {
//         inData[index++] = iByte;  // adding to message
//         if (iByte == 247) { //247 o 0xF7
//            digitalWrite(BOARD_LED_PIN, LOW);  // set to as LOW LED is turn-on
//             ValProcces(inData);
//             index = -1;
//         }
//     }
//  }
  
}

//Funcion para procesar pack
void ValProcces(int data[]){
  velLeft = (data[DATA_INDEX]-100)*10;
  velRight = (data[DATA_INDEX+1]-100)*10;
  if (velLeft > 0){
    velLeft = velLeft | 0x400;
   }
  if (velRight<0){
    velRight = velRight | 0x400;
  }
  Dxl.goalSpeed(MOTOR_LEFT, velLeft); 
  Dxl.goalSpeed(MOTOR_RIGHT, velRight); 
}

void parpadearLed(int veces){
  for (int i = 0; i < veces; i++){
    digitalWrite(BOARD_LED_PIN, LOW);
    delay(100);              // wait for a second
    digitalWrite(BOARD_LED_PIN, HIGH);
    delay(100);              // wait for a second
  }
}

