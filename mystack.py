#!/usr/bin/python
class MyStack:
    def __init__(self):
        self.stackList=[]

    def push(self,item):
        self.stackList.append(item)

    def pop(self):
        return self.stackList.pop()

    def is_empty(self):
        return (self.stackList==[])

def postfix(expr):
    import re
    token_list = re.split("([^0-9])",expr)
    stack = MyStack()
    for token in token_list:
        if token == "" or token == " ":
            continue
        if token == "+":
            sum = stack.pop() + stack.pop()
            stack.push(sum)
        elif token == "*":
            product = stack.pop() * stack.pop()
            stack.push(product)
        else:
            stack.push(int(token))
    return stack.pop()
if __name__=='__main__':
	a=postfix("123 456 + 2 *")
	print a