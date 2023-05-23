def BalanceParenthesis(string):
    counter = 0
    stack = []
    index = 0
    while index < len(string)-1:
        if  string[index] == "(":
            stack.append("(")
        if string[index] == ")" and len(stack) > 0:
            if stack[-1] != "(":
                return False
            else:
                stack.pop()
        
        index += 1
        counter += 1

    if counter == len(string):
        return True

print(BalanceParenthesis("(())"))
print(BalanceParenthesis("(()))"))
print(BalanceParenthesis("(()))))"))

