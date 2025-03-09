class JugSolver:
    def __init__(self, capacity_1, capacity_2, target_amount):
        self.capacity_1 = capacity_1 
        self.capacity_2 = capacity_2 
        self.target_amount = target_amount
        self.visited_states = set()  

    def is_valid(self, state):
        return 0 <= state[0] <= self.capacity_1 and 0 <= state[1] <= self.capacity_2

    def print_move(self, action, state):
        print(f"{action} -> Jug 1: {state[0]} Gallons, Jug 2: {state[1]} Gallons")

    def depth_first_search(self, initial_state):
        stack = [(initial_state, [])]
        while stack:
            current_state, actions = stack.pop()
            if current_state[0] == self.target_amount or current_state[1] == self.target_amount:
                print("Solution found!")
                for action in actions:
                    print(action)
                return True
            
            if current_state in self.visited_states:
                continue
            self.visited_states.add(current_state)

            jug1, jug2 = current_state

            possible_moves = [
                ((self.capacity_1, jug2), "Fill Jug 1"),  
                ((jug1, self.capacity_2), "Fill Jug 2"), 
                ((0, jug2), "Empty Jug 1"),               
                ((jug1, 0), "Empty Jug 2"),             
                ((0, jug1 + jug2) if jug1 + jug2 <= self.capacity_2 else (jug1 - (self.capacity_2 - jug2), self.capacity_2), "Pour Jug 1 into Jug 2"),
                ((jug1 + jug2, 0) if jug1 + jug2 <= self.capacity_1 else (self.capacity_1, jug2 - (self.capacity_1 - jug1)), "Pour Jug 2 into Jug 1")
            ]

            for next_state, action in possible_moves:
                if self.is_valid(next_state):
                    stack.append((next_state, actions + [action]))

        print("No solution found!")
        return False

jug1_capacity = 5
jug2_capacity = 3
target_amount = 4

solver = JugSolver(jug1_capacity, jug2_capacity, target_amount)
solver.depth_first_search((0, 0)) 
