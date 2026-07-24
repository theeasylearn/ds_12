#  0   1   1   2   3   5   8   13  .... 1000
#      p   c   n 
#          p   c   n 
# p = previous c = current n = next 
previous = 0 
current = 1 
next = previous + current 
print(previous,end=' ')
print(current,end=' ')

while next<100:
    print(next,end=' ')
    previous = current 
    current = next 
    next = previous + current




