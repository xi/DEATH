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

# how to start the game?

    python -m DEATH

# controls

-   arrow-keys: move cursor
-   space: toggle field value; after that it is the next player's turn
-   return: perform a single step (only for the active player);
    after that it is the next player's turn
-   "q": quit
