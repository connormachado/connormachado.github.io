function changeNote(){
    const quoteList = [
        {   author: "Theo_Dwyer", 
            Quote: "i cut through a penny once, yea with sciccors"},
        {   author: "Cassie_Richardson", 
            Quote: "i don't get sick, i just get drunk"},
        {   author: "Theo_Dwyer", 
            Quote: "these dudes must be virgins"},
        {   author: "Mady_Ockner", 
            Quote: "even i'm not aware of my own thoughts"},
        {   author: "Logan_Ockner", 
            Quote: "did you say it smells like boob in here?"},
        {   author: "Theo_Dwyer", 
            Quote: "connor i fucked up there's a soybean in the room"},
        {   author: "Jack_Gibberd", 
            Quote: "there's a really cool book called bomb"},
        {   author: "Braeden", 
            Quote: "i had a half meal of 5 vending machine snacks"},
        {   author: "Sam_Shurin", 
            Quote: "who would've thought paying attention helped so much"},
        {   author: "Nathan_Strope", 
            Quote: "i would've cried but i'm not a woman, i got that Y chromosome that asks 'Y are you crying'"},
        {   author: "Mady_Ockner", 
            Quote: "i was thinking about this the other day...wait what am i saying i was thinking about it now"},
        {   author: "Connor_Machado", 
            Quote: "never spend your diamonds on a hoe man, she should be content with the coal man"},
        {   author: "Mady_Ockner", 
            Quote: "i'm like hermione granger with her time turner in my head"},
        {   author: "Mady_Ockner", 
            Quote: "fuck being normal i want to be ab-normal"},
        {   author: "Logan_Ockner", 
            Quote: "i hate that place, it's cause they accused me of giving Xanax to a dog"},
        {   author: "Logan_Ockner", 
            Quote: "why the fuck would i give Xanax to a dog"},
        {   author: "Connor_Machado", 
            Quote: "i like making easy things hard, makes them more worth it"},
        {   author: "Connor_Machado", 
            Quote: "genetic disaster-piece"},
        {   author: "Mady_Ockner",
            Quote: "call me ed sheeran the way i'm ginger"},
        {   author: "Unknown_Unknown",
            Quote: "racist?... no, RACIST racist"},
        {   Author: "JoJo_Goldin",
            Quote: "nobody's letting me be antisemitic anymore and it's making me sad"}

    ]

    testInt = 0;

    ///////////////////////////////////////
    //Change the quote in the sticky note//
    ///////////////////////////////////////

    keys = Object.keys(quoteList);
    newText = quoteList[keys[Math.floor(keys.length * Math.random())]];
    StickyNote.textContent = newText.Quote;

    ///////////////////////////////////////
    //Change the color of the sticky note//
    ///////////////////////////////////////

    // Color linked list
    // Blue -> Purple
    // Purple -> Green
    // Green -> Orange
    // Orange -> Red
    // Red -> Yellow
    // Yellow -> Pink
    // Pink -> Blue

    //NEW IDEA
    //Change addNote's color randomly too, make them opposite though


    function resetColor(oldClass, newClass){
        currentNote = document.getElementById("StickyNote");
        currentNote.classList.remove(oldClass);
        currentNote.classList.add(newClass);
    }
    
    // If the returned list is not empty then the current sticky note is that color
    if( (document.getElementsByClassName("buttonBlue")).length != 0){
        resetColor("buttonBlue", "buttonPurple");
    }else if ((document.getElementsByClassName("buttonPurple")).length != 0){
        resetColor("buttonPurple", "buttonGreen");
    }else if ((document.getElementsByClassName("buttonGreen")).length != 0){
        resetColor("buttonGreen", "buttonOrange");
    }else if ((document.getElementsByClassName("buttonOrange")).length != 0){
        resetColor("buttonOrange", "buttonRed");
    }else if ((document.getElementsByClassName("buttonRed")).length != 0){
        resetColor("buttonRed", "buttonYellow");
    }else if ((document.getElementsByClassName("buttonYellow")).length != 0){
        resetColor("buttonYellow", "buttonPink");
    }else if ((document.getElementsByClassName("buttonPink")).length != 0){
        resetColor("buttonPink", "buttonBlue");
    }

    testInt++;
    console.log(testInt);

}