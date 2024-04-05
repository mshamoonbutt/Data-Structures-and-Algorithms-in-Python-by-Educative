class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

def is_match(opening, closing):
    return opening == '(' and closing == ')' or \
           opening == '[' and closing == ']' or \
           opening == '{' and closing == '}'

def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "([{":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
                break
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
                    break
        index += 1

    return s.is_empty() and is_balanced

# Test the function
print(is_paren_balanced("(([]))"))  # Should return True
print(is_paren_balanced("([]{})"))  # Should return True
print(is_paren_balanced("([)]"))    # Should return False
