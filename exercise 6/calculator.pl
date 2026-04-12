start :-
    write('Enter first number: '), nl,
    read(X),
    write('Enter second number: '), nl,
    read(Y),
    write('Choose operation: add / subtract / multiply / divide / modulus / power'), nl,
    read(Op),
    calculate(Op, X, Y, R),
    write('Result is: '), write(R), nl.

calculate(add, X, Y, R) :- R is X + Y.
calculate(subtract, X, Y, R) :- R is X - Y.
calculate(multiply, X, Y, R) :- R is X * Y.
calculate(divide, X, Y, R) :- Y \= 0, R is X / Y.
calculate(modulus, X, Y, R) :- R is X mod Y.
calculate(power, X, Y, R) :- R is X ** Y.

% Load set operations library
:- use_module(library(lists)).

start :-
    write('Choose: math / set'), nl,
    read(Type),
    run(Type).

% --- Simple Math ---
run(math) :-
    write('Enter X: '), read(X),
    write('Enter Y: '), read(Y),
    write('Op (add, subtract, multiply, divide): '), read(Op),
    math_calc(Op, X, Y, R),
    write('Result: '), write(R), nl.

math_calc(add, X, Y, R)      :- R is X + Y.
math_calc(subtract, X, Y, R) :- R is X - Y.
math_calc(multiply, X, Y, R) :- R is X * Y.
math_calc(divide, X, Y, R)   :- R is X / Y.

% --- Simple Sets ---
run(set) :-
    write('Enter Set1 (e.g. [1,2]): '), read(S1),
    write('Enter Set2 (e.g. [2,3]): '), read(S2),
    write('Op (union, intersection, difference): '), read(Op),
    set_calc(Op, S1, S2, R),
    write('Result: '), write(R), nl.

set_calc(union, S1, S2, R)        :- union(S1, S2, R).
set_calc(intersection, S1, S2, R) :- intersection(S1, S2, R).
set_calc(difference, S1, S2, R)   :- subtract(S1, S2, R).

