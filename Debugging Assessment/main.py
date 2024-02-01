# morse_chart = {
#     "a": "",
#     "b": "-...",
#     "c": "-.-.",
#     "d": "-..",
#     "e": "",
#     "f": "..-.",
#     "g": ".-",
#     "h": "....",
#     "i": "",
#     "j": ".---",
#     "k": "-.-",
#     "l": ".-..",
#     "m": "--",
#     "n": "-.",
#     "o": "",
#     "p": ".--.",
#     "q": "--.-",
#     "r": ".-.",
#     "s": "...",
#     "t": "-",
#     "u": "",
#     "v": "...-",
#     "w": ".--",
#     "x": "-..-",
#     "y": "-.--",
#     "z": "--..",
# }

# def convert_to_morse_code(text):
#     '''
#     Converts English text to morse code
#     :param text: Text to translate
#     :return: A string of morse code
#     '''
#     conversion = ""
#     for i in range(1, len(text)):
#         character = text[i]
#         if character in morse_chart:
#             conversion += morse_chart[character]
#     return conversion


# print(convert_to_morse_code(input("Enter text to convert: ")))
















# morse_chart = {
#     "a": ".-",
#     "b": "-...",
#     "c": "-.-.",
#     "d": "-..",
#     "e": ".",
#     "f": "..-.",
#     "g": "--.",
#     "h": "....",
#     "i": "..",
#     "j": ".---",
#     "k": "-.-",
#     "l": ".-..",
#     "m": "--",
#     "n": "-.",
#     "o": "---",
#     "p": ".--.",
#     "q": "--.-",
#     "r": ".-.",
#     "s": "...",
#     "t": "-",
#     "u": "..-",
#     "v": "...-",
#     "w": ".--",
#     "x": "-..-",
#     "y": "-.--",
#     "z": "--..",
# }

# def convert_to_morse_code(text):
#     '''
#     Converts English text to morse code
#     :param text: Text to translate
#     :return: A string of morse code
#     '''
#     conversion = ""
#     for i in range(len(text)):
#         character = text[i]
#         if character in morse_chart:
#             conversion += morse_chart[character] + " "
#     return conversion

# print(convert_to_morse_code(input("Enter text to convert: ").lower()))
