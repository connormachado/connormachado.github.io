function makeNote(color){
    myTable = document.getElementById("QuoteWall");
    tr = myTable.insertRow(-1);


    newButton = document.createElement("BUTTON");
    newButton.id = "firstID"
    newButton.text = "hello World?"
    document.getElementById("firstID").classList.add('stickyNote')
    
    newButton.innerHTML = '<img src=sn.png />';


    tr.appendChild(x)

    x.width = 50;
    x.height = 50;
}