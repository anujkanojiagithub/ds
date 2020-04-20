from stack_implementation import stack

s = stack()
with open('dummy_file.txt') as f:
    for i in f:
        s.push(i.rstrip('\n'))

with open('file_to_insert.txt','w') as f:
    while not s.is_empty():
        f.write(s.pop()+'\n')
