function makeNote(color){
    myTable = document.getElementById("QuoteWall");
    tr = myTable.insertRow(-1);


    newButton = document.createElement("BUTTON");
    newButton.id = "firstID"
    newButton.text = "hello World?"
    newButton.classList.add('stickyNote')
    
    newButton.innerHTML = '<img src=sn.png />';


    tr.appendChild(newButton)
}