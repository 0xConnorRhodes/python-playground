# Reeborg's World Challenge: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if front_is_clear() and not is_facing_north():
        move()
    elif front_is_clear() and wall_on_right():
        move()
    elif is_facing_north() and not wall_on_right():
        turn_right()
        move()
        turn_right()
    elif wall_in_front():
        turn_left()

