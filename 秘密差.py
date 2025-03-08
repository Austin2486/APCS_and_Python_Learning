num = input()
num_list = list(int(i) for i in str(num))
if len(num_list) % 2 == 1:
    a = sum(num_list[::2])
    b = sum(num_list[1::2])
else:
    a = sum(num_list[1::2])
    b = sum(num_list[::2])


ans = a-b
if ans < 0:
    ans = -(ans)
print(ans)