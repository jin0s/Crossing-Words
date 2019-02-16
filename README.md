# POOPs

## Vision Statement [7 points]
* Create a crossword puzzle generator for anyone who wants to kill time, or fancy crossword puzzle enthusiast
* Like words with friends but without the friend because its solo

## User Stories [6 points ]
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


## Requirements [6 point]
* Must accessible via web browser
* Generate unique crosswords every time
* Product Backlog [5 points]
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

## Product Backlog [5 points]

| User Story | Estimate | Priority | Validation Requirement | Status |
|------------|--------|----------|---------------------|--------|
|As a developer I want documentation so that I can construct a properly planned project |8|HIGH|We have a Vision Statement, User Stories, Requirements, Product Backlogs, Sprint Backlogs, Burndown Chart |DONE|
|As a developer I want units test so that I can do regression testing later |10|HIGH|For every function we should have either a manual or automatic test associated with it |Not Started|
|As a developer I want easy form of communication and data sharing so I can collaborate with my team |2|MID|As a team, Define what tools to use for text-based and voice-based communcation. Define what tools to use for version control. Define what tools to use for file sharing..|Done|
|As a developer I want a clean UI so that my players can play the crossword puzzle game with easy of use. |8|MID|Developers should have a mockup design to use as a draft |Not Started|
|As a player I want to have a challenging and new crossword puzzle so that I never get the same puzzle too often |20|HIGH| Generate the crossword puzzle from a database of thousands of words and hint pairs, when calling the python backend API to generated the puzzle, it should return plain text file that has the 2-d array. |In Progress|
|As a player I want a list of hints so that I can guess the correct word |5|HIGH|There should be a display of hints to the player on the website. The hints should correspond with the crossword words |Not Started|
|As a player I want the puzzle to load within 5 seconds |9|LOW|Create a dedicated test enviornment for load testing to determine the load time.|Not Started|
|As a player I want to be able to access the crossword so that I can play |8|HIGH| The crossword must be accessible via web-browser and the Internet. There must be a server that will host the crossword. Developers must have access to the server in order to restart and deploy the game. The server must be up 95% of the time and must be accessible during the demonstration. |Done|
|As a player I want to be able to enter my answer to a crossword puzzle so that I can play the game. |4|HIGH|There should be blocks for players to enter letters. |Not Started|
|As a player I want to have pointed out my mistakes so that I know which words I have gotten wrong |6|MID|Incorrect words should show in red for the players to know which ones are wrong. |Not Started|
|As a player I want a percentage of right answers so that I can show my friends and compare scores |6|LOW|Everytime the player finish a game an stdout will display with correct/total.|Not Started|
|As a player I want to see the completed board/correct answers after submitting so that I can learn new words |3|LOW| Everytime the player checks their crossword there should be an amount of percent correct/ total. When the user decides to give up, there will be a button to show all of the solutions |Not Started|
|As a player I want to save my progress so that I can continue playing later |4|LOW| If the web-browser gets closed, or the user leave the site, The game should present the option to either start a new game or continue from the previous game |Not Started|
|As a player I want to undo my wrong answer so that I can try to enter the right answer. |3|MID|Everytime the player checkes their crossword there should be an option to backspace their current answer, so they can type in another answer.|Not Started|
|As a player I want to be able to rate the crossword puzzle level to show my enjoyment. |2|LOW|When the player has finish a pop up alert will display with an option to rate the game|Not Started|

## Sprint Backlog [5 points]
* https://docs.google.com/spreadsheets/d/1ho4MHLfHYYG90qOGLvA9yksRg7iM44FcjVvcUUN4qdw/edit#gid=0

## Burndown Chart [2 points]

## Design Documents [3 points]
* The website is hosted on a Raspberry Pi on Jin's Home Network. In order to gain SSH access to the server, the developer's need to send Jin a public RSA key.
* After gaining access, developer's will be able to SSH using the command 'ssh 72.188.113.6 -l poops -p 8798'
* The link to the site for now is: http://72.188.113.6:8000/
* The server is running the following services:
```
poops@raspberrypi:~/Crossing-Words $ node --version
v10.15.1
poops@raspberrypi:~/Crossing-Words $ npm --version
6.4.1
```

## Code [3 points]

## Tests [3 point]

## Demonstration [10 point]
