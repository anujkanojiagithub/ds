def binary_search(a , key , low ,high):
    if low>high:
        return False
    else:
        mid = (low + high) // 2
        if a[mid] == key:
            return True
        elif a[mid]<key:
            return binary_search(a,key,mid+1,high)
        else:
            return binary_search(a, key, low , mid-1)
abc = [1,12,345,555,675,4566,5678]
print(binary_search(abc,12,0,len(abc)))