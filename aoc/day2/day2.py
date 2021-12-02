'''
--- Day 2: Dive! ---
Now, you need to figure out how to pilot this thing.

It seems like the submarine can take a series of commands like forward 1, down 2, or up 3:

forward X increases the horizontal position by X units.
down X increases the depth by X units.
up X decreases the depth by X units.
Note that since you're on a submarine, down and up affect your depth, and so they have the opposite result of what you might expect.

The submarine seems to already have a planned course (your puzzle input). You should probably figure out where it's going. For example:

forward 5
down 5
forward 8
up 3
down 8
forward 2
Your horizontal position and depth both start at 0. The steps above would then modify them as follows:

forward 5 adds 5 to your horizontal position, a total of 5.
down 5 adds 5 to your depth, resulting in a value of 5.
forward 8 adds 8 to your horizontal position, a total of 13.
up 3 decreases your depth by 3, resulting in a value of 2.
down 8 adds 8 to your depth, resulting in a value of 10.
forward 2 adds 2 to your horizontal position, a total of 15.
After following these instructions, you would have a horizontal position of 15 and a depth of 10. (Multiplying these together produces 150.)

Calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth?

'''

from aoc.helpers import read_file_to_list

part1_test_set = read_file_to_list("/day2/day2_part1_test.txt")
part1_input_set = read_file_to_list("/day2/day2_part1.txt")


"""
Calculate final position and depth 
"""
def get_final_position(data_set: list[str]):
    
    currentState = [0, 0] # hposition, depth
    
    for i in range(0, len(data_set)):
        
        line = data_set[i].split()
        
        direction = line[0]
        dist = int(line[1])
        
        if direction == 'forward':
            currentState[0] +=  dist
        elif direction == 'up':
            currentState[1] -=  dist
        else:
            currentState[1] +=  dist
            
    return currentState[0] * currentState[1]

"""
Calculate final position and depth with Aim
"""
def get_final_position_with_aim(data_set: list[str]):
    
    currentState = [0, 0, 0] # hposition, depth, aim 
    
    for i in range(0, len(data_set)):
        
        line = data_set[i].split()
        
        direction = line[0]
        dist = int(line[1])
        
        if direction == 'forward':
            currentState[0] +=  dist
            if(dist != 0):
                currentState[1] += (currentState[2] * dist)
        elif direction == 'up':
            currentState[2] -=  dist
        else:
            currentState[2] +=  dist
            
    return currentState[0] * currentState[1]


    
assert get_final_position(part1_test_set) == 150
print("solution 1:", get_final_position(part1_input_set))

assert get_final_position_with_aim(part1_test_set) == 900
print("solution 2:", get_final_position_with_aim(part1_input_set))

