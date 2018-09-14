Welcome to DEATH!

DEATH is a variant to Conways game of LIFE.

Every LIFE game can be described by two sets of numbers:

*   numbers of neighbors for a item to survive
*   numbers of neighbors for a item to be born

What I added is mulitiplayer support and a third number:

*   numbers of friendly neighbors for a friendly item to survive
*   numbers of friendly neighbors for a friendly item to be born
*   numbers of friendly neighbors for a foe item to be killed

the players take turns.

# controls

arrow-keys - move cursor
space      - toggle field value
               after that it is the next players' turn
backspace  - clear field value
return     - perform a full step (one for every player)
tab        - perform a single step (only for the active player)
               after that it is the next players' turn
h          - display a help screen
escape     - quit

# how to start the game?

run DeathCliMenu.py from a terminal

# dependencies

python (tested with 2.6)
optparse and curses should be installed with python

Latest code can be found on <https://github.com/xi/DEATH>.
