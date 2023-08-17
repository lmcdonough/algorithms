"""
write a function that:
 - iterates through a string
 - compares each character with the characters seen before
 - evaluates that each opening character has an equal closing
   charater
    - the string/list contains contain an unordered list of the characters "[({})]".
    - true/false question
        - TRUTH: the character is in the closing types group.
        - FALSE: the character is in the opening types group.
"""


def balanced_brackets(s: str) -> bool:
    # create containers, cursors, and or temp val holders
    opening_bracket_mapper = {")": "(", "]": "[", "}": "{"}
    bracket_stack = []

    # iterate through string
    for bracket in str:
        if bracket in opening_bracket_mapper.keys():
            if bracket_stack and (bracket_stack.pop() != opening_bracket_mapper[bracket]):
                return False
            else:

                bracket_stack.append(bracket)
        else:
            bracket_stack.append(bracket)
    if bracket_stack:
        return False
    else:
        return True
