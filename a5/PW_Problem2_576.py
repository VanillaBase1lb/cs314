def correct(s):
    i = 0
    for j in range(len(s)):
      if s[j] == '1':
          i = i + j + 1
    if i % (n + 1) == 0:
        return True
    else:
        return False  


n = int(input())

while(True):
    s = input()
    if s == '':
        exit()
    if len(s) == n:
        i = 0
        for j in range(n):
            if s[j] == '1':
                i = i + j + 1
        if i % (n + 1) != 0:
            rem = i % (n + 1)
            while s[rem - 1] != '1':
                rem = rem + n + 1
            s = s[:rem - 1] + '0' + s[rem:]
        print(s)
    
    elif len(s) < n:
        for i in range(len(s)):
            s1 = s[:i] + '1' + s[i:]
            if correct(s1):
                print(s1)
                break
            s2 = s[:i] + '0' + s[i:]
            if correct(s2):
                print(s2)
                break
    
    elif len(s) > n:
        for i in range(len(s)):
            s1 = s[:i] + s[i + 1:]
            if correct(s1):
                print(s1)
                break
