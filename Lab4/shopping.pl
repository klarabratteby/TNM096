%====================================================================
% SHOPPING PROBLEM

% CONTROL PARAMETERS
ordering(partial).
derivedPlans(one).

% ACTIONS:    action(Name,Prec,Del,Add)

% Agent A buys item X at the Store
action(buy(A,W,Store),
	[store(Store),at(A,Store),sells(Store,W)],
	[],
	[has(A,W),objAt(W,Store)]).

% Agent A goes from location X to location Y
action(go(A,X,Y),
	[location(X),location(Y),X\=Y,at(A,X)],
	[at(A,X)],
	[at(A,Y)]).

action(carry(A,W,X,Y),
	[has(A,W),location(X),location(Y),X\=Y,at(A,X),objAt(W,X)],
	[at(A,X),objAt(W,X)],
	[at(A,Y),objAt(W,Y)]).

% PARALLELISMS
parallel(X, Y) :- X =.. [F|_], Y =.. [F|_], F = buy, !.
parallel(X, Y) :- X =.. [F, A, W1, From, To], Y =.. [F, A, W2, From, To], F = carry, W1 \= W2, !.

% FLUENT
fluent(at(_,_)).
fluent(has(_,_)).
fluent(objAt(_,_)).

% DOMAIN KNOWLEDGE
store(ica) <- [].
store(clasohlson) <- [].
sells(ica,banana) <- [].
sells(ica,bread) <- [].
sells(ica,cheese) <- [].
sells(clasohlson,drill) <- [].
location(home) <- [].
location(office) <- [].
location(X) <- [store(X)].

% INITIAL SITUATION
holds(at(chris,home),init).
