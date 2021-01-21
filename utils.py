def remove_special_char(a_string: str):
    alpha_numeric = ""
    for character in a_string:
        if character.isalnum():
            alpha_numeric += character
    return alpha_numeric