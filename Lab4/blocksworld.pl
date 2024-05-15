:- use_module(library(clpfd)).
:- style_check(-singleton).

% Constraints
table(0). % Table set to position 0 
block(X) :- X in 2 \/ 3 \/ 4 \/ 6. % Blocks
pyramid(X) :- X in 1 \/ 5. % Pyramids
orange(X) :- X in 1 \/ 4.
green(X) :- X in 2 \/ 5.
blue(X) :- X in 3 \/ 6.

% Actions
act(move(X,A,B),
    [clear(X), clear(B)], % preconditions
    [on(X,A), clear(B)], % delete
    [on(X,B), clear(A)] % add

):-
block(B), % ensures B is a block
A #\= B. % ensures block is not moved to the same location

act( move_to_table(X,A),
     [on(X,A), clear(X)],% preconditions
     [on(X,A)], % delete
     [on(X,0), clear(A)] % add
):-
table(0),
A #\= 0. % ensure A is not already on the table

% Goal state
goal_state([on(X,Y), on(Y,Z), on(Z,0)]):-
green(Y),
blue(Z).

% Initial state
initial_state([on(1,0),on(2,0),on(3,4),on(4,0),on(5,6),on(6,0),clear(1),clear(2),clear(3),clear(5)]).

no_forbidden_state.