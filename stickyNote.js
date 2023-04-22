class stickyNote{
    constructor() {
        this.height = 200;
        this.width = 200;
        this.text = 'Creation Time'; //Maybe have random inspirational quotes 
        this.color = "blue";
      }

    changeText(newText){
        this.text = newText
    }

    changeColor(newColor){
        this.color = newColor;
    }


    makeNote(color){
        myTable = document.getElementById("QuoteWall");
        tr = myTable.insertRow(-1);


        x = document.createElement("BUTTON");
        x.onclick = this.changeText("Hello World!")

        tr.appendChild(x)

        x.width = 50;
        x.height = 50;
    }

}