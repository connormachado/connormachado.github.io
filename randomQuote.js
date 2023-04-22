function randomQuote(){
    const quoteList = [
        {
            firstname: "Theo_Dwyer", 
            Quote: "i cut through a penny once, yea with sciccors"
        },
        {
            firstname: "Cassie_Richardson", 
            Quote: "i don't get sick, i just get drunk"
        },
        {
            firstname: "Theo_Dwyer", 
            Quote: "these dudes must be virgins"
        }
    ]


    keys = Object.keys(quoteList);
    newText = quoteList[keys[Math.floor(keys.length * Math.random())]];
    StickyNote.textContent = toString(newText);
}