morse_code = {
    "A": "*-", "B": "-***", "C": "-*-*", "D": "-**", "E": "*", "F": "**-*",
    "G": "--*", "H": "****", "I": "**", "J": "*---", "K": "-*-", "L": "*-**",
    "M": "--", "N": "-*", "O": "---", "P": "*--*", "Q": "--*-", "R": "*-*",
    "S": "***", "T": "-", "U": "**-", "V": "***-", "W": "*--", "X": "-**-",
    "Y": "-*--", "Z": "--**",
    
    "0": "-----", "1": "*----", "2": "**---", "3": "***--", "4": "****-",
    "5": "*****", "6": "-****", "7": "--***", "8": "---**", "9": "----*",
    
    " ": "/",  # Space is often represented as a slash or just a pause
    ".": "*-*-*-", ",": "--**--", "?": "**--**", "'": "*----*", "!": "-*-*--",
    "/": "-**-*", "(": "-*--*", ")": "-*--*-", "&": "*-***", ":": "---***",
    ";": "-*-*-*", "=": "-***-", "+": "*-*-*", "-": "-****-", "_": "**--*-",
    '"': "*-**-*", "$": "***-**-", "@": "*--*-*"
}
print("-Morse Code Translator-")
print("Option1: Translate English to Morse code")
print("Option2: Translate Morse Code to English")

option = input("\nEnter an option (1 or 2): ")

#Option 1: Translate English to Morse Code 
if option == "1":
    text = input("Enter a text: ").strip()
#converting each char to morse code in library
    morse = "".join(morse_code.get(char.upper(), "?")for char in text)
    print("Morse Code:", morse)  

#Option 2: Translate Morse Code to English
elif option == "2":
    morse = input("Enter Morse code: ").strip()
    text = ""

    morse_dict = {v: k for k, v in morse_code.items()}  # Reverse dictionary
        text = "".join(morse_dict.get(part, "?") for part in morse.split(" "))
        
        print("English Text:", text)
