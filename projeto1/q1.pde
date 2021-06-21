float x, y;
float xSpeed, ySpeed;

void setup(){
  size(640, 480);
   
  x = 15;
  y = 465;
  
  xSpeed = 5.08f;
  ySpeed = -10;
}

void draw(){
  background(155);
  circle(x, y, 30);
  
  x = x + xSpeed;
  y = y + ySpeed;
  
  ySpeed = ySpeed + 0.5f;
  
  if(y >= 465) {
    ySpeed = -10;
  }
  
  if(x >= 625 || x <= 15) {
    xSpeed = -xSpeed;
  }
}
