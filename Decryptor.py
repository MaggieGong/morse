'''
This version so far can only decrypt 1 paragraphm maximum.
'''
morse = {
    ".-":"a", "-...":"b", "-.-.":"c", "-..":"d", ".":"e", "..-.":"f", "--.":"g", "....":"h", "..":"i", ".---":"j", "-.-":"k", ".-..":"l", "--":"m", "-.":"n", "---":"o", ".--.":"p", "--.-":"q", ".-.":"r", "...":"s", "-":"t", "..-":"u", "...-":"v", ".--":"w", "-..-":"x", "-.--":"y", "--..":"z"
}


code = str(input("Code to be decrypted: "))
decrypted_text = ""

def format(text):
    text = str(text)
    text = text.split(".")
    for sentence in text:
        print(sentence.strip().capitalize() + ". ", end="")

#paragraph splits into sentences
paragraph = code.split("'")
for sentences in paragraph:
    #sentences split into words
    sentence = sentences.split("  ")
    for words in sentence:
        word = words.split(" ")
        #words split into letters
        for letter in word:
            if letter in morse:
                decrypted_text += morse[letter]
            else:
                decrypted_text += letter
        decrypted_text += " "
    decrypted_text += "."
format(decrypted_text[:-4])
