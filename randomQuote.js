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
        },
        {
            firstname: "Mady_Ockner", 
            Quote: "even i'm not aware of my own thoughts"
        },
        {
            firstname: "Logan_Ockner", 
            Quote: "did you say it smells like boob in here?"
        },
        {
            firstname: "Theo_Dwyer", 
            Quote: "connor i fucked up there's a soybean in the room"
        },
        {
            firstname: "Jack_Gibberd", 
            Quote: "there's a really cool book called bomb"
        },
        {
            firstname: "Braeden", 
            Quote: "i had a half meal of 5 vending machine snacks"
        },
        {
            firstname: "Theo_Dwyer", 
            Quote: "who would've thought paying attention helped so much"
        }
    ]


    keys = Object.keys(quoteList);
    newText = quoteList[keys[Math.floor(keys.length * Math.random())]];
    StickyNote.textContent = newText.Quote;
}