//This is the size of the board
var amountOfColumnsInGrid = 15;
var amountOfRowsInGrid = 15;



//THIS IS TEMP JUST FOR TESTING REASONS
 var tempJSONStrings = ['{ "direction":"Down", "number":22, "x":3, "y":9, "answer":"NIGHT", "hint":"Dusk to dawn" }',
                        '{ "direction":"Across", "number":6, "x":1, "y":1, "answer":"REPEATS", "hint":"Shows youve seen" }',
                        '{ "direction":"Across", "number":7, "x":9, "y":1, "answer":"NINES", "hint":"Eights arent enough" }',
                        '{ "direction":"Across", "number":9, "x":0, "y":3, "answer":"DIAL", "hint":"Dont touch that __" }',
                        '{ "direction":"Across", "number":10, "x":5, "y":3, "answer":"ASTRONOMER", "hint":"Starstruck scientist" }',
                        '{ "direction":"Across", "number":11, "x":0, "y":5, "answer":"WEIGHING", "hint":"Measuring heaviness" }',
                        '{ "direction":"Across", "number":13, "x":9, "y":5, "answer":"COUSIN", "hint":"Maybe you can marry" }',
                        '{ "direction":"Across", "number":15, "x":0, "y":7, "answer":"JAZZ", "hint":"American music" }',
                        '{ "direction":"Across", "number":17, "x":5, "y":7, "answer":"BOATS", "hint":"Marina sights" }',
                        '{ "direction":"Across", "number":18, "x":11, "y":7, "answer":"EASE", "hint":"Let out" }',
                        '{ "direction":"Across", "number":19, "x":0, "y":9, "answer":"PURSES", "hint":"Sums of money" }',
                        '{ "direction":"Across", "number":20, "x":7, "y":9, "answer":"POSTPONE", "hint":"Give a rain check" }',
                        '{ "direction":"Across", "number":23, "x":0, "y":11, "answer":"RIDICULOUS", "hint":"Cockamamy" }',
                        '{ "direction":"Across", "number":26, "x":11, "y":11, "answer":"CAGE", "hint":"Hamsters home" }',
                        '{ "direction":"Across", "number":27, "x":1, "y":13, "answer":"GHOST", "hint":"Father & son, theres a crowd" }',
                        '{ "direction":"Across", "number":28, "x":7, "y":13, "answer":"ELEMENT", "hint":"Substance like no other" }',
                        '{ "direction":"Down", "number":1, "x":3, "y":0, "answer":"APOLOGIZES", "hint":"Makes amends" }',
                        '{ "direction":"Down", "number":2, "x":5, "y":0, "answer":"HAWAII", "hint":"Baracks home " }',
                        '{ "direction":"Down", "number":3, "x":7, "y":0, "answer":"ISNT", "hint":"__ it romantic?" }',
                        '{ "direction":"Down", "number":4, "x":9, "y":0, "answer":"ENFORCES", "hint":"Keeps lawfull" }',
                        '{ "direction":"Down", "number":5, "x":11, "y":0, "answer":"ONTO", "hint":"Im __ you!" }',
                        '{ "direction":"Down", "number":6, "x":1, "y":1, "answer":"RAISE", "hint":"Bring up" }',
                        '{ "direction":"Down", "number":8, "x":13, "y":1, "answer":"SPECIES", "hint":"Variety" }',
                        '{ "direction":"Down", "number":12, "x":7, "y":5, "answer":"GRASP", "hint":"Hold" }',
                        '{ "direction":"Down", "number":14, "x":11, "y":5, "answer":"UNEXPECTED", "hint":"Abrupt" }',
                        '{ "direction":"Down", "number":16, "x":1, "y":7, "answer":"AMUSING", "hint":"Gladdening" }',
                        '{ "direction":"Down", "number":17, "x":5, "y":7, "answer":"BISCUITS", "hint":"Go with gravy" }',
                        '{ "direction":"Down", "number":21, "x":9, "y":9, "answer":"SISTER", "hint":"Nun" }',
                        '{ "direction":"Down", "number":22, "x":13, "y":9, "answer":"NIGHT", "hint":"Dusk to dawn" }',
                        '{ "direction":"Down", "number":24, "x":3, "y":11, "answer":"IRON", "hint":"Pumping __" }',
                        '{ "direction":"Down", "number":25, "x":7, "y":11, "answer":"OVER", "hint":"Game __" }' ];

//Taking in Json Files to be read locally
	//let tempJSONStrings = require('data.json');

	var numberOfBoards = tempJSONStrings.length - 1;






//This function will draw the crossword
function drawCrossword(boardNumber = 5)
{
  var html = '';
  //This will be used to number each input from 0...254
  var inputNumber = 0;
    //Loop through the amnount of amount of rows
    for (var x = 0; x < amountOfRowsInGrid; x++)
    {
      //For every row loop through the amount of columns
      for(var y = 0; y < amountOfColumnsInGrid; y++)
      {
        //For every column write a block to the crossword
        html += '<input class = "writeableBlock" id = "'+inputNumber+'" onKeyUp = "makeEachCellOneCharacter('+inputNumber+')">';
        inputNumber++;
      }
      //For every row we want to add a break line
      html += '<br>';
    }
    $('#CrosswordPuzzle').html(html);
    addJSONDataToBoard(boardNumber);
    addCluesToBoard(boardNumber);
}

//This function will take the JSON String and add the data to the field
function addJSONDataToBoard(boardNumber)
{
  for(var j = 0; j < tempJSONStrings.length; j++)
  {
    console.log(i);
    //Parse the JSON Data with all of the data of this word
    var JSONData = JSON.parse(tempJSONStrings[j]);
    //Get the cell that this word starts on based on the x and y it starts of
    var cellToWriteData = turnXAndYToInputId(JSONData.x, JSONData.y);
    var placementOfWord = JSONData.direction;
    var incrementation = 0;
    //If the word is across we will add data increasing by columns
    if(placementOfWord === "Across")
    {
      incrementation = 1;
    }
    //If the word is down we will add data increasing by rows
    if(placementOfWord === "Down")
    {
      incrementation = amountOfColumnsInGrid;
    }
    //For every letter in the word we add a data type with the letter that is supposed to be there
    for(var i = 0; i < JSONData.answer.length; i++)
    {
      $('#'+cellToWriteData).attr('data-letter', JSONData.answer.charAt(i));
      cellToWriteData = cellToWriteData + incrementation;
    }
  }
  grayOutEmptyCells();
}

//This function will make all of the cells that dont have a word associated dark gray and untypable
function grayOutEmptyCells()
{
  //Loop through each of cells
  for(var x = 0; x < amountOfRowsInGrid; x++)
  {
    for(var y = 0; y < amountOfColumnsInGrid; y++)
    {
        var cellID = turnXAndYToInputId(x,y);
        //If this cell does not have a character associated with interval
        if($('#'+cellID).attr('data-letter') === undefined)
        {
          //Make cell untypeable
          $('#'+cellID).prop("readonly", true);
          //Black out the cells
          $('#'+cellID).css("background-color", "Black");
        }

    }
  }

}


//This function will take an x and y coordinate and find out what the id of that input is
function turnXAndYToInputId(x,y)
{
  //Have a variable to hold the id that is going to be associated with this place
  var id = 0;
  //For every row that means that we must count each cell in that row
  for(i = 0; i < y; i++)
  {
    id = id + amountOfRowsInGrid;
  }
  //Have to add all the cells that come before in this row
  id = id + x;
  //return the id of this input
  return id;
}

//This function will test the turn x and y into a single number
function testTurnXandYToInputId()
{
   var correctID = 0;
   var functionWorks = true;
   for(var y = 0; y < amountOfRowsInGrid; y++)
   {
     for(var x = 0; x < amountOfColumnsInGrid; x++)
     {
       var answer = turnXAndYToInputId(x,y);
       if(correctID !== answer)
       {
         functionWorks = false;
       }
       correctID++;
     }
   }
   console.log(functionWorks);
}

//This function makes sure that each block only has letter
function makeEachCellOneCharacter(cellID)
{
  //Get the word in the cell
  var wordInCell = $('#'+cellID).val();
  //If the word is longer than 1
  if(wordInCell.length > 1)
  {
    //Replace the value with the last character in the string
    $('#'+cellID).val(wordInCell.substr(-1));
  }
}

//This is the function that is going to check if the board is correct
function checkBoard()
{
  //We want to traverse the board
  var totalAmountOfCells = amountOfRowsInGrid * amountOfColumnsInGrid;
  for(var i = 0; i < totalAmountOfCells; i++)
  {
    //What did the player enter
    var inputByPlayer = $('#'+i).val().toUpperCase();
    //What letter did we have to enter here
    var correctLetter = $('#'+i).attr('data-letter');
    if(correctLetter !== undefined)
    {
      correctLetter.toUpperCase();
    }
    //If the word is correct we want to make it green
    if(inputByPlayer === correctLetter)
    {
      $('#'+i).css("background-color", "green");
    }
    //If the word is incorrect we want to make it red
    if(inputByPlayer !== correctLetter && correctLetter !== undefined)
    {
      $('#'+i).css("background-color", "red");
    }
  }

}

/**
 * Returns a random integer between min (inclusive) and max (inclusive).
 * The value is no lower than min (or the next integer greater than min
 * if min isn't an integer) and no greater than max (or the next integer
 * lower than max if max isn't an integer).
 * Using Math.round() will give you a non-uniform distribution!
 */
function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

// Function that will pull up a new random board
function newBoard()
{
    var randomBoardID = getRandomInt(0, numberOfBoards);
    drawCrossword(randomBoardID);
}

function addCluesToBoard(boardNumber)
{
    var JSONData = JSON.parse(tempJSONStrings[boardNumber]);
    var direction = JSONData.direction;
    var html = '';
    $('#acrossClues').html(html);
    $('#downClues').html(html);

    if(direction === "Across")
    {
        html = '<p class="A' + JSONData.number +'">' + JSONData.number + ". " + JSONData.hint + '</p>';
        $('#acrossClues').html(html);
    }

    else if(direction === "Down")
    {
        html = '<p class="D' + JSONData.number +'">' + JSONData.number + ". " + JSONData.hint + '</p>';
        $('#downClues').html(html);
    }

    else
    {
       console.log("Error adding the clue for" + JSONData.answer);
    }
}


//This function will read the crossword puzzle as a String
function readFile()
{
  const fs = require('fs')

  fs.readFile('../crosswords/crossword0.txt', (err, data) => {
      if (err) throw err;

      console.log(data.toString());
  })
}
