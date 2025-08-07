def parentheses(n):
    result = []
    
    def backtrack(made_parentheses, open, close):
        if len(made_parentheses) == 2*n:
            result.append(made_parentheses)
            return
        
        if open < n:
            backtrack(made_parentheses + "(", open + 1, close)

        if close < open:
            backtrack(made_parentheses + ")", open, close + 1)

    backtrack("", 0, 0)
    return result

print(parentheses(3))