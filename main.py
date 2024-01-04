dot = "·"
dash = "–"

morseCode_dict = {
    " ": "   ",
    "A": dot + dash,
    "B": dash + dot + dot + dot,
    "C": dash + dot + dash + dot,
    "D": dash + dot + dot,
    "E": dot,
    "F": dot + dot + dash + dot,
    "G": dash + dash + dot,
    "H": dot + dot + dot + dot,
    "I": dot + dot,
    "J": dot + dash + dash + dash,
    "K": dash + dot + dash,
    "L": dot + dash + dot + dot,
    "M": dash + dash,
    "N": dash + dot,
    "O": dash + dash + dash,
    "P": dot + dash + dash + dot,
    "Q": dash + dash + dot + dash,
    "R": dot + dash + dot,
    "S": dot + dot + dot,
    "T": dash,
    "U": dot + dot + dash,
    "V": dot + dot + dot + dash,
    "W": dot + dash + dash,
    "X": dash + dot + dot + dash,
    "Y": dash + dot + dash + dash,
    "Z": dash + dash + dot + dot,
    "1": dot + dash + dash + dash + dash,
    "2": dot + dot + dash + dash + dash,
    "3": dot + dot + dot + dash + dash,
    "4": dot + dot + dot + dot + dash,
    "5": dot + dot + dot + dot + dot,
    "6": dash + dot + dot + dot + dot,
    "7": dash + dash + dot + dot + dot,
    "8": dash + dash + dash + dot + dot,
    "9": dash + dash + dash + dash + dot,
    "0": dash + dash + dash + dash + dash,
}


def ask_for_retry():
    ans = input("Would you like to try again ?: Y/N ").upper()
    return ans


print(
    """
    This is a text-based program that will let you
    convert Text to Morse Code!
"""
)
stillContinue = True
while stillContinue:
    text = str(input("Please input the text that will be converted: ").upper())
    output_text = "".join((morseCode_dict.get(char) for char in text))
    print(output_text)
    retry = ask_for_retry()
    while retry not in ["Y", "N"]:
        print("Invalid response, please enter again ")
        retry = ask_for_retry()
    if retry == "N":
        stillContinue = False
