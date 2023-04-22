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

}