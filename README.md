# POOPs

## Vision Statement
Crossing Words is a crossword puzzle game that will generate a new crossword from a dataset of know word:hint pairs. It is needed by anyone who wants to escape from their stressful thoughts and engage in extending their vocabulary, problem solving, and good old wasting time. Unlike the New York Times newspaper version, where you need a subscription and a physical copy of the paper, the game will be entirely hosted on a server and will be accessible via Internet. Our product is reactive by informing the player of correct and incorrect answers. It is also shareable by allowing players to share their board with other players. Lastly, it is intuitively easy to use. The game itself it free of charge to play, but the target customer is anyone who wants to advertise. We believe that Crossing Words will be a bit hit since it is available to the masses and shareable. The site itself is a great investment for anyone wanting to generate advertisement revenue.

## Product Backlog
* https://docs.google.com/spreadsheets/d/1dMm4ts908kk_r-WLcMa7490zs8nHdqAeZO0t8PZn6iw/edit#gid=0


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


## Sprint Backlog
* https://docs.google.com/spreadsheets/d/1ho4MHLfHYYG90qOGLvA9yksRg7iM44FcjVvcUUN4qdw/edit#gid=0

## Burndown Chart
* https://docs.google.com/spreadsheets/d/1O6-5PgWYNVYqPI3yn2iEwXZJWgYm1r5lbdo5Slb988c/edit#gid=0

## Design Documents
* The website is hosted on a Raspberry Pi on Jin's Home Network. In order to gain SSH access to the server, the developer's need to send Jin a public RSA key.
* After gaining access, developer's will be able to SSH using the command 'ssh 72.188.113.6 -l poops -p 8798'
* The link to the site for now is: http://poopsCrossword.ml
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
