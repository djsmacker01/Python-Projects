# test.py

from main import convert_to_morse_code

# Test Case 1: Basic Input
input_text_1 = "python"
expected_output_1 = "......-...-..---"
assert convert_to_morse_code(input_text_1) == expected_output_1

# Test Case 2: Handling of Unknown Characters
input_text_2 = "hello123"
expected_output_2 = "......-...-..---"
assert convert_to_morse_code(input_text_2) == expected_output_2

# Test Case 3: Case Sensitivity
input_text_3 = "HelloWorld"
expected_output_3 = "......-...-..---.-----.-..-.."
assert convert_to_morse_code(input_text_3) == expected_output_3

# Add more test cases as needed




# import week10


# print(week10.addnum(50,89))
# print(week10.num)
# # answer = addnum(50,40)
# # print (week10)