for i in range (150):
    print(i)

for i in range (5,1001,5):
    print(i)

for i in range (0,101):
    if i % 10 == 0:
        print("coding dojo")
    elif i % 5 ==0:
        print ("coding")
    else :
        print (i)

sum = 0
for i in range (1,500001,2):
    sum += i
print (sum)

for i in range (2018,0,-4):
    print (i)

low = 3
hight =12
mult =4

for i in range (low,hight+1):
    if i % mult == 0:
        print (i)