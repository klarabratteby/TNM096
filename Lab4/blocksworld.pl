:- use_module(library(clpfd)).

% Constraints
block(X) :- X in 1..4.
pyramid(X) :- X in 5..6.
orange(X) :- X in 1 \/ 4.
green(X) :- X in 2 \/ 5.
blue(X) :- X in 3 \/ 6.
