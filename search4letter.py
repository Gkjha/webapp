def search4letter(phrase:str, letter:str='aeiou') -> str:
    return str(set(phrase).intersection(set(letter)))
