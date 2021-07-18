'''
Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''
def appendZero(s,n):
    for i in range(n):
        s+='0'
    return s
def addBinary(a,b):
    na = len(a)
    nb = len(b)
    res=''
    if ( na < nb ):
        a=appendZero(a,nb-na)
    else:
        b=appendZero(b,na-nb)
    carry=0
    print("A",a)
    print("B",b)
    for i in range(len(a)):
        xor = int(a[i]) ^ int(b[i]) ^ carry
        carry = (int(a[i]) & int(b[i])) | (int(b[i]) & carry) | (int(a[i]) & carry)
        res+=str(xor)

    return res
        

print(addBinary('1010','1011'))