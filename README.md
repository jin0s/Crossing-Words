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
* As a player I want to be able to rate the crossword puzzle ;evel to show my enjoyment. - Tony 



## Requirements [6 point]
* Must accessible via web browser
* Generate unique crosswords every time
* Product Backlog [5 points]
* Set up node.js server to host the crossword puzzle
* Draft up UI design
* Have list of API calls

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
