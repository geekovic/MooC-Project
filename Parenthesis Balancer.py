def is_balanced(s):
    #Function to check if a string of parentheses is balanced
    stack = []
    matching_parentheses = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in "({[":
            stack.append(char)  # Push opening brackets to the stack
        elif char in ")}]":
            # Check if stack is not empty and matches the last opened bracket
            if stack and stack[-1] == matching_parentheses[char]:
                stack.pop()  # Pop the matched opening bracket
            else:
                return False  # Mismatch or stack is empty

    return len(stack) == 0  # If stack is empty, it's balanced


# Main Execution
if __name__== "__main__":
    print("Parentheses Balancer")
    while True:
        flag = True
        string = input("\nEnter a string of parentheses (or type 'exit' to quit): ")
        for char in string:
            if char not in  "({[)]}":
                flag = False
                break
        if flag == False and string!='exit' :
            print("Enter Valid Parenthesis")
            continue
        if string.lower() == 'exit':
            print("Exiting program. Goodbye!")
            break
        if is_balanced(string):
            print("The string is balanced.")
        else:
            print("The string is not balanced.")
