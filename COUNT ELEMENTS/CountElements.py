arr:int = [int(x) for x in input("Enter the elements:").split()]
evenCount, oddCount = 0,0
for i in range(len(arr)):
    if arr[i] & 1 == 0:
        evenCount += 1
    else:
        oddCount += 1
if evenCount > oddCount:
    print(0)
else:
    for i in range(len(arr)):
        arr[i] = -1
    print(arr)