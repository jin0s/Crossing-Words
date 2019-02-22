//This is the size of the board
var amountOfColumnsInGrid = 15;
var amountOfRowsInGrid = 15;


//This function will draw the crossword
function drawCrossword()
{
  var html = '';
    //Loop through the amnount of amount of rows
    for (var i = 0; i < amountOfRowsInGrid; i++)
    {
      //For every row loop through the amount of columns
      for(var j = 0; j < amountOfColumnsInGrid; j++)
      {
        //For every column write a block to the crossword
        html += '<input class = "writeableBlock">';
      }
      //For every row we want to add a break line
      html += '<br>';
    }
    $('#CrosswordPuzzle').html(html);
}
