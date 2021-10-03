with open("scrambledeggs.jpg", "rb") as f:
    file = f.read()

# Append null bytes so that bytes can be manipulated properly in columns of five.
while len(file) % 5 != 0:
    file += b"\x00"

print(len(file))

# Format PNG into columns of five: 1 - 16 | 1, 2, 3, 4, 5
arr = []
temp = []
for i, byte in enumerate(file):
    temp.append(byte)
    if len(temp) == 5:
        arr.append(temp)
        temp = []


print(len(arr) * 5)

# Do column swap: 1, 2, 3, 4, 5  ->  5, 3, 4, 2, 1
arr2 = []
for row in arr:
    temp = [0, 0, 0, 0, 0]
    temp[0] = row[4]
    temp[1] = row[2]
    temp[2] = row[3]
    temp[3] = row[1]
    temp[4] = row[0]
    arr2.append(temp)

print(len(arr2) * 5)

# Do even odd row swap: 1, 2, 3, 4  -> 2, 1, 4, 3
evens = []
odds = []
for i, row in enumerate(arr2):
    if i % 2 == 0:
        evens.append(row)
    else:
        odds.append(row)
arr = []
for j, k in zip(evens, odds):
    arr.append(k)
    arr.append(j)

print(len(arr) * 5)

# Do even odd row shifts: O <- 1 | E -> 2
arr2 = []
for i, row in enumerate(arr):
    temp = [0, 0, 0, 0, 0]
    if i % 2 == 0:
        temp[0] = row[3]
        temp[1] = row[4]
        temp[2] = row[0]
        temp[3] = row[1]
        temp[4] = row[2]
    else:
        temp[0] = row[1]
        temp[1] = row[2]
        temp[2] = row[3]
        temp[3] = row[4]
        temp[4] = row[0]
    arr2.append(temp)

print(len(arr2) * 5)

# Convert ints to bytes
binstr = b""
for i in arr2:
    binstr += bytes([i[0]])
    binstr += bytes([i[1]])
    binstr += bytes([i[2]])
    binstr += bytes([i[3]])
    binstr += bytes([i[4]])

print(len(binstr))

with open("Challenge Items/Upload Documents/scrambled.jpg", "wb") as j:
    j.write(binstr)