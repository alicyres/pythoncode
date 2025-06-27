num1 = [1,2,3,0,0,0,0,0]
num2 = [2,5,6,3]

# sefr_count = num1.count(0)
# print(sefr_count)

while 0 in num1:
    num1.remove(0)
    
num1.extend(num2)
num1.sort()
print(num1)