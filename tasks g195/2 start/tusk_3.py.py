morse = dict((
('A', '.-'),
('B', '-...'),
('C', '-.-.'),
('D', '-..'),
('E', '.'),
('F', '..-.'),
('G', '--.'),
('H', '....'),
('I', '..'),
('J', '.---'),
('K', '-.-'),
('L', '.-..'),
('M', '--'),
('N', '-.'),
('O', '---'),
('P', '.--.'),
('Q', '--.-'),
('R', '.-.'),
('S', '...'),
('T', '-'),
('U', '..-'),
('V', '...-'),
('W', '.--'),
('X', '-..-'),
('Y', '-.--'),
('Z', '--..'),
('1', '.----'),
('2', '..---'),
('3', '...--'),
('4', '....-'),
('5', '.....'),
('6', '-....'),
('7', '--...'),
('8', '---..'),
('9', '----.'),
('0', '-----')))


def textmorse(text):
    morse_code = []
    for caps in text.upper():
        if caps in morse:
            morse_code.append(morse[caps])
        else:
            morse_code.append('/')
    return ' '.join(morse_code)
word = input("Enter tekst: ")
morseout = textmorse(word)
print(f"Zashifrovanii tekst '{word}': {morseout}")
