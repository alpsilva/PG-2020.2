float x, y;
float xSpeed, ySpeed;

void setup(){
  size(640, 480);
   
  x = 15;
  y = 300;
  
  xSpeed = 5; //velocidade horizontal ajustava para o período de ida e volta de 4s
  ySpeed = 10; //valor da gravidade
}

void draw(){
  background(155);
  fill(0, 0, 255);
  circle(x, y, 30);
  fill(255, 0, 0);
  rect(0, 315, 640, 165);
  
  x = x + xSpeed; //x recebe um adicional de xspeed para acelerar lateralmente
  y = y + ySpeed; //y recebe um adicional de yspeed para acelerar horizontalmente
  
  ySpeed = ySpeed + 0.5;
  
  if(x >= width - 15){
    xSpeed = -xSpeed;
  }else if(x <= 15){
    xSpeed = -xSpeed;
  }
  
  if(y >= 300){
    ySpeed = -ySpeed + 0.5;
    y = 300;
    
  }else if(y <= 0){
    ySpeed = -ySpeed;
  }

}
