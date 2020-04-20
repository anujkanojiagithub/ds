def linear_search(a,key):
    flag = False
    index = 0
    while index <len(a) and not flag:
        if a[index]==key:
            flag = True
        index = index+1
    return flag

print(linear_search([132,123,22,313,4,13,2424,5,1],132))