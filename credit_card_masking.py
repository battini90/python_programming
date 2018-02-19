import re

DISCOVER_PATTERN = "6(?:011|5[0-9]{2})[0-9]{12}"
VISA_PATTERN = "4[0-9]{12}(?:[0-9]{3})?"
ANY_PATTERN = "6(?:011|5[0-9]{2})[0-9]{12} | 4[0-9]{12}(?:[0-9]{3})?"

user_input = input("Please enter any message: ")

def mask_message(user_input):
    pattern = re.compile(ANY_PATTERN)
    pattern.findall(user_input)
    masked_string = pattern.sub("*******", user_input)
    print(masked_string)



#
# def mask_message(user_input, matched_pattern):
#     pattern = re.compile(matched_pattern)
#     pattern.findall(user_input)
#     masked_string = pattern.sub("*******", user_input)
#     print(masked_string)

# def find_pattern(user_input):
#     if re.search(ANY_PATTERN, user_input):
#         mask_message(user_input, ANY_PATTERN)
#     elif re.search(VISA_PATTERN, user_input):
#         mask_message(user_input, VISA_PATTERN)
#     else:
#         mask_message(user_input, DISCOVER_PATTERN)

#find_pattern(user_input)


mask_message(user_input)







