# POOPs

## Vision Statement
Crossing Words is a crossword puzzle game that will generate a new crossword from a dataset of know word:hint pairs. It is needed by anyone who wants to escape from their stressful thoughts and engage in extending their vocabulary, problem solving, and good old wasting time. Unlike the New York Times newspaper version, where you need a subscription and a physical copy of the paper, the game will be entirely hosted on a server and will be accessible via Internet. Our product is reactive by informing the player of correct and incorrect answers. It is also shareable by allowing players to share their board with other players. Lastly, it is intuitively easy to use. The game itself it free of charge to play, but the target customer is anyone who wants to advertise. We believe that Crossing Words will be a bit hit since it is available to the masses and shareable. Te site itself is a great investment for anyone wanting to generate advertisement revenue.

## User Stories
* As a developer I want documentation so that I can construct a properly planned project -Jin
* As a developer I want units test so that I can do regression testing later - Jorge
* As a developer I want easy form of communication and data sharing so I can collaborate with my team - Tony
* As a developer I want a clean UI so that my players can play the crossword puzzle game with easy of use. - Tony
* As a player I want to have a challenging and new crossword puzzle so that I never get the same puzzle too often -Jin
* As a player I want a list of hints so that I can guess the correct word - Jorge
* As a player I want the puzzle to load within 5 seconds - Tony
* As a player I want to be able to access the crossword anywhere so that I can play - Jin
* As a player I want to be able to enter my answer to a crossword puzzle so that I can play the game. - Jorge
* As a player I want to have pointed out my mistakes so that I know which words I have gotten wrong - Jorge
* As a player I want a percentage of right answers so that I can show my friends and compare scores - Jorge
* As a player I want to see the completed board/correct solutions after submitting so that I can learn new words - Jin
* As a player I want to save my progress so that I can continue playing later - Jin
* As a player I want to undo my wrong answer so that I can try to enter the right answers. - Tony
* As a player I want to be able to rate the crossword puzzle level to show my enjoyment. - Tony
* As a developer I want a fast, clean way to verify that a word is in the clue repository, so that puzzle validation is simple to accomplish. - Steven
* As a developer I want a clean way to export randomly generated crosswords into a consistent format to be used. - Steven
* As a developer I want a clear understanding of how I will be using object-oriented concepts to simplify the challenge of randomly generating crosswords -Steven
* As a player I want to have the crossword puzzles follow the same format as other common crosswords puzzles, such as the NYT daily crossword. - Steven
* As a player I want the crosswords to not be too similar to crosswords I have played before, with hints not often reused. - Steven
* As a player I want the structure of the crossword to vary, such that the board feels different everytime I play - Steven

## Requirements
* Must accessible via web browser
* Must Generate unique crosswords every time
* Crosswords must follow NYT Crossword guidelines:
  * All words must be 3 or more characters
  * The entire grid must be interconnected, i.e. not disjoint
  * Every square must be "checked": part of both a down and an across word
  * The (empty) grid must be rotationally symmetric: can be rotated 180 degrees and remain identical.
* The probability of any pair of randomly generated crosswords sharing a clue should be less than 50%
* The probability of any pair of randomly generated crosswords sharing similar structure (>50% match of black tiles) should be less than 10%
* Set up node.js server to host the crossword puzzle
* Draft up UI design
* Have list of API calls
* Must set up tests for most functions
* Must produce a list of hints
* Must show the list of hints to the User
* Hints must match the Words
* Must have a place to enter the answers
* Turn the hints red if the player has guessed incorrectly
* Must have a button to have the player test
* Must find out how many words the player has gotten correct
* Must show the percentage to the player
* There must be vision statements, user stories, requirements, product backlogs, sprint backlogs, burndown chart
* There must be a common repository that include everyone's notes and research
* Generate the crossword puzzle from a database of thousands of words and hint pairs
* The crossword must be accessible via web-browser and the Internet.
* Developers must have access to the server in order to restart and deploy the game
* The server must be up 95% of the time and must be accessible during the demonstration
* There must be a button to show the answer, but only be available after the player submits his answers
* After clicking the show answer the correct board will be displayed
* The correct board must be displayed until the player clicks new game
* There must be a button to save the game
* The game will not save by default
* When the player reloads the game he is presented with the option to either start a new game or continue
* If the player selects new game, a new board will be generated
* If the player selects continue, the game will load all of the previous entries

## Product Backlog
|ID| User Story | Estimate | Priority | Validation Requirement | Status |
|---|------------|--------|----------|---------------------|--------|
|01|As a developer I want documentation so that I can construct a properly planned project |8|HIGH|We have a Vision Statement, User Stories, Requirements, Product Backlogs, Sprint Backlogs, Burndown Chart |DONE|
|02|As a developer I want units test so that I can do regression testing later |10|HIGH|For every function we should have either a manual or automatic test associated with it |Not Started|
|03|As a developer I want easy form of communication and data sharing so I can collaborate with my team |2|MID|As a team, Define what tools to use for text-based and voice-based communication. Define what tools to use for version control. Define what tools to use for file sharing.|Done|
|04|As a developer I want a clean UI so that my players can play the crossword puzzle game with easy of use. |8|MID|Developers should have a mockup design to use as a draft |Not Started|
|05|As a player I want to have a challenging and new crossword puzzle so that I never get the same puzzle too often |20|HIGH| Generate the crossword puzzle from a database of thousands of words and hint pairs, when calling the python backend API to generated the puzzle, it should return plain text file that has the 2-d array. |In Progress|
|06|As a player I want a list of hints so that I can guess the correct word |5|HIGH|There should be a display of hints to the player on the website. The hints should correspond with the crossword words |Not Started|
|07|As a player I want the puzzle to load within 5 seconds |9|LOW|Create a dedicated test environment for load testing to determine the load time.|Not Started|
|08|As a player I want to be able to access the crossword so that I can play |8|HIGH| The crossword must be accessible via web-browser and the Internet. There must be a server that will host the crossword. Developers must have access to the server in order to restart and deploy the game. The server must be up 95% of the time and must be accessible during the demonstration. |Done|
|09|As a player I want to be able to enter my answer to a crossword puzzle so that I can play the game. |4|HIGH|There should be blocks for players to enter letters. |Not Started|
|10|As a player I want to have pointed out my mistakes so that I know which words I have gotten wrong |6|MID|Incorrect words should show in red for the players to know which ones are wrong. |Not Started|
|11|As a player I want a percentage of right answers so that I can show my friends and compare scores |6|LOW|Everytime the player finish a game an stdout will display with correct/total.|Not Started|
|12|As a player I want to see the completed board/correct answers after submitting so that I can learn new words |3|LOW| Everytime the player checks their crossword there should be an amount of percent correct/ total. When the user decides to give up, there will be a button to show all of the solutions |Not Started|
|13|As a player I want to save my progress so that I can continue playing later |4|LOW| If the web-browser gets closed, or the user leave the site, The game should present the option to either start a new game or continue from the previous game |Not Started|
|14|As a player I want to undo my wrong answer so that I can try to enter the right answer. |3|MID|Everytime the player checks their crossword there should be an option to backspace their current answer, so they can type in another answer.|Not Started|
|15|As a player I want to be able to rate the crossword puzzle level to show my enjoyment. |2|LOW|When the player finish a game a stdout display will give an option to rate the level.|Not Started|
|16|As a developer I want a fast, clean way to verify that a word is in the clue repository, so that puzzle validation is simple to accomplish|7|MID|Verification that a word is in the repository should take under 15ms|In Progress|
|17|As a developer I want a clean way to export randomly generated crosswords into a consistent format to be used.|3|HIGH|The Crossword generator should output its results to a txt file in an agreed upon format|In Progress|
|18|As a developer I want a clear understanding of how I will be using object-oriented concepts to simplify the challenge of randomly generating crosswords|3|HIGH|A complete UML diagram clearly showcasing the classes I will be using, how they interact, and what members and methods each of them possess|Done|
|19|As a player I want to have the crossword puzzles follow the same format as other common crosswords puzzles, such as the NYT daily crossword|7|HIGH|The crossword should follow NYT conventions, meaning no words under 3 characters, rotational symmetry, and a fully interconnected, checked board|Not Started|
|20|As a player I want the crosswords to not be too similar to crosswords I have played before, with hints not often reused.|4|LOW|The odds of two crosswords having an identical clue should be less than 50%|Not Started|
|21|As a player I want the structure of the crossword to vary, such that the board feels different everytime I play|6|LOW|The odds of two crosswords having more than a 50% match of black (empty) squares should be under 10%|Not Started|
## Sprint Backlog
* https://docs.google.com/spreadsheets/d/1ho4MHLfHYYG90qOGLvA9yksRg7iM44FcjVvcUUN4qdw/edit#gid=0

## Burndown Chart
* https://docs.google.com/spreadsheets/d/1O6-5PgWYNVYqPI3yn2iEwXZJWgYm1r5lbdo5Slb988c/edit#gid=0

## Design Documents
* The website is hosted on a Raspberry Pi on Jin's Home Network. In order to gain SSH access to the server, the developer's need to send Jin a public RSA key.
* After gaining access, developer's will be able to SSH using the command 'ssh 72.188.113.6 -l poops -p 8798'
* The link to the site for now is: http://poopsCrossword.ml (http://72.188.113.6:8000/)
* The server is running the following services:
    ```
    poops@raspberrypi:~/Crossing-Words $ node --version
    v10.15.1
    poops@raspberrypi:~/Crossing-Words $ npm --version
    6.4.1
    ```
* Mockup in the Sprint1 folder

## Code
* Source code is in the 'src' directory
* https://github.com/jin0s/Crossing-Words/tree/master/Sprint%201/src

## Tests
* Test code is in the 'test' directory
* https://github.com/jin0s/Crossing-Words/tree/master/Sprint%201/test
* To run pytest: Navigate the the Sprint 1 Folder and enter:
    ```
    jin@XPS15z:~/Documents/Crossing-Words$ cd Sprint\ 1/
    jin@XPS15z:~/Documents/Crossing-Words/Sprint 1$ python3 -m pytest -v
    ============================= test session starts ==============================
    platform linux -- Python 3.6.7, pytest-4.3.0, py-1.7.0, pluggy-0.8.1 -- /usr/bin/python3
    cachedir: .pytest_cache
    rootdir: /home/jin/Documents/Crossing-Words/Sprint 1, inifile:
    plugins: pylama-7.4.3
    collected 3 items                                                              

    test/test_crossword.py::test_init_Clue PASSED                            [ 33%]
    test/test_mathlib.py::test_calc_total PASSED                             [ 66%]
    test/test_mathlib.py::test_calc_multiply PASSED                          [100%]

    =========================== 3 passed in 0.13 seconds ===========================                     
    ```

## Demonstration

This is a link to our Youtube video showing our server up and running our code: https://www.youtube.com/watch?v=nxk0t8i9fRQ
