import os

morse = {
    "A":".-", "B":"-...", "C":"-.-.", "D":"-..", "E":".", "F":"..-.", "G":"--.", "H":"....", "I":"..", "J":".---", "K":"-.-", "L":".-..", "M":"--", "N":"-.", "O":"---", "P":".--.", "Q":"--.-", "R":".-.", "S":"...", "T":"-", "U":"..-", "V":"...-", "W":".--", "X":"-..-", "Y":"-.--", "Z":"--..",
}

print("# make sure you have put the file you want to encrypt in the same directory #")
file_name = str(input('file name: '))

here = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(here, file_name)
text = open(file if ".txt" in file else file + ".txt", "r").read().upper()

encrypted_text = ""

for _ in text:
    if _ in morse:
        encrypted_text += (morse[_] + " ")
    elif _ == " ":
        encrypted_text += "  "
    elif _ == ".":
        encrypted_text += "'"
    else:
        encrypted_text += (_ + " ")
        
print("\n" + "ORIGINAL:" + "\n" + text)
print("\n" + "ENCRYPTED:" + "\n" + encrypted_text)
