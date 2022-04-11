#!/usr/bin/env python
# coding: utf-8

# In[7]:


little_mermaid = 3
brother_bear = 5
hercules = 1

movies = [little_mermaid, brother_bear, hercules]
print(movies)
price = 3
rentals = 0

for days in movies:
   rentals += days * price
print(rentals)


# In[12]:


google = 400
amazon = 380
facebook = 350
hourly_rate = [google, amazon, facebook]
hours_worked = [6, 4, 10]
weeks_pay = 0

for hours in hours_worked:
    for rate in hourly_rate:
        weeks_pay += rate * hours
print(weeks_pay)


# In[52]:


google = 400
amazon = 380
facebook = 350
hourly_rate = [google, amazon, facebook]
hours_worked = [6, 4, 10]
weeks_pay = []

weeks_pay = hourly_rate[1] * hours_worked[1]


# In[27]:


student_enrolled = True
full_class = False
class_schedule = True
current_schedule = False
student_enrolled != full_class and (class_schedule != current_schedule)


# In[59]:


google = 400
amazon = 380
facebook = 350
hourly_rate = [google, amazon, facebook]
hours_worked = [6, 4, 10]
weeks_pay = []

weeks_pay = hourly_rate[0] * hours_worked[0] + hourly_rate[1] * hours_worked[1] + hours_worked[2] * hourly_rate[2]
print(weeks_pay)


# In[69]:


password_at_least_5_char = True
username_more_than_20_char = False
password_is_username = False

proper_username_and_password = password_at_least_5_char and not username_more_than_20_char and not password_is_username
print(proper_username_and_password)


# In[80]:


hours_worked = [30, 50]
hourly_wages = 20
weekly_wages = [h * hourly_wages for h in hours_worked]
print(weekly_wages)


# In[82]:


hours_worked = [30, 50]
hourly_wages = 20
weekly_wages = [h * hourly_wages for h in hours_worked]
print(weekly_wages)

for h in hours_worked:
    if h > 40:
        weekly_wages = [h * hourly_wages *1.5 for h in hours_worked]
    else:
        weekly_wages = [h * hourly_wages for h in hours_worked]
print(weekly_wages)


# In[93]:


i = 5

while i <= 15:
    print(i)
    i += 1


# In[96]:


n = 0

while n <= 100:
    print(n)
    n += 2


# In[97]:


n = 100

while n >= -10:
    print(n)
    n += -5


# In[101]:


n = 2

while n < 1000000:
    print(n)
    n = n * n


# In[102]:


n = 100

while n >= 5:
    print(n)
    n += -5


# In[126]:


number = int(input("Enter a number. "))

for n in range(1, 11):
    print(f'{number} x {n} = {n * number}')
    


# In[144]:


for n in range(1, 10):
    print(f'{n * (10**(n-1))}')


# In[ ]:


number = input("Enter an odd number between 1 and 50, ")

d = number.isdigit()
print(d)
while d =:
    input("Try again")

for n in range(1, 51):
    if n % 2 == 0:
        continue
    print(f'Here is an odd number: {n}')


# In[155]:





# In[163]:


for n in range(1, 101):
    print(n)
    n += 1


# In[174]:


for n in range(1, 101):
    if n % (3 * 5) == 0:
        print("FizzBuzz")


# In[194]:


integer = int(input("Enter a integer. "))

print("number |"+" squared |"+" cubed")
for n in range(1, (integer+1)):
    print(str(n) + "      |"+ str(n**n)+ "       |"+ str(n**n**n))

cont = input("Do you want to continue?")


# In[219]:


grade = int(input("Enter grade from 0-100, "))
A = list(range(88, 101))
B = list(range(80, 88))
C = list(range(67, 80))
D = list(range(60, 67))
F = list(range(60))
grade_ranges = [A, B, C, D, F]

print(grade_ranges)

(input("Please continue, "))


# In[230]:


user_genre = input("Enter a genre, ")

for book in books_read:
     if book['genre'] == user_genre:
            print("Title: "+ book['title'])
            print("Author: "+ book['author'])
            print("Genre: "+book['genre'])


# In[226]:


beginning_book = ["Start", 'Sally', 'mystery']
middle_book = ["Continue", 'Billy', 'adventure']
ending_book = ["Finish", 'Tommy', 'horror']

beginning_book = {'title': "Start", 'author': 'Sally', 'genre': 'mystery'}
middle_book = {'title': "Continue", 'author': 'Billy', 'genre': 'adventure'}
ending_book = {'title': "Finish", 'author': 'Tommy', 'genre': 'horror'}

books_read = [beginning_book, middle_book, ending_book]

for book in books_read:
    print("Title: "+ book['title'])
    print("Author: "+ book['author'])
    print("Genre: "+book['genre'])


# In[221]:


student_0 = [1, 'joe', 89]
student_1 = [2, 'arsene', 87]
student_2 = [3, 'kayla', 88]


student_0 = {
    'id':1,
    'name':'joe',
    'grades':[99, 100]
    }

student_1 = {
    'id':2,
    'name':'arsene',
    'grades': [87, 88, 89, 90, 91]
}

student_2 = {
    'id':3,
    'name':'kayla',
    'grades':[88, 89]
}

list_of_students = [student_0, student_1, student_2]

#easy_grade_sum = sum_of_student_0_and_1+ list_of_students[2]['grade']


for student in list_of_students:
    print(student['name'])
    print(student['grades'])
    sum_of_grades_for_student = 0


# In[251]:


pos = input("Enter an positive number: ")
pos.isdigit()
pos = int(pos)

for x in range(pos):
    x = x+1
    if x > 0:
        print(str(x)+' is positive')
    


# In[238]:


#The input function can be used to prompt for input and use that input in your python code. 
#Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
#(Hints: first make sure that the value the user entered is a valid number, 
#also note that the input function returns a string, so you'll need to convert this to a numeric type


# In[254]:


#Write a program that prompts the user for a positive integer. 
#Next write a loop that prints out the numbers from the number the user entered down to 1
pos = input("Enter an positive number: ")
pos.isdigit()
pos = int(pos)

for x in range(pos):
    x = x+1
    if x > 0:
        x = pos - (x-1)
        print(str(x)+' is positive')
        
        


# In[258]:


odd = input("Enter an odd number between 1 and 50, ")
odd.isdigit()

odd = int(pos)



for n in range(1, 51):
    if n % 2 == 0:
        continue
    print(f'Here is an odd number: {n}')


# In[383]:


print("number |"+" squared |"+" cubed")
for n in range(1, (integer+1)):
    print(str(n) + "      |"+ str(n**n)+ "       |"+ str(n**n**n))

cont = input("Do you want to continue? Yes or No, ")

if cont == 'Yes':
    integer = int(input("Enter an integer, "))
    print("number |"+" squared |"+" cubed")
    for n in range(1, (integer+1)):
        print(str(n) + "      |"+ str(n**n)+ "       |"+ str(n**n**n))
else:
    print('Thanks for playing')


# odd = input("Enter an odd number between 1 and 50, ")
# odd.isdigit()
# 
# odd = int(odd)
# 
# if odd > 0 and odd <= 50 and odd % 2 == 1:
#      print(str(odd) + ' is odd, greater than 0, and less than or equal 50')
# else:
#     odd = input("Enter another number")

# In[270]:


odd = input("Enter an odd number between 1 and 50, ")
odd.isdigit()

odd = int(odd)

if odd > 0 and odd <= 50 and odd % 2 == 1:
     print(str(odd) + ' is odd, greater than 0, and less than or equal 50')
else:
    odd = input("Enter another number")


# In[283]:


#5. Convert given number grades into letter grades.
# Prompt the user for a numerical grade from 0 to 100.
# Display the corresponding letter grade.
# Prompt the user to continue.
# Assume that the user will enter valid integers for the grades.
# The application should only continue if the user agrees to.
# Grade Ranges:

grade = int(input("Enter grade from 0-100, "))
A = list(range(88, 101))
B = list(range(80, 88))
C = list(range(67, 80))
D = list(range(60, 67))
F = list(range(60))

grade_ranges = [A, B, C, D, F]

if grade in grade_ranges[0]:
    print('Grade is A')
elif grade in grade_ranges[1]:
    print('Grade is B')
elif grade in grade_ranges[2]:
    print('Grade is C')
elif grade in grade_ranges[3]:
    print('Grade is D')
else:
    print('Grade is F')
    
    
cont = input("Would you like to continue? Yes or No, ")
if cont == 'Yes':
    grade = int(input("Enter grade from 0-100, "))
    if grade in grade_ranges[0]:
        print('Grade is A')
    elif grade in grade_ranges[1]:
        print('Grade is B')
    elif grade in grade_ranges[2]:
        print('Grade is C')
    elif grade in grade_ranges[3]:
        print('Grade is D')
    else:
        print('Grade is F')

else:
    print('Thanks for playing')


# In[290]:


integer = int(input("Enter an integer. "))

print("number |"+" squared |"+" cubed")
for n in range(1, (integer+1)):
    print(str(n) + "      |"+ str(n**n)+ "       |"+ str(n**n**n))

cont = input("Do you want to continue? Yes or No, ")

if cont == 'Yes':
    integer = int(input("Enter an integer, "))
    print("number |"+" squared |"+" cubed")
    for n in range(1, (integer+1)):
        print(str(n) + "      |"+ str(n**n)+ "       |"+ str(n**n**n))
else:
    print('Thanks for playing')


# In[ ]:


hours_worked = [30, 50]
hourly_wages = 20
weekly_wages = [h * hourly_wages for h in hours_worked]
print(weekly_wages)

for h in hours_worked:
    if h > 40:
        weekly_wages = [h * hourly_wages *1.5 for h in hours_worked]
    else:
        weekly_wages = [h * hourly_wages for h in hours_worked]
print(weekly_wages)

if h in hours_worked < 40


# In[308]:


hours_worked = [30, 50]
hourly_wages = 20
weekly_wages = [h * hourly_wages for h in hours_worked]


for h in hours_worked:
    if h < 40:
        h = [h * hourly_wages] 
    else:
        h = [h * hourly_wages * 1.5]
    print('Weekly wages are $' + str(h))


# In[309]:


hours_worked = [30, 50]
hourly_wages = 20
weekly_wages = [h * hourly_wages for h in hours_worked]


for h in hours_worked:
    if h < 40:
        h = [h * hourly_wages] 
    else:
        h = [h * hourly_wages * 1.5]
    print('Paycheck is $' + str(h))


# In[310]:


for n in range(1, 10):
    print(f'{n * (10**(n-1))}')


# In[314]:


for n in list(range(1, 10)):
    print(str(n)*n)


# In[318]:


# Prompt the user for an odd number between 1 and 50. 
# Use a loop and a break statement to continue prompting the user if they enter invalid input. 
# (Hint: use the isdigit method on strings to determine this). 
# Use a loop and the continue statement to output all the odd numbers between 1 and 50, 
# except for the number the user entered

odd = input("Enter an odd number between 1 and 50, ")
odd.isdigit()

odd = int(odd)

for n in odd:
    if odd.isdigit() == False:
        odd = input("Try entering an odd number again")
    elif:
        odd > 0 and odd <= 50 and odd % 2 == 1
        print(str(odd) + ' is odd, greater than 0, and less than or equal 50')
    else:
        print('Number is not odd.')


# In[323]:


# Prompt the user for an odd number between 1 and 50. 
# Use a loop and a break statement to continue prompting the user if they enter invalid input. 
# (Hint: use the isdigit method on strings to determine this). 
# Use a loop and the continue statement to output all the odd numbers between 1 and 50, 
# except for the number the user entered

odd = input("Please enter an odd number from 1 to 50, ")

for n in odd:
    if odd.isdigit() == False:
        odd = input('Please try again using numbers only, ')
    elif odd.isdigit() == True:
        break


# In[327]:


odd = input("Please enter an odd number from 1 to 50, ")

for n in odd:
    if odd.isdigit() == False:
        odd = input('Please try again using numbers only, ')
    elif odd.isdigit() == True:
        break

odd = int(odd)

if odd > 0 and odd <= 50 and odd % 2 == 1:
     print(str(odd) + ' is odd, greater than 0, and less than or equal 50')
else:
    odd = input("Enter another number")


# In[329]:


odd = input("Please enter an odd number from 1 to 50, ")

for n in odd:
    if odd.isdigit() == False:
        odd = input('Please try again using numbers only, ')
    elif odd.isdigit() == True:
        break

for n in odd:
    odd = int(odd)
    elif odd > 0 and odd <= 50 and odd % 2 == 1:
        print(str(odd) + ' is odd, greater than 0, and less than or equal 50')
    else:
        odd = input("Enter another number, ")


# In[375]:


odd = input("Please enter an odd number from 1 to 50, ")

for n in odd:
    if odd.isdigit() == False or int(odd) > 50 or int(odd) % 2 == 0:
        odd = input('Please try again using odd numbers only, ')
    elif odd.isdigit() == True:
        break
        
for n in range(1, 51):
    odd = int(odd)
    if n == odd:
        print('Yikes! Skipping number ' + str(odd))
    elif n % 2 == 0:
        continue
    else:
        print(f'Here is an odd number: {n}')


# In[377]:


pos = input("Enter an positive number: ")
pos.isdigit()
pos = int(pos)

for x in range(pos):
    x = x+1
    if x > 0:
        x = pos - (x-1)
        print(str(x)+' is positive')


# In[380]:


pos = input("Enter an positive number: ")
pos.isdigit()
pos = int(pos)

for x in range(pos):
    x = x+1
    if x >= 0:
        print(str(x)+' is positive')


# In[381]:


pos = input("Enter an positive number: ")
pos.isdigit()
pos = int(pos)

for x in range(pos):
    x = x+1
    if x > 0:
        print(str(x)+' is positive')


# In[341]:


for n in range(1, 51):
    print(type(n))


# In[371]:


number = int(input("Enter a number. "))

for n in range(1, 11):
    print(f'{number} x {n} = {n * number}')


# In[369]:


hours_worked = [30, 50]
hourly_wages = 50
weekly_wages = [h * hourly_wages for h in hours_worked]


for h in hours_worked:
    if h <= 40:
        h = [h * hourly_wages] 
    else:
        h = [h * hourly_wages * 1.5]
    print('Paycheck is $' + str(h))


# In[367]:


#d. The input function can be used to prompt for input and use that input in your python code. 
# Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
# (Hints: first make sure that the value the user entered is a valid number,
# also note that the input function returns a string, so you'll need to convert this to a numeric type.)
pos = input("Enter an positive number: ")
pos.isdigit()

for n in pos:
    if pos.isdigit() == False:
        pos = input('Please try again using positive numbers only, ')
    elif pos.isdigit() == True:
        break
        
pos = int(pos)


for x in range(pos):
    x = x+1
    if x > 0:
        print(str(x)+' is positive')


# In[364]:


odd = input("Please enter an odd number from 1 to 50, ")

for n in odd:
    if odd.isdigit() == False:
        odd = input('Please try again using odd numbers only, ')
    elif odd.isdigit() == True:
        break
        

