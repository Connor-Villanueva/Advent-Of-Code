def hasRepeatingSubsequence(id : int) -> bool:
    idStr = str(id)
    
    doubled = idStr + idStr
    return idStr in doubled[1:-1]

num = 123123123

print(hasRepeatingSubsequence(num))