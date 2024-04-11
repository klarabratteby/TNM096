import heapq
import time


class State:
    def __init__(self, state, parent, cost, heuristic):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic
    # Equality comparison

    def __eq__(self, other):
        return self.state == other.state

    # Less than comparison
'''
    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)
'''

# Function for h1


def h1(state, goal_state):
    # Number of misplaced tiles
    misplaced = sum(1 for i in range(len(state))
                    if state[i] != goal_state[i] and state[i] != 0)

    return misplaced

# Function for h2


def h2(state, goal_state):
    distance = 0

    for i in range(len(state)):
        if state[i] != 0:  # Skip the blank tile
            # Calculate the current position and goal position of the tile
            row, col = i // 3, i % 3
            goal_index = goal_state.index(state[i])
            goal_row, goal_col = goal_index // 3, goal_index % 3

            # Calculate the Manhattan distance for the tile
            distance += abs(row - goal_row) + abs(col - goal_col)

    return distance


# Possible actions

def actions(state):
    actions = []

    for i in range(len(state)):
        # Check if the current index contains the blank space (0)
        if state[i] == 0:
            # Check if moving up is possible
            if i > 2:
                actions.append('up')
            # Check if moving down is possible
            if i < 6:
                actions.append('down')
            # Check if moving left is possible
            if i % 3 > 0:
                actions.append('left')
            # Check if moving right is possible
            if i % 3 < 2:
                actions.append('right')
    return actions


def apply_action(state, action):
    # Find the index of the blank space (0) in the state
    blank_index = state.index(0)
    # Determine the new index after applying the action
    new_index = None
    if action == 'up':
        new_index = blank_index - 3
    elif action == 'down':
        new_index = blank_index + 3
    elif action == 'left':
        new_index = blank_index - 1
    elif action == 'right':
        new_index = blank_index + 1

    # Check if the new index is within bounds
    if 0 <= new_index < len(state):
        # Swap the blank space with the tile in the new index
        state[blank_index], state[new_index] = state[new_index], state[blank_index]
        return state  # Return the new state after applying the action
    else:
        return None  # Return None if the action cannot be applied

# Priority queue for states


class PriorityQueue:
    # Initialize the priority queue
    def __init__(self):
        self.elements = []
    # Check is the priority queue is empty

    def empty(self):
        return len(self.elements) == 0  # checks if priority queue is empty
    # Insert an item based on priority

    def put(self, item, priority):
        # priority and item = state object
        heapq.heappush(self.elements, (priority, item))
    # Remove item

    def get(self):
        return heapq.heappop(self.elements)[1]


def astar(initial_state, goal_state, heuristic):
    frontier = PriorityQueue()
    # state attribute of the State object holds a reference to the initial_state,
    start_state = State(initial_state, None, 0,
                        heuristic(initial_state, goal_state))
    # Add initial state to the priorityqueue with priority based on cost and heuristic
    frontier.put(start_state, start_state.cost + start_state.heuristic)
    # Keep track of explored states
    explored = set()

    while not frontier.empty():

        current_state = frontier.get()

        # Check if current state is the goal state
        if current_state.state == goal_state:
            # Construct and return the solution path
            return construct_solution_path(current_state)
        # Mark the current state as explored
        explored.add(tuple(current_state.state))
        # Explore possible actions from current state
        for action in actions(current_state.state):

            # Apply action to generate the next state
            next_state = apply_action(current_state.state.copy(), action)
            # Check if the next state has not been explored
            if tuple(next_state) not in explored:
              # State object is created
                next_state_obj = State(
                    next_state, current_state, current_state.cost + 1, heuristic(next_state, goal_state))
                # add to the priority queue
                frontier.put(next_state_obj, next_state_obj.cost +
                             next_state_obj.heuristic)

    return None

# Construct solution path


def construct_solution_path(state):
    path = []
    # Trace back from the goal state to the initial state by following parent pointers
    while state.parent:
        # add current state to path
        path.append(state.state)
        # move to the parent state
        state = state.parent
    # Add the initial state to the path
    path.append(state.state)
    # Return the solution path in reverse order (from initial state to goal state)
    return path[::-1]


def print_state(state):
    for i in range(3):
        print(state[i * 3:i * 3 + 3])
    print()


    # Main program
if __name__ == "__main__":
    # initial_state = [2, 5, 0, 1, 4, 8, 7, 3, 6]
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    initial_state = [8, 6, 7, 2, 5, 4, 3, 0, 1]

    # Start time
    start_time = time.time()

    # Choose heuristic function

    while True:
        choice = input("Enter h1 or h2:")
        if choice in ['h1', 'h2']:
            break
        else:
            print("Invalid")

    heuristic_function = globals()[choice]

    h1_value = h1(initial_state, goal_state)
    print("Missplaced tiles:", h1_value)
    h2_value = h2(initial_state, goal_state)
    print("Manhattan distance:", h2_value)

    # Run A*
    solution_path = astar(initial_state, goal_state, heuristic_function)

    # Calculate elapsed time
    elapsed_time = time.time() - start_time

    # Elapsed time
    print("Elapsed Time:", elapsed_time, "seconds")

    if solution_path:
        print("Solution found:")
        print("Initial State:")
        print_state(initial_state)
        print("Goal State:")
        print_state(goal_state)
        print("Solution Path:")
        for index, state in enumerate(solution_path):
            print(f"State {index}:")
            print_state(state)
    else:
        print("No solution found.")
