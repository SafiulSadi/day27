x = input()
y = (x.split())
arr = []
for i in y:
    arr.append(int(i))

count1 = 0
if arr[0] == arr[1]:
    count1 += 1
if arr[0] == arr[2]:
        count1 += 1
if arr[0] == arr[3]:
            count1 += 1
if arr[1] == arr[2] and not arr[0] == arr[2]:
    count1 +=1
if arr[1] == arr[3] and not arr[0] == arr[3]:
    count1 += 1
if arr[2] == arr[3] and not arr[0] == arr[3] and not arr[1] == arr[3]:
    count1 += 1
if count1 > 4:
    count1 = 4
print(count1)
