:- dynamic item/3.

start :-
    menu.

menu :-
    nl,
    write('1. Add Item'), nl,
    write('2. Order Items'), nl,
    write('3. Display Items'), nl,
    write('4. Exit'), nl,
    write('Enter your choice: '),
    read(Choice),
    process(Choice).

process(1) :- add_item, menu.
process(2) :- order_items, menu.
process(3) :- display_items, menu.
process(4) :- write('Thank you!'), nl.
process(_) :- write('Invalid choice'), nl, menu.

add_item :-
    write('Enter item name: '), nl,
    read(Name),
    write('Enter price: '), nl,
    read(Price),
    write('Enter quantity: '), nl,
    read(Qty),
    assertz(item(Name, Price, Qty)),
    write('Item added successfully!'), nl.

display_items :-
    write('Available Items:'), nl,
    forall(item(Name, Price, Qty),
        (write(Name), write(' - Rs.'), write(Price),
         write(' - Qty: '), write(Qty), nl)
    ).

order_items :-
    write('Enter number of products: '), nl,
    read(N),
    take_orders(N, Total),
    write('Total Bill = Rs.'), write(Total), nl.

take_orders(0, 0).
take_orders(N, Total) :-
    N > 0,
    write('Enter item name: '), nl,
    read(Name),
    write('Enter quantity: '), nl,
    read(Qty),

    ( item(Name, Price, AvailableQty) ->
        ( Qty =< AvailableQty ->
            Subtotal is Price * Qty,
            write('Subtotal = Rs.'), write(Subtotal), nl,

            NewQty is AvailableQty - Qty,
            retract(item(Name, Price, AvailableQty)),
            assertz(item(Name, Price, NewQty)),

            N1 is N - 1,
            take_orders(N1, RestTotal),
            Total is Subtotal + RestTotal
        ;
            write('Not enough quantity available!'), nl,
            take_orders(N, Total)
        )
    ;
        write('Item not found!'), nl,
        take_orders(N, Total)
    ).







:- dynamic pizza/3.

start :-
    menu.

menu :-
    nl,
    write('1. Add Pizza'), nl,
    write('2. Order Pizza'), nl,
    write('3. Display Menu'), nl,
    write('4. Exit'), nl,
    write('Enter your choice: '),
    read(Choice),
    process(Choice).

process(1) :- add_pizza, menu.
process(2) :- order_pizza, menu.
process(3) :- display_menu, menu.
process(4) :- write('Thank you!'), nl.
process(_) :- write('Invalid choice'), nl, menu.

add_pizza :-
    write('Enter pizza name: '), nl,
    read(Name),
    write('Enter price: '), nl,
    read(Price),
    write('Enter quantity available: '), nl,
    read(Qty),
    assertz(pizza(Name, Price, Qty)),
    write('Pizza added successfully!'), nl.

display_menu :-
    write('Available Pizzas:'), nl,
    forall(pizza(Name, Price, Qty),
        (write(Name), write(' - Rs.'), write(Price),
         write(' - Qty: '), write(Qty), nl)
    ).

order_pizza :-
    write('Enter number of pizzas to order: '), nl,
    read(N),
    take_orders(N, Total),
    write('Total Bill = Rs.'), write(Total), nl.

take_orders(0, 0).
take_orders(N, Total) :-
    N > 0,
    write('Enter pizza name: '), nl,
    read(Name),
    write('Enter quantity: '), nl,
    read(Qty),

    ( pizza(Name, Price, AvailableQty) ->
        ( Qty =< AvailableQty ->
            Subtotal is Price * Qty,
            write('Subtotal = Rs.'), write(Subtotal), nl,

            NewQty is AvailableQty - Qty,
            retract(pizza(Name, Price, AvailableQty)),
            assertz(pizza(Name, Price, NewQty)),

            N1 is N - 1,
            take_orders(N1, RestTotal),
            Total is Subtotal + RestTotal
        ;
            write('Not enough pizza quantity available!'), nl,
            take_orders(N, Total)
        )
    ;
        write('Pizza not found!'), nl,
        take_orders(N, Total)
    ).
