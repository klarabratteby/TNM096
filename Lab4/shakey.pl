
%   Shakey World

%  To run this example, first consult the planner you want to use
%  (strips.pl, idstrips.pl or exstrips.pl) and then consult shakey.pl
%  In the query window, run the goal:
%  ?- plan.


% actions
act( go(X,Y),
     [at(shakey,X), connected(X,Y), onfloor],
     [at(shakey,X)],
     [at(shakey,Y)]
     ).

act( push(B,X,Y),
     [at(shakey,X), at(B,X), connected(X,Y), light_on(X), onfloor],
     [at(shakey,X), at(B,X)],
     [at(shakey,Y), at(B,Y)]
     ).

act( turn_on(S),
     [at(shakey,S), inroom(S, Room), light_off(Room), onbox],
     [light_off(Room)],
     [light_on(Room)]
     ).

act( turn_off(S),
     [at(shakey,S), inroom(S, Room), light_on(Room), onbox],
     [light_on(Room)],
     [light_off(Room)]
     ).

act( climb_up(B,X),
     [at(shakey,X), at(B, X), onfloor],
     [onfloor],
     [onbox]
     ).

act( climb_down(X),
     [at(shakey,X), onbox],
     [onbox],
     [onfloor]
     ).  

goal_state( [at(shakey, room1), light_off(room1), at(box2, room2)] ).

initial_state(
     [    connected(room1, corridor),
          connected(room2, corridor),
          connected(room3, corridor),
          connected(room4, corridor),

          connected(corridor, room1),
          connected(corridor, room2),
          connected(corridor, room3),
          connected(corridor, room4),

          connected(room1, switch1),
          connected(room2, switch2),
          connected(room3, switch3),
          connected(room4, switch4),

          connected(switch1, room1),
          connected(switch2, room2),
          connected(switch3, room3),
          connected(switch4, room4),

          inroom(switch1, room1),
          inroom(switch2, room1),
          inroom(switch3, room1),
          inroom(switch4, room1),

          light_on(room1),
          light_on(room4),
          light_off(room2),
          light_off(room3),
          light_on(corridor),

          at(shakey, room3),
          at(box1, room1),
          at(box2, room1),
          at(box3, room1),
          at(box4, room1),

          onfloor
          ]).
