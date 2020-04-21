from karel.stanfordkarel import *

"""
File: TripleKarel.py
--------------------
When you finish writing this file, TripleKarel should be
able to paint the exterior of three buildings in a given
world, as described in the Assignment 1 handout. You
should make sure that your program works for all of the 
Triple sample worlds supplied in the starter folder.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    paint_rectangle() 
    turn_right() 
    paint_rectangle()
    turn_right()
    paint_rectangle()


def paint_side():
    while left_is_blocked():
        put_beeper()
        move()

def paint_rectangle():
    paint_side()
    turn_left()
    move()
    paint_side()
    turn_left()
    move()
    paint_side()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
    
   
  
 


