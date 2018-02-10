# ConnectXor
## Author

## Points
350
## Category
Pwn
## Description
This challenge is a simple connect 4 game.  It has the ability to support a few
players and one observer per player.  The goal of the challenge is to force
teams to explore the state-space of the program.

Teams must discern that after a observing a tie game, an observer can replay
the game in its entirety.  Theobserver can choose to go back any number of
moves, or to any CPU timer state in the game.  This timer value can overflow if
the observer stays on the prompt asking for a replay for too long.

Once that timer value overflows, this causes a condition where a loop variable
is never properly set, and remains as -1.  This variable is then used as an
index to access previous moves.  Given the arrangement of the game_t type, the
previous moves are stored directly adjacent to the player's name, which the
player can directly control.

Finally, when the game is being replayed, the board is printed for each move
made.  If a board state is determined to be invalid, the board is simply
"printed" to the screen.  This is done incorrectly, by passing the board as a
char * directly to an fprintf function call.

Teams can then use the shellcode they placed in the name field to overwrite the
stack and get code execution.  They can use this codex to find the flag which
is stored at /flag.
## Flag
`flag{st@t3ful_und3rfl0w}`
## Solution
[solver.py](solver.py)
## Setup
Given you have a basic linux system with Docker, you should be able to build an
image simply by running build.sh.
Similarly, run.sh with run the docker image with a restart mechanism.
This challenge should be run with auto-restart (as done in run.sh) as teams can
crash the service with certain inputs.