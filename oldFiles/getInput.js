function getInput(){
    quote = document.getElementById('inputQuote').value;

    newSticky = new stickyPost("Random_Name", new stickyNote(quote));
}