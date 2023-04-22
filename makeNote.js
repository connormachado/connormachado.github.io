function makeNote(color){
    myTable = document.getElementById("QuoteWall");
    tr = myTable.insertRow(-1);


    newButton = document.createElement("BUTTON");
    newButton.id = "firstID"
    newButton.textContent = "Hello World?";
    newButton.classList.add('stickyNote')
    newButton.classList.add('buttonGreen')

    if (color = "Green"){
        newButton.classList.add('buttonGreen')
    }else if(color = "Blue"){
        newButton.classList.add('buttonBlue')
    }

    tr.appendChild(newButton)
}