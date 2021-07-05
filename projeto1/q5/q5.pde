// circle center 
float x=250;
float y=250;
 
// that is added to the angle
float pos=0.1;
 
void setup ()
{
  size(500, 500);
  frameRate(30);
}
 
void draw ()
{ 
  background(200);
  fill(200);
  stroke(0, 0, 255);
  strokeWeight(2);
  ellipse(x, y, 250, 250);
  circulo(100, -0.1);
}
void circulo(float r, float step)
{
   
  float x1 = x +  r*cos(pos); //<>//
  float y1 = y +  r*sin(pos); //<>//
 
  ellipse(x1, y1, 50, 50);
  
 
  stroke(0, 0, 255);
  strokeCap(ROUND);
  stroke(255, 0, 0);
  x1 = x1 + 25f*cos(-pos*4);
  y1 = y1 + 25f*sin(-pos*4);
  fill(255, 0, 0);
  circle(x1, y1, 5); //<>//
  
  
  pos+=0.5*step; //<>//
}
