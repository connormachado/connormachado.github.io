function makeNote(color){
    myTable = document.getElementById("QuoteWall");
    tr = myTable.insertRow(-1);


    newButton = document.createElement("BUTTON");
    newButton.id = "firstID"
    newButton.textContent = "Hello World?";
    newButton.classList.add('stickyNote')
    newButton.classList.add('buttonTheo')

    if (color = "Theo"){
        newButton.classList.add('buttonTheo')
    }else if(color = "Blue"){
        newButton.classList.add('buttonBlue')
    }

    tr.appendChild(newButton)
}