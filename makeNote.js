function makeNote(color){
    myTable = document.getElementById("QuoteWall");
    tr = myTable.insertRow(-1);


    x = document.createElement("BUTTON");
    x.id = "firstID"
    x.text = "hello World?"
    //x.onclick = this.changeText("Hello World!")

    tr.appendChild(x)

    x.width = 50;
    x.height = 50;
}