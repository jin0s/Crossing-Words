# POOPs

## Vision Statement [7 points]
* Create a crossword puzzle generator for anyone who wants to kill time, or fancy crossword puzzle enthusiast
* Like words with friends but without the friend because its solo

## User Stories [6 points ]
* As a developer I want documentation so that I can construct a properly planned project -Jin
* As a developer I want units test so that I can do regression testing later - Jorge
* As a developer I want easy form of communication and data sharing so I can collaborate with my team - Tony
* As a developer I want a clean UI so that my players can play the crossword puzzle game with easy of use. - Tony
* As a player I want to have a challenging and new crossword crossword puzzle so that I never get the same puzzle too often -Jin
* As a player I want a list of hints so that I can guess the correct word - Jorge
* As a player I want the puzzle to load within 5 seconds - Tony
* As a player I want to be able to access the crossword anywhere so that I can play - Jin
* As a player I want to be able to enter my answer to a crossword puzzle so that I can play the game. - Jorge
* As a player I want to have pointed out my mistakes so that I know which words I have gotten wrong - Jorge
* As a player I want a percentage of right answers so that I can show my friends and compare scores - Jorge
* As a player I want to see the correct and completed board after submitting so that I can learn new words - Jin
* As a player I want to save my progress so that I can continue playing later - Jin
* As a player I want to undo my wrong answer so that I can try to enter the right asnwer. - Tony
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
* As a developer I want documentation so that I can construct a properly planned project -Jin
* There must be vision statements, user stories, requirements, product backlogs, sprint backlogs, burndown chart
* There must be a common repository that include everyone's notes and research
* Generate the crossword puzzle from a database of thousands of words and hint pairs
* There must be a server that will host the crossword
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
|As a developer I want documentation so that I can construct a properly planned project |8|HIGH|We have a Vision Statement, User Stories, Requirements, Product Backlogs, Sprint Backlogs, Burndown Chart|DONE|
|As a developer I want units test so that I can do regression testing later |10|HIGH|-----|-----|
|As a developer I want easy form of communication and data sharing so I can collaborate with my team |2|MID|-----|-----|
|As a developer I want a clean UI so that my players can play the crossword puzzle game with easy of use. |8|MID|-----|-----|
|As a player I want to have a challenging and new crossword crossword puzzle so that I never get the same puzzle too often |20|HIGH|-----|-----|
|As a player I want a list of hints so that I can guess the correct word |5|HIGH|-----|-----|
|As a player I want the puzzle to load within 5 seconds |9|LOW|-----|-----|
|As a player I want to be able to access the crossword so that I can play |8|HIGH|-----|-----|
|As a player I want to be able to enter my answer to a crossword puzzle so that I can play the game. |4|HIGH|-----|-----|
|As a player I want to have pointed out my mistakes so that I know which words I have gotten wrong |6|MID|-----|-----|
|As a player I want a percentage of right answers so that I can show my friends and compare scores |6|LOW|-----|-----|
|As a player I want to see the correct and completed board after submitting so that I can learn new words |3|LOW|-----|-----|
|As a player I want to save my progress so that I can continue playing later |4|LOW|-----|-----|
|As a player I want to undo my wrong answer so that I can try to enter the right asnwer. |3|MID|-----|-----|
|As a player I want to be able to rate the crossword puzzle level to show my enjoyment. |2|LOW|-----|-----|

## Sprint Backlog [5 points]

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
