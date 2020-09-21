def decodeMorse(morse_code):
    """
    morse_code: string containing morse code
    returns decoded morse code in upper case
    """
    words = [morse_word for morse_word in morse_code.split("  ")]
    letters = [l for w in words for l in w.split(" ")]
    decoded = ""
    for l in letters:
        if l != '':
            decoded += MORSE_CODE[l]
        else:
            decoded += ' '
    return decoded.strip()
    #return morse_code.replace('.', MORSE_CODE['.']).replace('-', MORSE_CODE['-']).replace(' ', '')
