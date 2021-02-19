def create_monster_cast():
    monster_cast = {}
    return  monster_cast

def add_cast_member(monsters,character,cast_member):
    monsters[character] = cast_member
    return monsters

def get_cast_member(monsters,character):
    return monsters[character]

def get_cast_size(monsters):
    count = 0
    for key in monsters:
        count += 1
    return count

def change_cast_member(monsters,character,cast_member):
    monsters[character] = cast_member
    return monsters

def has_character(monsters,character):

    for key in monsters:
        if key == character:
            return True

    return False

def has_cast_member(monsters,cast_member):

    for key in monsters:
        if monsters[key] == cast_member:
            return True
    return False

def get_longest_cast_member(monsters):
    count = 0
    for value in monsters:
        cast = len(monsters[value])
        if cast > count:
            count = cast
            word = monsters[value]
    return word

def get_longest_character(monsters):
    count = 0
    for key in monsters:
        key1 = len(key)
        if key1 > count:
            count = key1
            word = key
    return word

def get_character_of_longest_cast_member(monsters):
    count = 0
    for key in monsters:
        char = len(monsters[key])
        if char > count:
            count = char
            word = key
    return word
