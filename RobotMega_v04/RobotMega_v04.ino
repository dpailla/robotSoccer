/*
* Programa del robot en Arduino MEGA
* Codigo del robot
* ID_ROBOT: ID del robot
* DATA_INDEX: indice donde empiezan los datos del robot
* DATA_SIZE: tamaño de la trama
* funciones creadas: parpadearMotores, parpadearLed
* 
*/
#include <DynamixelSerial1.h>


#define MOTOR_LEFT 1
#define MOTOR_RIGHT 2
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
  // initialize digital pin 13 as an output.
  pinMode(13, OUTPUT);
  Serial.begin(115200);
  Serial3.begin(115200);
  
  Dynamixel.begin(1000000,2);  // Inicialize the servo at 1Mbps and Pin Control 2
  delay(1000);
  Dynamixel.setEndless(MOTOR_LEFT,ON);
  Dynamixel.setEndless(MOTOR_RIGHT,ON);

  Dynamixel.turn(1,LEFT,500);
  Dynamixel.turn(2,LEFT,500);
  delay(500);
  //Gira contra manecillas de reloj
  Dynamixel.turn(1,RIGTH,500);
  Dynamixel.turn(2,RIGTH,500);
  delay(500);
  Dynamixel.turn(1,LEFT,0);
  Dynamixel.turn(2,LEFT,0);
  
  
}

void loop(){
  while (Serial3.available()) {  
     int iByte = Serial3.read();
    //Serial.println(iByte);
     
     //Serial.println(iByte);
     if (iByte == 240){
        digitalWrite(13, HIGH);   // turn the LED on (HIGH is the voltage level)

//         Serial.println("Inicio");
         index = 0;
     }
  
     if (index>=0) {
         inData[index++] = iByte;  // adding to message
         if (iByte == 247) { //247 o 0xF7
            
            digitalWrite(13, LOW);   // turn the LED on (HIGH is the voltage level)
//             Serial.write("vel");
             //Serial.write(inData[1]);
             ValProcces(inData);
             index = -1;
//             Serial.println("Fin");
         }
     }
  }
  
}

//Funcion para procesar pack
void ValProcces(int data[]){
  velLeft = (data[DATA_INDEX]-100)*10;
  velRight = (data[DATA_INDEX+1]-100)*10;
  if (velLeft > 0){
    dirLeft = RIGTH;
   }
   else{
    dirLeft = LEFT;
   }
  
  if (velRight>0){
    dirRight = LEFT;
  }
  else
  {
    dirRight = RIGTH;
  }
  velLeft = abs(velLeft);
  velRight = abs(velRight);
  Dynamixel.turn(MOTOR_LEFT, dirLeft, velLeft); 
  Dynamixel.turn(MOTOR_RIGHT, dirRight , velRight); 
   
}

void parpadearLed(int veces){
  for (int i = 0; i < veces; i++){
    digitalWrite(13, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(200);              // wait for a second
    digitalWrite(13, LOW);    // turn the LED off by making the voltage LOW
    delay(200);              // wait for a second
  }
}
void parpadearMotores(int veces){
  for (int i = 0; i < veces; i++){
    Dynamixel.ledStatus(1,ON);           // Turn ON the LED
    Dynamixel.ledStatus(2,ON);           // Turn ON the LED
    delay(200);
    Dynamixel.ledStatus(1,OFF);           // Turn ON the LED
    Dynamixel.ledStatus(2,OFF);           // Turn ON the LED
    delay(200);
  }
}

