//This is the size of the board
var amountOfColumnsInGrid = 15;
var amountOfRowsInGrid = 15;

//This is the max amount of crosswords we have in the back
var numberOfBoards = 5;

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
        $('#acrossClues').append(html);
		inputNumber++
      }

      //For every row we want to add a break line
      html += '<br>';
    }
    $('#CrosswordPuzzle').html(html);
    addJSONDataToBoard(boardNumber);
    addCluesToBoard(boardNumber);
}





	//checking if tempJSONStrings has value
function isEmpty(tempJSONStrings)
{
	return (!tempJSONStrings || 0 === tempJSONStrings.length);
}

//This function will take the JSON String and add the data to the field
function addJSONDataToBoard(boardNumber)
{
  var numberLabels = new Set();

  for(var j = 0; j < tempJSONStrings.length; j++)
  {
    //Parse the JSON Data with all of the data of this word
    var JSONData = tempJSONStrings[j];
    //Get the cell that this word starts on based on the x and y it starts of
    var cellToWriteData = turnXAndYToInputId(JSONData.x, JSONData.y);
    var placementOfWord = JSONData.direction;
    var hintNumber = JSONData.number;
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
      if(i == 0 && !numberLabels.has(hintNumber))
      {
          var label;
          if(hintNumber < 10)
          {
            // Add the hint's number label to the crossword
            label = "<span class=\"numLabel\">" + hintNumber + "</span>"
          }

          else
          {
              label = "<span class=\"numLabelTwoDigit\">" + hintNumber + "</span>"
          }
        $('#'+cellToWriteData).after(label);

        // Keep track which numbers have been added so far so we don't add them twice
        numberLabels.add(hintNumber);
      }

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
    var html = '';
    $('#acrossClues').html(html);
    $('#downClues').html(html);

    for(var i = 0; i < tempJSONStrings.length; i++) {
        var JSONData = tempJSONStrings[i];
        var direction = JSONData.direction;

        if(direction === "Across")
        {
            html = '<p class="A ' + JSONData.number +'">' + JSONData.number + ". " + JSONData.hint + '</p>';
            $('#acrossClues').append(html);
        }

        else if(direction === "Down")
        {
            html = '<p class="D ' + JSONData.number +'">' + JSONData.number + ". " + JSONData.hint + '</p>';
            $('#downClues').append(html);
        }

        else
        {
           console.log("Error adding the clue for" + JSONData.answer);
        }
    }

}



/*
 * SAVE AND LOAD FUNCIONALITY
 *
 *
 *
 *
 */
function saveTheBoard(boardNumber) {
    var charArray = convertTheBoardToCharArray();
    saveCharArrayToLocalStorage(boardNumber, charArray);
}

function saveCharArrayToLocalStorage(boardNumber, charArray) {
    var string = charArray.join("");
    localStorage.setItem(boardNumber,string);
}

function convertTheBoardToCharArray()
{
    var numberOfCells = amountOfRowsInGrid * amountOfColumnsInGrid;
    var charArray = new Array();

    // Go through each cell and read what is writen in the text box and save it
    // as a charArray
    for(var i = 0 ; i < numberOfCells ; i++)
    {
        var inputByPlayer = $('#'+i).val().toUpperCase();
        var writable = !document.getElementById(i).readOnly;

        // if it is writeableBlock and if there is a character in the cell then
        if(writable && inputByPlayer !== "")
        {
            charArray[i] = inputByPlayer;
        }

        else
        {
            charArray[i] = '\0';
        }
    }

    return charArray;
}

function loadTheBoard(boardNumber) {

    // Error check: if theres are no saved boards in local storage just return -1
    if(localStorage.getItem(boardNumber) === null){
        return -1;
    }

    var charArray = loadCharArrayFromLocalStorage(boardNumber);
    loadCharArrayToBoard(charArray);

    return boardNumber;
}

function loadCharArrayFromLocalStorage(boardNumber) {
    var string = localStorage.getItem(boardNumber);
    return string.split('');
}

function loadCharArrayToBoard(charArray) {
    var numberOfCells = amountOfRowsInGrid * amountOfColumnsInGrid;

    // Go through each cell and write the index of charArray into the block
    for(var i = 0 ; i < numberOfCells ; i++)
    {
        var inputByPlayer = $('#'+i).val().toUpperCase();
        var writable = !document.getElementById(i).readOnly;

        // if it is writeableBlock and if there is a character there write to the cell
        if(writable && charArray[i] !== '\0')
        {
            $("#"+i).val(charArray[i]);
        }
    }
}

//This function will read the crossword puzzle as a String
function readFile()
{
  //var boardNumber = Math.floor(Math.random() * numberOfBoards);
  var boardNumber = 1;
  console.log(boardNumber);
  $.ajax({
    //url: "https://raw.githubusercontent.com/jin0s/Crossing-Words/master/Sprint%203/crosswords/crossword"+boardNumber+".txt",
    url: "https://raw.githubusercontent.com/jin0s/Crossing-Words/master/Sprint%203/crosswords/test_crossword.txt",
    async: false,
    success: function (data){
          var JSONObject = JSON.parse(data);
          tempJSONStrings = JSONObject.clues;
          newBoard();
        }
  });
}
