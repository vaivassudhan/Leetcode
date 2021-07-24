def reverse(s):
    if(len(s)==1 or s==""):
        return s
    return reverse(s[1:])+s[0]
print(reverse("olleH"))