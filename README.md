# POOPs

## Vision Statement
Crossing Words is a crossword puzzle game that will generate a new crossword from a dataset of known word:hint pairs. It is needed by anyone who wants to escape from their stressful thoughts and engage in extending their vocabulary, problem solving, and good old wasting time. Unlike the New York Times newspaper version, where you need a subscription and a physical copy of the paper, the game will be entirely hosted on a server and will be accessible via Internet. Our product is reactive by informing the player of correct and incorrect answers. It is also shareable by allowing players to share their board with other players. Lastly, it is intuitively easy to use. The game itself it free of charge to play, but the target customer is anyone who wants to advertise. We believe that Crossing Words will be a big hit since it is available to the masses and shareable. The site itself is a great investment for anyone wanting to generate advertisement revenue.

## Product Backlog
* https://docs.google.com/spreadsheets/d/1dMm4ts908kk_r-WLcMa7490zs8nHdqAeZO0t8PZn6iw/edit#gid=0
* Requirements is a different tab in the Product Backlog sheet.

## Sprint Backlog
* https://docs.google.com/spreadsheets/d/1ho4MHLfHYYG90qOGLvA9yksRg7iM44FcjVvcUUN4qdw/edit#gid=0
* Sprint 1 and 2 are on different tabs in the Sprint Backlog sheet

## Burndown Chart
* https://docs.google.com/spreadsheets/d/1O6-5PgWYNVYqPI3yn2iEwXZJWgYm1r5lbdo5Slb988c/edit#gid=0
* Sprint 1 and 2 are on different tabs in the Burndown Chart

## Design Documents
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
* To start the server run:
    ```
    poops@raspberrypi:~/Crossing-Words $ node initialServerV2.js
    6.4.1
    ```
* System Design: https://drive.google.com/file/d/1jLuTz9hMdekggEr7gyuucSSUol9e0XDF/view?usp=sharing
![alt text](https://raw.githubusercontent.com/jin0s/Crossing-Words/master/Sprint%202/Design%20Documents/SystemDiagram.PNG)
* Python Crossword Generator UML Diagram: https://drive.google.com/file/d/1p0xWuy4sp1mSsMqn8s_j10ji1tLLKYL1/view?usp=sharing
* User Interface Draft
![alt text](https://raw.githubusercontent.com/jin0s/Crossing-Words/master/Sprint%202/Design%20Documents/UI_Diagram.jpg)

## Code
* Crossword generator source code is in 'src' and Webpages files are in the folder 'Sprint 2'
* Python Crossword Generator: https://github.com/jin0s/Crossing-Words/tree/master/Sprint%202/src
* Webpage Files: https://github.com/jin0s/Crossing-Words/tree/master/Sprint%202/

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
* Validation Tests for UI: https://docs.google.com/document/d/1L3gZZaVUrWObaSc9bOd9gkVLOY24MreumPI_OTGZgFM/edit?usp=sharing

## Demonstration

This is a link to our Youtube video showing our server up and running our code: https://www.youtube.com/watch?v=_oHg13jeh1g
