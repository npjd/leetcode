# Enter your code here. Read input from STDIN. Print output to STDOUT

child_height = 90.25/100
mean = 0.675
std_dev = 0.065

distance = child_height-mean
ans = distance/std_dev

ans = round(ans, 2)

print(ans)