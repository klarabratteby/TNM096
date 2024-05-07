
%   Shakey World

%  To run this example, first consult the planner you want to use
%  (strips.pl, idstrips.pl or exstrips.pl) and then consult the blocks.pl example
%  In the query window, run the goal:
%  ?- plan.


% actions
%% act( go(X,Y),
%%      [at(X), door(X,corridor), door(Y,corridor), onfloor],
%%      [at(X)],
%%      [at(Y)]
%%      ).

act( go(X,Y),
     [at(X), onfloor],
     [at(X)],
     [at(Y)]
     ).

%% act( room_go(X,Y,Room),
%%      [at(X), inroom(X,Room), inroom(Y,Room), onfloor],
%%      [at(X)],
%%      [at(Y)]
%%      ).

act( push(B, X, Y, Room),
     [at(X), box_at(B,X), light_on(Room), onfloor],
     [at(X), box_at(B,X)],
     [at(Y), box_at(B,Y)]
     ).

act( turn_on(S, Room),
     [at(S), inroom(S, Room), light_off(Room), onbox],
     [light_off(Room)],
     [light_on(Room)]
     ).

act( turn_off(S, Room),
     [at(S), inroom(S, Room), light_on(Room), onbox],
     [light_on(Room)],
     [light_off(Room)]
     ).

act( climb_up(B, X),
     [at(X), box_at(B, X), onfloor],
     [onfloor],
     [onbox]
     ).

act( climb_down(B, X),
     [at(X), onbox],
     [onbox],
     [onfloor]
     ).  

% goal_state( [at(room1), light_off(room1), box_at(box2, room2)] ).
goal_state( [at(room1), light_off(room1)] ).

initial_state(
     [    door(room1, corridor),
          door(room2, corridor),
          door(room3, corridor),
          door(room4, corridor),
          inroom(switch1, room1),
          inroom(switch2, room2),
          inroom(switch3, room3),
          inroom(switch4, room4),
          inroom(box1, room1),
          inroom(box2, room1),
          inroom(box3, room1),
          inroom(box4, room1),
          light_on(room1),
          light_on(room4),
          light_off(room2),
          light_off(room3),
          at(room3),
          box_at(box1, box1),
          box_at(box2, box2),
          box_at(box3, box3),
          box_at(box4, box4),
          onfloor
          ]).
