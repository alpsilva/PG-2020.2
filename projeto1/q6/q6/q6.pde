float bigCircleCenterX = 100;
float bigCircleCenterY = 100;
float bigCircleRadius = 100;
float smallCircleRadius = 25;
float smallCircleBaseAngle = 0.0;
float smallCircleBaseX, smallCircleBaseY;
float radiusRate = bigCircleRadius / smallCircleRadius;

void setup() {
  size(800,600, P3D);
}

void draw() {
  background(200,200,200);
  setupCoordinates();
  drawBasis();
  drawBigCircle();
  
  smallCircleBaseAngle = smallCircleBaseAngle + PI/120;
  
  setSmallCircleBase();
  drawSmallCircle();
}

void drawSmallCircle() {
  translate(smallCircleBaseX, smallCircleBaseY, smallCircleRadius);
  rotateX(PI/2);
  rotateY(-smallCircleBaseAngle);
  circle(0,0,50);
  stroke(255,0,0);
  strokeWeight(3);
  point(smallCircleRadius * sin(smallCircleBaseAngle * radiusRate),smallCircleRadius * cos(smallCircleBaseAngle * radiusRate),0);
}

void setSmallCircleBase() {
  smallCircleBaseX = bigCircleCenterX + sin(smallCircleBaseAngle) * bigCircleRadius;
  smallCircleBaseY = bigCircleCenterY + cos(smallCircleBaseAngle) * bigCircleRadius;
}

void drawBigCircle() {
  rotateX(PI/3);
  stroke(0,0,0);
  noFill();
  circle(bigCircleCenterX,bigCircleCenterY,2 * bigCircleRadius);
  rect(0,0,2 * bigCircleRadius,2 * bigCircleRadius);
}

void setupCoordinates() {
  translate(width/2,height/2,0);
  rotateX(PI/6);
  rotateZ(3 * PI/4);
  translate(-800,-40,-1200);
  scale(5,5,5);
}

void drawBasis() {
  strokeWeight(0.5);
  // X é vermelho.
  stroke(255,0,0);
  line(0,0,0,1000,0,0);
  // Y é verde.
  stroke(0,255,0);
  line(0,0,0,0,1000,0);
  // Z é azul.
  stroke(0,0,255);
  line(0,0,0,0,0,1000);
}
