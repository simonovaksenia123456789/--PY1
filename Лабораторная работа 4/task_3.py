def delete(list_,index=None):
    if index == None:
        return list_[:-1]
    else:
        list1 = list_[:index]
        list2 = list_[index+1:]
        return list1+list2

print(delete([0,0,1,2], index=0))
print(delete([0,1,1,2,3], index=1))
print(delete([0,1,2,3,4,4]))

def delete(list_, index=None):
    if index != None:
        list_.pop(index)
    else:
        list_.pop()
    return list_

print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]