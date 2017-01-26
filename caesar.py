def alphabet_position(letter):
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if letter in lower_case:
        return lower_case.index(letter)
    if letter in upper_case:
        return upper_case.index(letter)

def rotate_character(rot,char):
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_pos = (alphabet_position(char) + rot) % 26
    if char in lower_case:
        new_letter = lower_case[new_pos]
    if char in upper_case:
        new_letter = upper_case[new_pos]
    return new_letter

def encrypt(text, rot):
    something = ""
    for i in text:
        if i.isalpha() == True:
            something = something + rotate_character(rot, i)
        else:
            something = something + i

    return something
