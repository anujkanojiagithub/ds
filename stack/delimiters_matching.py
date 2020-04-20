from stack_implementation import stack

def delimiter_matching(exp):
    lefty = '([{'
    righty = ')]}'
    s = stack()
    for c in exp:
        if c in lefty:
            s.push(c)
        elif c in righty:
            if s.is_empty():
                return False
            if righty.index(c) != lefty.index(s.pop()):
                return False
    return s.is_empty()


print(delimiter_matching(r'{{}{()}}}'))