n = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
password = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
result = [[]]
for i in n:
    for j in password:
        for y in password:
            result[i]  = []
            k = j + y
            if i % k == 0:
                if y and j not in result:
                    result[i].append(j)
                    result[i].append(y)
                    print(i,"-",*result)
            if k > i:
                break
            else:
                 continue




