### Game Board
For the game board, a list of 7 sub-lists of 6 strings with a
single whitespace character each.

### Display function
Add the string in column Y at index X to a single string for row X.

Print the entire row. Repeat this for all rows, in reverse order.

Print a string labeling the columns 1 - 7.

### Move function
Ask for player input: A number in 1 - 7 that represents a column.

Validate the input. Is it in range? Is that column not full?

If the move is valid, add player's piece to the right index.
Update moves played.

### Game-Over function
Check for win condition: Consecutive line of 4 of the same pieces.

Check for tie condition: Full board.

### Game Loop
Ask for player names. Assign to player X and player O

Welcome message.

Current player = player x.

Create board.

Show board.

Ask player X to make a move.

Check game-state.

If a game-over condition is met, break the loop and print
the relevant message.

If not, switch current player and ask for another move.