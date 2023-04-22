class stickyNote{
    constructor(text) {
        this.height = 200;
        this.width = 200;
        this.text = text;
        this.color = "blue";
      }

    changeText(newText){
        this.text = newText
    }

    chaneColor(newColor){
        this.color = newColor;
    }
}