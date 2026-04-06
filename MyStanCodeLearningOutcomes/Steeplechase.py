"""
File: Steeplechase.py
Name: 詹以新
---------------------------------

"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    pass

    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()


def jump():
    up()
    down()

def up():
    """
    Pre:east
    Post:north
    """
    turn_left()

    while not right_is_clear():
        move()
    turn_right()

def down():
    """
    Pre:east
    Post:east
    """
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

def turn_right():
    for i in range(3):
        turn_left()

# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
