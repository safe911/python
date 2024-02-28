evensum=0
oddsum=0
count=0
for i in range (1,101):
    if i % 2 ==0:
        count=count+1
        evensum=evensum+i
    else:
        oddsum=oddsum+i
        count=count+1
print (" 1부터 100까지의 짝수의 합계는: %d"  %evensum)
print (" 1부터 100까지의 홀수의 합계는: %d"  %oddsum)
