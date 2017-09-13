/*Serial3_Echo
 
 Demonstrates sending data from the computer to the CM900, OpenCM9.04
 echoes it to the computer again.
 You can just type in terminal program, character you typed will be displayed
 
 You can connect the below products to J9 Connector in CM900, OpenCM9.04
 [BT-110A] or [BT-110A Set]
 http://www.robotis-shop-kr.com/goods_detail.php?goodsIdx=875
 [ZIG-110A Set]
 http://www.robotis-shop-kr.com/goods_detail.php?goodsIdx=405
 [LN-101] download tool in CM-100
 http://www.robotis-shop-kr.com/goods_detail.php?goodsIdx=348
 
 You can also find all information about ROBOTIS products
 http://support.robotis.com/
 
                  Compatibility
 CM900                  O
 OpenCM9.04             O

 created 16 Nov 2012
 by ROBOTIS CO,.LTD.
 */

/*
Serial1 : Dynamixel_Poart
 Serial2 : Serial_Poart(4pin_Molex)
 Serial3 : Serial_Poart(pin26:Tx3, pin27:Rx3)
 
 TxD3(Cm9_Pin26) <--(Connect)--> RxD(PC)
 RxD3(Cm9_Pin27) <--(Connect)--> TxD(PC)
 */
 /* Serial device defines for dxl bus */
#define DXL_BUS_SERIAL1 1  //Dynamixel on Serial1(USART1)  <-OpenCM9.04
#define DXL_BUS_SERIAL2 2  //Dynamixel on Serial2(USART2)  <-LN101,BT210
#define DXL_BUS_SERIAL3 3  //Dynamixel on Serial3(USART3)  <-OpenCM 485EXP
/* Dynamixel ID defines */
#define ID_NUM1 1
#define ID_NUM2 2
#define CCW_Angle_Limit 8
#define GOAL_SPEED 32
#define ID_ROBOT 1


Dynamixel Dxl(DXL_BUS_SERIAL1);
int data[2];
int velLeft = 0;
int velRight = 0;

//Funcion para procesar pack
/*void tomarValores(){
  
  int Pos = ((ID*2)-1)
  
  for(int i = Pos;i<(Pos+3);i++)
     data[i] = Serial.read(); 
  
  for(int i = 0; i <(len(data));i++)
     Serial.write(datadata[i])
}

*/
void setup(){
  //Serial3 Serial initialize
  Dxl.begin(3);
  //AX MX RX Series
  Dxl.writeWord(ID_NUM1, CCW_Angle_Limit, 0); 
  Dxl.writeWord(ID_NUM2, CCW_Angle_Limit, 0); 
  SerialUSB.begin();  
}

void loop(){
  

  // when you typed any character in terminal
  while (SerialUSB.available() < 5);    // wait until a full packet has been buffered (infinite loop risk alert)
  for (int i = 0; i < 2; i++){
      data[i] = SerialUSB.read();
      SerialUSB.println("Robot:  ");
      SerialUSB.write(data[i]);
      }
      
//  velLeft = (int(data[0])-100)*1023/100;
//  velRight = (int(data[1])-100)*1023/100;
//  if (velLeft <0){
//    velLeft = abs(velLeft)|0x400;
//  }
//  if (velRight>0){
//      velRight = velRight|0x400;
//  }
//  else
//  {
//    velRight = abs(velRight);
//  }
//  Dxl.writeWord(ID_NUM1, GOAL_SPEED, velLeft); 
//  Dxl.writeWord(ID_NUM2, GOAL_SPEED, velRight); 

  //Serial.write(velLeft);
  //print(velLeft)

}

