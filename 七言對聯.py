#https://zerojudge.tw/ShowProblem?problemid=g275

doble_line = int(input())

for i in range(doble_line):
    word = list(map(int,input().split()))
    word2 = list(map(int,input().split()))
    
    if (word[1] != word[3] and word[1] == word[5]) and\
       (word2[1] != word2[3] and word2[1] == word2[5]):
        ans1 = None
    else:
        ans1 = 'A'
    if word[6] == 1 and word2[6] == 0:
        ans2 = None
    else:
        ans2 = 'B'
    if (word[1] != word2[1]) and\
       (word[3] != word2[3]) and\
       (word[5] != word2[5]):
        ans3 = None
    else:
        ans3 = 'C'
    
    if (ans1 == None) and\
       (ans2 == None) and\
       (ans3 == None):
        print('None')
    else:
        result = [x for x in (ans1, ans2, ans3) if x is not None]
        print("".join(result))
