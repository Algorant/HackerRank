# Takes the 4 inputs in order
x, y, z, n = (int(input()) for _ in range(4))


# Create list and append the values to it
num_list = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if (i + j + k) != n:
                num_list.append([i,j,k])

# print list in format [i,j,k] values
print(num_list)
