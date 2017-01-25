def alphabet_position(letter):
    letters = letter.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if letters in alphabet:
        position = alphabet.find(letters)
    return position

def rotate_character(char,rot):
    new_string = ""
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    if char.isalpha() == True:
        orig = alphabet_position(char)
        new = (orig + rot) % 26
        new_letter = alphabets[new]
        if char.islower() == True:
            new_string = new_string + new_letter.lower()
        if char.islower() == False:
            new_string = new_string + new_letter.upper()
    else:
        new_string = new_string + char
    return new_string



def encrypt(text,rot):
    new_string = ""
    for char in text:
        new_string = new_string + rotate_character(char,rot)

    return new_string
