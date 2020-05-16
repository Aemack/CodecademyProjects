let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

// Write your code below:

function generateTarget(){
    a = Math.floor(Math.random() * 10);
    console.log(a)
    return a
}

function getAbsoluteDistance(num1,num2){
    return Math.abs(num1 - num2);
}

function compareGuesses(humanGuess,computerGuess,target){
    if (getAbsoluteDistance(humanGuess,target) < getAbsoluteDistance(computerGuess,target)){
        return true;
    }else {
        return false;
    }
}

function updateScore(winner){
    if (winner == "human"){
        humanScore++;
    } else {
        computerScore++;
    }
}

function advanceRound(){
    currentRoundNumber ++;
}