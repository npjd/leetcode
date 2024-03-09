# Enter your code here. Read input from STDIN. Print output to STDOUT
def std_dev(arr):
    mean = sum(arr) / len(arr)
    sigma = 0
    for num in arr:
        sigma += (num-mean)**2
    return (sigma/len(arr))**0.5
    
A = [1, 2, 3]
stdA = std_dev(A)
print(stdA)
mn = float('inf')
N = 0
possible_sols = range(-100000, 300000)
possible_sols = map(lambda x: x/10000, possible_sols)
for i in possible_sols:

    B = [1, 2, 3, i]
    stdB = std_dev(B)
    if (abs(stdA - stdB) <= mn):
        mn = abs(stdA - stdB)
        N = i

print( str(round(N,2)))
