def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


#function to get random location
#this was replaced with newer get location
# def get_location():
#    monster = None
#    door = None
#    player = None
#
#     return monster, door, player

def get_location():
    return random.sample(CELLS, 3)
#returns a list of 3 tuples...and then unpack the tuple..
