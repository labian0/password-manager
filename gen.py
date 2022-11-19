from random import randrange

def gen_password(length:int=8,lower=True, upper=True, digits=True):
    args = [lower,upper,digits]
    chars = ["abcdefghijklmnopqrstuvwxyz","ABCDEFGHIJKLMNOPQRSTUVWXYZ","0123456789"]#62 chars
    if not True in args:#if none of the char types are selected
        return
    while False in args:
        for i in range(2):
            if not args[i]:
                del args[i]
                del chars[i]
                break
    chars = str().join(chars)
    
    pw = str()

    for i in range(length):
        pw+=chars[randrange(len(chars))]
    return pw

    


password = gen_password(length=16)
print(password)