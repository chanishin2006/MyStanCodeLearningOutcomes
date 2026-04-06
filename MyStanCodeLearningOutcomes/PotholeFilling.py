"""
File: PotholeFilling.py
Name: 詹以新
--------------------------
This program demonstrates how Karel fills multiple potholes
by using decomposition.

In this program, we will guide Karel to fix three potholes
on the road. Instead of writing all the commands in one place,
we will practice breaking a big task into smaller, reusable
functions to make the program clearer and easier to manage.
"""

from karel.stanfordkarel import *


def main():
    """
    TODO
    """
    pass
    for i in range(3):
        move()
        turn_right()
        move()
        put_99beeper()
        turn_left()
        turn_left()
        move()
        turn_right()
        move()





def turn_right():
    turn_left()
    turn_left()
    turn_left()

def put_99beeper():
    for i in range(99):
        put_beeper()

# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
