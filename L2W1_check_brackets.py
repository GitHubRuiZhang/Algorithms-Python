# Uses python3
# Find errors in the usage of brackets in the code
# Brackets: []{}(), they must appear in pair, [{( must be in the left side of }})
# Input: string s
# Output:
# "Success" if correct, otherwise the first unmatched closing bracket

# Example:
# Input:[]
# Output:
# Success

# Example:
# Input: {}[]
# Output:
# Success

# Example:
# Input: [()]
# Output:
# Success

# Example:
# Input: (())
# Output:
# Success

# Example:
# Input: {[]}()
# Output:
# Success

# Example:
# Input: {
# Output:
# 1

# Example:
# Input: {[}
# Output:
# 3
# Explanation:
# } is unmatched because [ hasn't been matched

# Example:
# Input: foo(bar)
# Output:
# Success

# Example:
# Input: foo(bar[i)
# Output:
# 10
# Explanation:
# ) is unmatched because [ hasn't been matched

# Solution Methods:
#


class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False


text = list(input())
opening_brackets_stack = []
for i, next in enumerate(text):
    if next == '(' or next == '[' or next == '{':
        opening_brackets_stack.append(Bracket(next, i))
    elif next == ')' or next == ']' or next == '}':
        if not opening_brackets_stack:
            print(i + 1)
            break
        opening_brackets = opening_brackets_stack[len(opening_brackets_stack) - 1]
        if opening_brackets.Match(next):
            opening_brackets_stack.pop()
        else:
            print(i + 1)
            break

    if i == len(text) - 1:
        if not opening_brackets_stack:
            print('Success')
        else:
            print(opening_brackets_stack[0].position + 1)
