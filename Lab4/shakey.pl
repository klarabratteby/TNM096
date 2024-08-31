
%   Shakey World

%  To run this example, first consult the planner you want to use
%  (strips.pl, idstrips.pl or exstrips.pl) and then consult shakey.pl
%  In the query window, run the goal:
%  ?- plan.


% actions

act( push(B,X,Y),
     [at(shakey,X), at(B,X), connected(X,Y), inroom(X,Room), light_on(Room), inroom(X,RoomX), inroom(shakey,RoomX), inroom(Y,RoomY), onfloor],
     [at(shakey,X), at(B,X), inroom(shakey,RoomX)],
     [at(shakey,Y), at(B,Y), inroom(shakey,RoomY)]
     ).

act( go(X,Y),
     [at(shakey,X), connected(X,Y), inroom(X,RoomX), inroom(shakey,RoomX), inroom(Y,RoomY), onfloor],
     [at(shakey,X), inroom(shakey,RoomX)],
     [at(shakey,Y), inroom(shakey,RoomY)]
     ).

act( turn_on(S),
     [at(shakey,S), switch(S), inroom(S,Room), light_off(Room), onbox],
     [light_off(Room)],
     [light_on(Room)]
     ).

act( turn_off(S),
     [at(shakey,S), switch(S), inroom(S,Room), light_on(Room), onbox],
     [light_on(Room)],
     [light_off(Room)]
     ).

act( climb_up(B,X),
     [at(shakey,X), at(B,X), box(B), onfloor],
     [onfloor],
     [onbox]
     ).

act( climb_down(X),
     [at(shakey,X), onbox],
     [onbox],
     [onfloor]
     ).  

% goal_state( [inroom(shakey,room1), light_off(room1), at(box2,room2)] ).
goal_state( [light_off(room1)] ).

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

          inroom(corridor, corridor),

          inroom(room1, room1),
          inroom(room2, room2),
          inroom(room3, room3),
          inroom(room4, room4),

          inroom(switch1, room1),
          inroom(switch2, room2),
          inroom(switch3, room3),
          inroom(switch4, room4),

          switch(switch1),
          switch(switch2),
          switch(switch3),
          switch(switch4),

          box(box1),
          box(box2),
          box(box3),
          box(box4),

          light_on(room1),
          light_on(room4),
          light_off(room2),
          light_off(room3),
          light_on(corridor),

          at(shakey, room3),
          inroom(shakey, room3),

          at(box1, room1),
          at(box2, room1),
          at(box3, room1),
          at(box4, room1),

          onfloor
          ]).
