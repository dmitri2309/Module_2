n = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
def select(i):
    result = []
    for j in range(1,i):
        for y in range(j+1,i):
            k = j + y
            if i % k == 0:
                result.append(j)
                result.append(y)
            else:
                continue
    return result
for i in n:
    result = select(i)
    print(f"{i} - ",*result,sep='')