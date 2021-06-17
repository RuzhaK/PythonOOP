def reverse_text(s):
    i=len(s)-1
    while i>=0:
        yield s[i]
        i-=1

for char in reverse_text("step"):
    print(char, end='')
