with open("../Upload Documents/scrambled.jpg", "rb") as f:
    file = f.read()

print(len(file))

# Format PNG into columns of five: 1 - 16 | 1, 2, 3, 4, 5
arr = []
temp = []
for byte in file:
    temp.append(byte)
    if len(temp) == 5:
        arr.append(temp)
        temp = []

arr2 = []
for i, row in enumerate(arr):
    temp = [0, 0, 0, 0, 0]
    if i % 2 == 0:
        temp[0] = row[2]
        temp[1] = row[3]
        temp[2] = row[4]
        temp[3] = row[0]
        temp[4] = row[1]
    else:
        temp[0] = row[4]
        temp[1] = row[0]
        temp[2] = row[1]
        temp[3] = row[2]
        temp[4] = row[3]
    arr2.append(temp)


# Do even odd row swap: 1, 2, 3, 4  -> 2, 1, 4, 3
evens = []
odds = []
for i, row in enumerate(arr2):
    if i % 2 == 0:
        evens.append(row)
    else:
        odds.append(row)


arr2 = []
for j, k in zip(odds, evens):
    arr2.append(j)
    arr2.append(k)

arr = []
for row in arr2:
    temp = [0, 0, 0, 0, 0]
    temp[0] = row[4]
    temp[1] = row[3]
    temp[2] = row[1]
    temp[3] = row[2]
    temp[4] = row[0]
    arr.append(temp)

binstr = b""
for i in arr:
    binstr += bytes([i[0]])
    binstr += bytes([i[1]])
    binstr += bytes([i[2]])
    binstr += bytes([i[3]])
    binstr += bytes([i[4]])

print(binstr)

with open("../../test.jpg", "wb") as f:
    f.write(binstr)