def delete(list_, index=None):
    if index is not None:
        a = list_[:index] + list_[index+1:]
    else:
        a = list_[:-1]
    return a


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
