def queens(size):
    def is_valid(board_state, current_row, current_col):
        for previous_row in range(current_row):
            if board_state[previous_row] == current_col or abs(board_state[previous_row] - current_col) == abs(previous_row - current_row):
                return False
        return True

    def find_solutions(board_state, current_row):
        if current_row == size:
            all_solutions.append(board_state[:])  
            return
        for current_col in range(size):
            if is_valid(board_state, current_row, current_col):
                board_state[current_row] = current_col
                find_solutions(board_state, current_row + 1) 
                board_state[current_row] = -1 

    all_solutions = []
    board_state = [-1] * size 
    find_solutions(board_state, 0) 
    return all_solutions

def display_solutions(solutions):
    for solution in solutions:
        for row in solution:
            print(" ".join("Q" if col == row else "." for col in range(len(solution))))
        print()
        
size = 4  
solutions = queens(size)
print(f"Found {len(solutions)} solutions for size={size}:")
display_solutions(solutions)
