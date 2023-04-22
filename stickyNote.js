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
        var canvas = document.getElementById("QuoteWall");
        if (canvas.getContext){
            var ctx = canvas.getContext('2d');
            ctx.fillStyle = color;    
            var x = document.createElement("BUTTON");
            x.onclick = this.changeText("Hello World!")
            x.width = 50;
            x.height = 50;
        }
    }

}