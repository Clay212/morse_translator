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

option = input("\nEnter an option: ")

if option == "1":
    text = input("Enter text: ").strip()
    morse = ""

  for char in text:
        morse += morse_code.get(char.upper(), "?") + " "  # Add space between Morse symbols

    print(morse.strip())  # Strip extra space at the end


