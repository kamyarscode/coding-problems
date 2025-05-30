"""
Problem: 
Come up with solution to take input of elevator starting floor and the floors to visit and output how long it takes
to visit all the floors in order. 

Run Script:
Clone this repo or download the elevatorProblem.py file.
Navigate to directory of script then run:
python or python3 eleavatorProblem.py

Assumptions:
Script input passed in from inside code function, not from CMD or GUI.
Single floor travel time - 10 seconds
starting_floor must be an integer between 1 and max floor. If not, then return (0, [0]) to indicate invalid input.
floors_to_visit array values must be integer in range 1 through max floor to start computing. If not, then invalid input and floor doesn't exist.
We can return a tuple of int and list i.e return (int, []). This is a bit more readable than having 1 output array with index 0 designated as total time.
Don't throw or raise exceptions with text when catching errors, instead we can just return a standard format of (int, []). Throwing exceptions is recommended for larger systems. 
Function takes in starting_floor and the floors_to_visit as separate parameters. 
Max floor in building = 50. Cannot go above 50. 
Starting floor counts as a visited floor. 
Floors to visit array can be empty because someone could just walk into the elevator and not press any buttons for fun and just stand there menacingly.
If you have consecutive repeating floors i.e [1,2,3,4,4,5], you would still be on the same floor, so do nothing.

"""

### -------------------------------------------------------------------------------------------------------------------- ###
"""
Function Description:
Take starting floor and list of floors to visit and figure out how much time it will take to go to all floors. 

Time Complexity:
O(n) because you are iterating through exactly 1 for loop at any time, which is the most computationally expensive process in this function.
- max() function 
- for loop in any()
- my own for loop

Space Complexity: 
- O(n) when creating arrays in defaults.
- O(1) when creating ints in defaults.
- O(1) when setting output array of (int, []).

Parameters:
starting_floor: int - Integer representing what floor elevator starts on.
floors_to_visit: list - All the floors to visit in that order.

Returns: 
Tuple[int, list[int]] - Tuple representing visitation info in format (total travel time in seconds, [floors visited])

"""

# Import List and Tuple to help with type hinting.
from typing import Tuple, List

def elevator(starting_floor: int, floors_to_visit: List[int]) -> Tuple[int, List[int]]:
    
    ### Defaults and variables:
    TIME_PER_FLOOR = 10 # Set time per floor to be 10 seconds.
    total_time = 0 # Start at 0 for total count. 
    current_floor = starting_floor # Make your current floor the starting one initially.
    max_floor = 50 # Set max floor. Set to float('inf') to remove floor restriction. 
    visited = [starting_floor] # Array to track which floors have already been visited. Starting with your first floor. 

    ### Base cases and invalid inputs:
    # Check to see starting floor is integer or if it is less than 1. Starting floor must be integer between 1 and max floor. 
    # Your floor pretty much doesn't exist, so return (0, [0]). 
    if not isinstance(starting_floor, int) or starting_floor < 1 or starting_floor > max_floor:
        return (0, [0])
    
    # If floors array is empty, you're just standing there inside the elavator without it moving.
    # You won't move. Return the floor you're on which would be your starting floor.
    if floors_to_visit is None:
        return (0, [starting_floor])

    # Check floors to see if they adhere to being an integer in range of 1 through max floor.
    # You won't move. Return the floor you're on which would be your starting floor.
    if any(not isinstance(floor, int) or floor < 1 or floor > max_floor for floor in floors_to_visit):
        return (0, [starting_floor])
    

    # Look at each floor in order and explicitly traverse through loop.
    for floor in floors_to_visit: 
        # Start from current floor and navigate to next floor. Can simplify this logic using abs(current_floor - floor) * TIME_PER_FLOOR too. 
        # going down
        if current_floor > floor:
            # calculate difference in floors and multiply by 10 for time traveled. 
            total_time += (current_floor - floor) * TIME_PER_FLOOR
            # Add floor visited to visited array.
            visited.append(floor)

        # going up
        if current_floor < floor:
            total_time += (floor - current_floor) * TIME_PER_FLOOR
            # Add floor visited to visited array.
            visited.append(floor)

        # If loop goes here, then we know the current_floor == floor. We can skip this. 
        else:
            pass

        # Set current floor to be where you just were.
        current_floor = floor

    # Finalize the output and return tuple.
    return (total_time, visited)



def main():

    # Set inputs here
    starting_floor = 12
    floors_to_visit = [2,9,1,32]

    print (elevator(starting_floor=starting_floor, floors_to_visit=floors_to_visit))

if __name__ == "__main__":
    main()