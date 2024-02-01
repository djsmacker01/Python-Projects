# test.py

from main import convert_to_morse_code

# Test Case 1: Basic Input
inputText = "python"
expectedRes = ".--.-.---....-."
assert convert_to_morse_code(inputText) == expectedRes

# Test Case 2: Handling of Unknown Characters
inputText_2 = "hello123"
output = "......-...-..---"
assert convert_to_morse_code(inputText_2) == output

# Test Case 3: Case Sensitivity
inputText_3 = "HelloWorld"
output_2 = "......-...-..---.-----.-..-.."
assert convert_to_morse_code(inputText_3) == output_2

inputText_3 = ""
output_1 = "" 
assert convert_to_morse_code(inputText_3) == output_1
# The expected output for an empty input is an empty string
# To test for more extensive character 
inputText_1 = "The quick brown fox jumps over the lazy dog 123!@#$%^&*()"
output = "- .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --.   .-- --- .-.   - .... .   .-.. .- --.. -.--   -.. --- --.   .---- ..--- ...-- ! @ # $ % ^ & * ( )"
assert convert_to_morse_code(inputText_1) == output



print(convert_to_morse_code("python"))



#  Test Case:Extensive character
# Input: "The quick brown fox jumps over the lazy dog 123!@#$%^&*()"
# Actual Output: ....--.--.-.-.--....-..---...-.-..-.-----.--.......-.-.-.....-..--..-.---...-

# Enter text to convert: 
#  

# 
# Enter text to convert: python
# -.---....-.
# import week10
# print(week10.addnum(50,89))
# print(week10.num)
# # answer = addnum(50,40)
# # print (week10)