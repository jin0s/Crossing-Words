//This is the size of the board
var amountOfColumnsInGrid = 15;
var amountOfRowsInGrid = 15;

//THIS IS TEMP JUST FOR TESTING REASONS
var tempJSONString = '{ "direction":"Down", "number":22, "x":3, "y":9, "answer":"NIGHT", "hint":"Dusk to dawn" }';

//This function will draw the crossword
function drawCrossword()
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
        html += '<input class = "writeableBlock" id = "'+inputNumber+'">';
        inputNumber++;
      }
      //For every row we want to add a break line
      html += '<br>';
    }
    $('#CrosswordPuzzle').html(html);
    addJSONDataToBoard();
}



//This function will take an x and y coordinate and find out what the id of that input is
function turnXAndYToInputId(x,y)
{
  //Have a variable to hold the id that is going to be associated with this place
  var id = 0;
  //For every row that means that we must count each cell in that row
  for(i = 0; i < x; i++)
  {
    id = id + amountOfRowsInGrid;
  }
  //Have to add all the cells that come before in this row
  id = id + y;
  //return the id of this input
  return id;
}

//This function will take the JSON String and add the data to the field
function addJSONDataToBoard()
{
  //Parse the JSON Data with all of the data of this word
  var JSONData = JSON.parse(tempJSONString);
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
