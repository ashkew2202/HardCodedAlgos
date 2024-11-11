import numpy as np

seq1 = input("type in the seq1: ")
seq2 = input("type in the seq2: ")

nseq1 = len(seq1)
nseq2 = len(seq2)

gap = 1
match = 1
mismatch = 1

# Optimal score at each possible pair of characters.
matrix = np.zeros((nseq1 + 2, nseq2 + 2))
for i in range(nseq1 + 1):
    matrix[i+1][0] = -2*(i+1)*gap
for j in range(nseq2 + 1):
    matrix[0][j+1] = -2*(j+1)*gap

# Reference matrix to trace through an optimal aligment.
P = np.zeros((nseq1 + 1, nseq2 + 1))
P[:,0] = 3
P[0,:] = 4

# Temporary scores.
t = np.zeros(3)
for i in range(nseq1):
    for j in range(nseq2):
        if seq1[i] == seq2[j]:
           t[0] = matrix[i,j] + match
        else:
            t[0] = matrix[i,j] - mismatch
        t[1] = matrix[i,j+1] - 2*gap
        t[2] = matrix[i+1,j] - 2*gap
        tmax = np.max(t)
        matrix[i+1,j+1] = tmax
# 2 is for diagonals, 3 is for top value, 4 is for left value
        if t[0] == tmax:
            P[i+1,j+1] = 2
        if t[1] == tmax:
            P[i+1,j+1] = 3
        if t[2] == tmax:
            P[i+1,j+1] = 4
print(P)
print(matrix)

# Trace through the optimal alignment which starts from bottom right corner.
i = nseq1
j = nseq2
rx = []
ry = []
while i > 0 or j > 0:
    if P[i,j] in [2, 5, 6, 9]:
        rx.append(seq1[i-1])
        ry.append(seq2[j-1])
        i -= 1
        j -= 1
    elif P[i,j] in [3, 5, 7, 9]:
        rx.append(seq1[i-1])
        ry.append('-')
        i -= 1
    elif P[i,j] in [4, 6, 7, 9]:
        rx.append('-')
        ry.append(seq2[j-1])
        j -= 1

# Reverse the strings because while using the pointer matrix they were made reversed
rx = ''.join(rx)[::-1]
ry = ''.join(ry)[::-1]
print(rx)
print(ry)

