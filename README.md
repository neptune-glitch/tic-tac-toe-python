     Tic Tac Toe – Python (Player vs Computer)



A simple yet fun Tic Tac Toe game built in Python, where the player competes against the computer .

The game runs in the terminal and supports real-time input, win-checking, computer moves, and draw detection.



     Features


✅ Player vs Computer gameplay.

✅ Real-time board update.

✅ Automatic win detection.

✅ Computer blocks or makes smart moves.

✅ Fully command-line based.

✅ Clean and readable code.

✅ Replay-friendly structure.




     How to Play



1.The board is shown as a 3×3 grid.

2.You choose:

   Row: row1, row2, or row3
   Position: 0, 1, or 2
   Your symbol is X.

3.Computer will respond with symbol 0 (zero).

4.Game ends when:

  Player wins
  Computer wins
  Draw (board full)



   Screenshot of the game 

<img width="980" height="900" alt="image" src="https://github.com/user-attachments/assets/c68aff1d-f060-45a6-9e4b-6ca0635c6a4d" />


    Game Logic

✔ Player Move

The player selects a row and a position. The board updates instantly.

✔ Computer Move

The computer checks:
Can it win? → plays winning move
Does it need to block the player? → plays blocking move
Else → places at the first empty spot

✔ Win Check

The game checks:
All 3 rows
All 3 columns
Both diagonals


    File Structure

tic_tac_toe.py      → Main game file


README.md           → Project documentation


    Run the Game

Make sure Python is installed.

    Requirements

No external libraries needed — only Python 3.


   Future Improvements 

1. Add replay option inside game
 
2. Add AI difficulty levels
 
3. Add GUI using Tkinter or Pygame
 
 4.Add score system



