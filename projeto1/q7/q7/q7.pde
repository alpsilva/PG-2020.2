float totalFrames = 30 * 8;

float sphereX = 400;
float sphereY = 100;
float sphereZ = 0;
float pathProgress = 0.0;
float angularSpeed;
float currentPathAngle = PI;
float currentPathRadius = 500;
float pathRadiusCenterX = 400;
float pathRadiusCenterZ = 500;

float milestoneB = PI/2 * 500; //<>//
float milestoneD = milestoneB + PI * 100;
float milestoneE = milestoneD + milestoneB;

float linearSpeed = milestoneE / totalFrames;
float speedY = 200/totalFrames;

void setup() {
  size(800,600, P3D);
  frameRate(30);
  smooth();
}

void draw() {
  background(200,200,200);
  setupCoordinates();
  drawBasis();
  
  if (pathProgress <= milestoneB) {
    currentPathRadius = 500;
    pathRadiusCenterX = 400;
    pathRadiusCenterZ = 500;
  } else if (pathProgress > milestoneB && pathProgress <= milestoneD) {
    currentPathRadius = 100;
    pathRadiusCenterX = 0;
    pathRadiusCenterZ = 500;
  } else if ( pathProgress <= milestoneE) {
    currentPathRadius = 500;
    pathRadiusCenterX = -400;
    pathRadiusCenterZ = 500;
  } else {
    linearSpeed = 0.0;
    speedY = 0.0;
  }
  
  updateSpherePosition();
  drawSphere();
}

void updateSpherePosition () {
  pathProgress = pathProgress + linearSpeed;
  angularSpeed = linearSpeed / currentPathRadius;
  currentPathAngle = currentPathAngle + angularSpeed;
  
  sphereX = pathRadiusCenterX + sin(currentPathAngle) * currentPathRadius;
  sphereZ = pathRadiusCenterZ + cos(currentPathAngle) * currentPathRadius;
  sphereY = sphereY - speedY;
}

void drawSphere() {
  noStroke();
  lights();
  translate(sphereX,sphereY,sphereZ);
  sphere(20);
}

void setupCoordinates() {
  translate(width/2,height/2,0);
  rotateX(PI/4);
  rotateZ(PI/4);
  scale(0.25,0.25,0.25);
}

void drawBasis() {
  strokeWeight(4);
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
