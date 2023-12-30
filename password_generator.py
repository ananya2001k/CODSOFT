#Task 3- Program to create a password generator application using python
import random
print("*****Here's your password generator*****")
print("Enter the length of the password:")
length=int(input())
print("Choose the complexity of the password:")
print("1. Only alphabets\n2. Both alphabets and numbers\n3. Alphabets, numbers and symbols")
ch=int(input())
alphabets="a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
numbers="1 2 3 4 5 6 7 8 9"
symbols="~ ! @ # $ % ^ & * ( ) _ + { [ ] } - /"
#converting string to list 
alphabets=alphabets.split(" ")
numbers=numbers.split(" ")
symbols=symbols.split(" ")
password_list=[] #created list to use shuffle method
match ch:
    case 1:
        for i in range(length):
            password_list=password_list+list(random.choice(alphabets))
    case 2:
        print("Enter the number of alphabets:")
        alpha=int(input())
        print("Enter the number of digits:")
        dig=int(input())
        for i in range(alpha):
            password_list=password_list+list(random.choice(alphabets))
        for i in range(dig):
            password_list=password_list+list(random.choice(numbers))
        random.shuffle(password_list)
    case 3:
        print("Enter the number of alphabets:")
        alpha=int(input())
        print("Enter the number of digits:")
        dig=int(input())
        print("Enter the number of symbols:")
        sym=int(input())
        for i in range(alpha):
            password_list+=list(random.choice(alphabets))
        for i in range(dig):
            password_list+=list(random.choice(numbers))
        for i in range(sym):
            password_list+=list(random.choice(symbols))
        random.shuffle(password_list)
    case _:
        print("Wrong option chosen for complexity of the password")
#converting list to string for simplied output
password=""
for char in password_list:
    password+=char
print("Your password is:",password)