def is_isogram(string):
    string=string.replace(" ", "")
    string= string.replace("-","")
    string=string.lower()
    a=list(string)
    if len(a)!= len(set(a)):
        return False
    else:
        return True