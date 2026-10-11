'''
Q.1) WAT a program to count no.of digits in a number 
'''

# num = abs(int(input("enter a number:")))
# count = 0

# if num == 0:
#     count = 1
# else:
#     while num > 0:
#         count += 1
#         num //=10


# print("Number of digits:",count)


'''
  Q.2) wap a program to reverse a number
'''


num = int(input("enter a number:"))
reverse = 0

while num > 0:
   digit = num % 10
   reverse = reverse * 10 + digit
   num = num // 10

  
print("Reversed number :",reverse) 