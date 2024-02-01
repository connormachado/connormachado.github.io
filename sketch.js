function setup() {
    createCanvas(720, 400);
    background(230);
    strokeWeight(2);
    ellipseList = [];
  }

  function keepEllipse(x, y, a, b, color){
    //Save an ellipse for later use
    newE = [x, y, a, b, color]
    ellipseList.push(newE)
    console.log(newE, ellipseList.length)
  }
  
  function draw() {
    background(220);

    //Draw previously clicked ellipses from earlier
    for (let i=0; i < ellipseList.length; i++) {
      tempE = ellipseList[i];
      ellipse(tempE[0], tempE[1], tempE[2], tempE[3])
      fill(tempE[4])
    }
 
    //The aim of the function, change this later
    line(mouseX - 66, mouseY, mouseX + 66, mouseY);
    line(mouseX, mouseY - 66, mouseX, mouseY + 66);
  }

  function mouseClicked(){
    //Mouse clicks once
    //Add in the radius changer here
    // https://editor.p5js.org/awade5/sketches/H1W0g19BX
    myColor = color(random(255), random(255), random(255));
    keepEllipse(mouseX, mouseY, 20, 20, myColor)
    stroke(255);
  }