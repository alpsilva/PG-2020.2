float firstArmX, firstArmY;
float secondArmX, secondArmY;
float firstArmLength = 100;
float secondArmLength = 150;
float firstArmAngle = PI;
float secondArmAngle = PI;
float firstArmAngularSpeed = - PI/240;
float secondArmAngularSpeed = - PI/120;

void setup() {
  size(800,600);
  frameRate(60);
  smooth();
}

void draw() {
  background(155);
  setupCoordinates(width/2, height/2);
  
  updateArmsPosition();
  if (secondArmAngle >= HALF_PI) {
    stepAnimation();
  }
  
  drawArm(firstArmX,firstArmY);
  translate(firstArmX,firstArmY);
  drawArm(secondArmX,secondArmY);
}

void stepAnimation() {
  firstArmAngle = firstArmAngle + firstArmAngularSpeed;
  secondArmAngle = secondArmAngle + secondArmAngularSpeed;
}

void updateArmsPosition() {
  firstArmX = firstArmLength * sin(firstArmAngle);
  firstArmY = firstArmLength * cos(firstArmAngle);
  
  secondArmX = secondArmLength * sin(secondArmAngle);
  secondArmY = secondArmLength * cos(secondArmAngle);
}

void drawArm(float x, float y) {
  stroke(255,255,255);
  strokeWeight(4);
  line(0,0,x,y);
  strokeWeight(10);
  stroke(0,0,0);
  point(0,0);
  point(x,y);
}

void setupCoordinates(float originX, float originY) {
  translate(originX, originY);
  scale(1,-1);
}
