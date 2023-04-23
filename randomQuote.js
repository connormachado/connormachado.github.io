function randomQuote(){
    const quoteList = [
        {   firstname: "Theo_Dwyer", 
            Quote: "i cut through a penny once, yea with sciccors"},
        {   firstname: "Cassie_Richardson", 
            Quote: "i don't get sick, i just get drunk"},
        {   firstname: "Theo_Dwyer", 
            Quote: "these dudes must be virgins"},
        {   firstname: "Mady_Ockner", 
            Quote: "even i'm not aware of my own thoughts"},
        {   firstname: "Logan_Ockner", 
            Quote: "did you say it smells like boob in here?"},
        {   firstname: "Theo_Dwyer", 
            Quote: "connor i fucked up there's a soybean in the room"},
        {   firstname: "Jack_Gibberd", 
            Quote: "there's a really cool book called bomb"},
        {   firstname: "Braeden", 
            Quote: "i had a half meal of 5 vending machine snacks"},
        {   firstname: "Theo_Dwyer", 
            Quote: "who would've thought paying attention helped so much"},
        {   firstname: "Nathan_Strope", 
            Quote: "i would've cried but i'm not a woman, i got that Y chromosome that asks 'Y are you crying'"},
        {   firstname: "Mady_Ockner", 
            Quote: "i was thinking about this the other day...wait what am i saying i was thinking about it now"},
        {   firstname: "Connor_Machado", 
            Quote: "never spend your diamonds on a hoe man, she should be content with the coal man"},
        {   firstname: "Mady_Ockner", 
            Quote: "i'm like hermione granger with her time turner in my head"},
        {   firstname: "Mady_Ockner", 
            Quote: "fuck being normal i want to be ab-normal"},
        {   firstname: "Logan_Ockner", 
            Quote: "i hate that place, it's cause they accused me of giving Xanax to a dog"},
        {   firstname: "Logan_Ockner", 
            Quote: "why the fuck would i give Xanax to a dog"},
        {   firstname: "Connor_Machado", 
            Quote: "i like making easy things hard, makes them more worth it"},
        {   firstname: "Connor_Machado", 
            Quote: "genetic disaster-piece"},
        {   firstname: "Mady_Ockner",
            Quote: "call me ed sheeran the way i'm ginger"}
    ]

    // Blue -> Purple
    // Purple -> Green
    // Green -> Orange
    // Orange -> Blue

    keys = Object.keys(quoteList);
    newText = quoteList[keys[Math.floor(keys.length * Math.random())]];
    StickyNote.textContent = newText.Quote;

    currentNote = document.getElementById("Sticky Note");

    function resetColor(oldClass, newClass){
        currentNote.classList.remove(oldClass);
        currentNote.classList.remove(newClass);
    }
    
    // If the returned list is not empty then the current sticky note is that color
    if( (document.getElementsByClassName("buttonBlue")).length() != 0){
        resetColor("buttonBlue", "buttonPurple");
    }else if ((document.getElementsByClassName("buttonPurple")).length() != 0){
        resetColor("buttonPurple", "buttonGreen");
    }else if ((document.getElementsByClassName("buttonGreen")).length() != 0){
        resetColor("buttonGreen", "buttonOrange");
    }else if ((document.getElementsByClassName("buttonOrange")).length() != 0){
        resetColor("buttonOrange", "buttonBlue");
    }

    
}