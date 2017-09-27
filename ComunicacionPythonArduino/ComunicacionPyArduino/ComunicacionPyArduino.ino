/*
 * 2017/09/27: Programa ejemplo de comunicacion con Python
 */
int inData[5];
int index=-1;

void setup() {
  // initialize digital pin 13 as an output.
  pinMode(13, OUTPUT);
  Serial.begin(1000000);
}

void loop(){
  while (Serial.available()) {   
     int iByte = Serial.read();
  
     if (iByte == 240){
//         Serial.println("Inicio");
         index = 0;
     }
  
     if (index>=0) {
         inData[index++] = iByte;  // adding to message
  
         if (iByte == 247) { //247 o 0xF7
//             Serial.write("vel");
             Serial.write(inData[1]);
             index = -1;
//             Serial.println("Fin");
         }
     }
  }


}

}


