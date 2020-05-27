let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

// Generates a random number between 0 and 10
function generateTarget(){
    a = Math.floor(Math.random() * 10);
    console.log(a)
    return a
}

// Gets absolute value of difference between numbers
function getAbsoluteDistance(num1,num2){
    return Math.abs(num1 - num2);
}


// Compares human guess to target, if lower, returns true, otherwise false
function compareGuesses(humanGuess,computerGuess,target){
    if (getAbsoluteDistance(humanGuess,target) < getAbsoluteDistance(computerGuess,target)){
        return true;
    }else {
        return false;
    }
}


// Checks if human won, if so, increases the player score, otherwise increase computers
function updateScore(winner){
    if (winner == "human"){
        humanScore++;
    } else {
        computerScore++;
    }
}


// Adds one to round counter
function advanceRound(){
    currentRoundNumber ++;
}