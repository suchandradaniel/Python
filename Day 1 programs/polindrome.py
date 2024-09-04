def ispolindrome(s):
    return s==s[::1]
s=str(input("enter a name"))
ans= ispolindrome(s)
if ans:
    print("yes")
else:
    print("no")
