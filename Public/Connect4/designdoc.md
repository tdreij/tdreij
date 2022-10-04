# Connect 4 Clone

## 1: Represent the game board as a 2D list.
> A standard board is 7 columns x 6 rows.
>
> To more easily add a played piece to the lowest open slot in
> a column, the columns will be the sub-lists.

## 2: Display the board to the players.
> The main list is effectively sideways, and we want to print it
> row by row for the players, as you would see a real board.
> 
> Also, since the columns are filled from the bottom up, as if the 
> pieces were dropped by gravity, we'll print the rows in reversed 
> order.

## 3: Drop a piece.
> The main gameplay of Connect 4 consists of 2 players taking turns
> to drop a piece in a column. The piece drops to the lowest empty slot.
> So we need a function to take care of this process

## 4: Move validation.
> If a player tries to drop a piece outside the board, i.e. in a
> non-existent column, or into a column where are slots are filled,
> the move should not be executed. Probably give them a polite 
> error message and try again.

## 5: Game over!
> The game should end under two conditions:
>
> 1: The board is full, every slot contains a piece, no more legal
> moves available. It's a tie!
> 
> 2: A dropped piece creates an uninterrupted line of 4 of their pieces,
> which can be horizontal, vertical, or diagonal. That player wins!

## 6: Playing a game.
> First, start the game by asking for the players' names, assigning
> them both one of the pieces (X or O), and printing a welcome message.
> 
> Create an empty board, a turn counter at 0, and set the current player
> to 'X'
> 
> Show the empty board.
> 
> Ask the current player to pick a column. Check if that's a legal move.
> If the move is legal, add the piece.
> Then, check the game-state for ties or wins.
> If the win condition has not been met and the board is not full, 
> play another turn.
> Else print a game-over message and exit the loop.