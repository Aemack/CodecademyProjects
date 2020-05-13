using System;

namespace ConsoleGame
{
  class Game : SuperGame
  {


// Updates the change in x and y position based on what string is recieved
    public new static void UpdatePosition(string keyPressed, out int xChange, out int yChange){
      switch (keyPressed)
      {
        case "DownArrow":
          yChange = 1;
          xChange = 0;
          break;
        case "UpArrow":
          yChange = -1;
          xChange = 0;
          break;
        case "LeftArrow":
          xChange = -1;
          yChange = 0;
          break;
        case "RightArrow":
          xChange = 1;
          yChange = 0;
          break;
        default:
          xChange = 0;
          yChange = 0;
          break;
      }
    }

    //Changes the appearence the cursor depending on what string is recieved

    public new static char UpdateCursor(string keyPressed){
      switch (keyPressed){
        case "LeftArrow":
          return '<';
        case "RightArrow":
          return '>';
        case "UpArrow":
          return '^';
        case "DownArrow":
          return 'v';
        default:
          return ' ';
      }
    }


    //Makes sure that if cursor goes out of bounds, it goes to other side 

    public new static int KeepInBounds(int coord, int maxValue){
      if (coord >= maxValue){
        return  0;
      } else if (coord < 0){
        return maxValue -1;
      } else {
        return coord;
      }   
    }
    
    //Checks to see if position of cursor and fruit are the same
    public new static bool DidScore(int charx, int chary, int fruitx, int fruity){
      if ((charx == fruitx) && (chary == fruity)){
        return true;
      } else {
        return false;
      }
    }

    
    }
    
  }
