:- use_module(library(clpfd)).

% Constraints
block(X) :- X in 1..4.
pyramid(X) :- X in 5..6.
orange(X) :- X in 1 \/ 4.
green(X) :- X in 2 \/ 5.
blue(X) :- X in 3 \/ 6.

% Actions
act(move(X,A,B),
    [on(X,A), clear(X),clear(B)],[on(X,A)], %preconditions
    [on(X,A)], % delete
    [on(X,B), clear(A)] % add

):-
block(B), % ensures B is a block
A #\= B. % ensures block is not moved to the same location


% Goal state
goal_state([on(X,Y), on(Y,Z)]):-
green(Y).
blue(Z).

% Initial state
initial_state([on(1,0),on(2,0),on(3,4),on(4,0),on(5,6),on(6,0)]).