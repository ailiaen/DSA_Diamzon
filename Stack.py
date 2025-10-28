class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        if self.top:
            new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        popped_node = self.top
        self.top = self.top.next
        popped_node.next = None
        return popped_node.data

    def peek(self):
        if self.top:
            return self.top.data
        return None

    def is_empty(self):
        return self.top is None

def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    right_associative = {'^'}
    stack = []
    output = []
    expression = expression.replace(" ", "")
    for char in expression:
        if char.isalnum():
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if stack and stack[-1] == '(':
                stack.pop()
        elif char in precedence:
            while stack and stack[-1] != '(':
                top = stack[-1]
                if (top in precedence and
                    ((char not in right_associative and precedence[top] >= precedence[char]) or
                     (char in right_associative and precedence[top] > precedence[char]))):
                    output.append(stack.pop())
                else:
                    break
            stack.append(char)
        else:
            continue
    while stack:
        output.append(stack.pop())
    return ''.join(output)
