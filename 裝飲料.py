watercup = int(input())
w1,w2,h1,h2 = map(int,input().split())
watervolum = list(map(int,input().split()))

W1 = w1 * w1 * h1
W2 = w2 * w2 * h2

Hmax = 0
for i in watervolum:
    H = 0

    if W1 < 0 and W2 < 0:
        break

    elif W1 != 0:
        
        if i > (W1 + W2):
            H = (W1 // (w1 * w1)) + (W2 // (w2 * w2))

        elif i > W1:
            H = i - W1
            H = (W1 // (w1 * w1)) + (H // (w2 * w2))
            W1 = 0
            W2 = W2 - (i - W1)
        
        elif i < W1:
            H = i // (w1 * w1)
            W1 = W1 - i

        elif i == W1:
            H = (W1 // (w1 * w1))
            W1 = 0

    elif W1 == 0:
        
        if i > W2:
            H = W2 // (w2 * w2)
            W2 = 0
        
        elif i < W2:
            H = i // (w2 * w2)
            W2 = W2 - i
        
        elif i == W2:
            H = W2 // (w2 * w2)
            W2 = 0
            
    if Hmax < H:
        Hmax = H
print(Hmax)