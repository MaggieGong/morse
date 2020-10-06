'''
This version so far can only encrypt 1 paragraphm maximum. The later versions will be able to encrypt txt files and other types of files as well.
'''
morse = {
    "A":".-", "B":"-...", "C":"-.-.", "D":"-..", "E":".", "F":"..-.", "G":"--.", "H":"....", "I":"..", "J":".---", "K":"-.-", "L":".-..", "M":"--", "N":"-.", "O":"---", "P":".--.", "Q":"--.-", "R":".-.", "S":"...", "T":"-", "U":"..-", "V":"...-", "W":".--", "X":"-..-", "Y":"-.--", "Z":"--..",
}

#upper-case every letter in the text the user input
text = str(input('Text to be encrypted: ')).upper()
encrypted_text, index = "", 0


#after each letter: 1 space
#after each word: 2 space
#after each sentence: 3 space
#after each paragraph: new line

while index < len(text):
    if text[index] in morse:
        encrypted_text += (morse[text[index]] + " ")
    elif text[index] == " ":
        encrypted_text += (text[index] + "  ")
    elif text[index] == ".":
        encrypted_text += ("'")
    else:
        encrypted_text += (text[index] + " ")
    index += 1
print("\n" + 'ORIGINAL:' + "\n" + text)
print("\n" + "ENCRYPTED:" + "\n" + encrypted_text)