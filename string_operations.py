# Create a function to perform basic arithmetic operations that includes addition, subtraction, multiplication and division on a string number (e.g. "12 + 24" or "23 - 21" or "12 // 12" or "12 * 21").

# Here, we have 1 followed by a space, operator followed by another space and 2. For the challenge, we are going to have only two numbers between 1 valid operator. The return value should be a number.

# eval() is not allowed. In case of division, whenever the second number equals "0" return -1.

def arithmetic_operation(n):
    try:
        op = {'+': lambda x, y: x + y,'-': lambda x, y: x - y,'//': lambda x,y: x//y, '*': lambda x,y: x*y}
        ans = n.split( )
        return op[ans[1]](int(ans[0]),int(ans[2]))
    except ZeroDivisionError as e:
        return -1




ans= arithmetic_operation("12 // 0")

print(ans)