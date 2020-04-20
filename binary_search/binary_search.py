def binary_search(list,key):
    low = 0
    high = len(list)-1
    mid = (high +low)//2
    while(high>=low):
        if list[mid]==key:
            return True
        elif list[mid]<key:
            low = mid+1
        else:
            high = mid-1
    return False


print(binary_search([1,4,54,65,66,66,113,165,201],33))
