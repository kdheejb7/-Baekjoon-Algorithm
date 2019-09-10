number = int(input())
w = [0,0,1,1]
if number >= 4: 
    for i in range(4, number+1):
        if i % 6 == 0:
            w.append(min(w[i-1], w[i//2], w[i//3])+1)
        elif i % 2 == 0:
            w.append(min(w[i-1], w[i//2])+1)
        elif i % 3 == 0:
            w.append(min(w[i-1], w[i//3])+1)
        else:
            w.append(w[i-1]+1)
print(w[number])
