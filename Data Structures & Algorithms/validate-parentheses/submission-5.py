class Solution:
    def isValid(self, s: str) -> bool:

        if s == "":
            return True
        
        dict_order = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        my_stack = []

        for c in s:
            if c in dict_order.values():
                my_stack.append(c)

            else:
                if not my_stack:
                    return False

                if dict_order[c] != my_stack[-1]:
                    return False

                trash = my_stack.pop()

        return not my_stack

                    