# leetcode 1903
import math

lst = []

def reminder_by_10(number):

    ans, rem = divmod(number, 10)

    if ans not in lst:
        lst.append(int(ans))
        reminder_by_10(ans)

    if rem not in lst:
        lst.append(int(rem))
        reminder_by_10(rem)

    return 0, 0


num = input("Enter number : ")
ls = [num]
tmp = list(num)
length = len(tmp)

lst.append(num)
lst[0] = int(lst[0])
rem_lst = []

#Creating substring form the String
for i in range(length):
    ans, rem = divmod(int(num), math.pow(10, i))
    rem_lst.append(int(rem))

    if rem not in lst:
        lst.append(int(rem))
    reminder_by_10(ans)

for i in range(len(rem_lst)):
    reminder_by_10(rem_lst[i])

#sorting list
lst.sort()
print(lst)
print("length is : ",len(lst))
large = 0

#Searching for largest odd number from list
for i in range(len(lst)):
    if large < lst[i] and lst[i] % 2 != 0:
        large = lst[i]

f_lst = [str(large)]
print(f_lst)
