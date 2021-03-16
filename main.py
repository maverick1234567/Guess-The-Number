'''def is_leap(year):
    leap = False

    if (year % 4 == 0):
        leap = True
        if (year % 100 == 0):
            leap = False
            if (year % 400 == 0):
                leap = True
    return leap

year= int(input())
print(is_leap(year))'''

#a= int(input(""))
#if (1<=a<=151):
    #print(a)

'''a= int(input())
l= list()
for i in range(1<=a<=150):
        l.append(i**1)
print(*l)'''


'''def print_function():
        if n>-6 and n<93:
                while(i > n):
                        print(n, end=" ")
                n=n+1

a=int(input(""))
print(print_function())'''

'''a=int(input())
l= list()
for i in range(a>1 and a<150):
        print(a)'''



'''def function():
        print(*range(1, int(input()) + 1), sep='')

function()'''




'''a=float(input("enter the mealcost\n"))
b=int(input("entert the tipPercent\n"))
c=int(input("enter the taxPercent\n"))

d = round(a * b/100);
e = round(a *  c/100);
totalCost = int(a + d + e)
print(totalCost)'''



'''c=print(int(n*(i)))
c1=int(n*(i*2))
c2=int(n*(i*3))
c3=int(n*(i*4))
c4=int(n*(i*5))
c5=int(n*(i*6))
c6=int(n*(i*7))
c7=int(n*(i*8))
c8=int(n*(i*9))
c9=int(n*(i*10))


print(c)
print(c1)
print(c2)
print(c3)
print(c4)
print(c5)
print(c6)
print(c7)
print(c8)
print(c9)'''

'''n= int(input())
for i in range (1,11):
    print (str(n)+" x "+str(i)+" = "+str(i*n))'''

'''n = int(input(""))

if n%2==0 and (n in range(2,6) or n>20 ):
    print("Not Weird")
else:
    print("Weird")'''

'''print("Age is not valid, setting age to 0.")
a= int(input())
b= int(input())
c= int(input())
d= int(input())
e= int(input())
if a<13 and b<13 and c<13 and d<13 and e<13:
        print("you are young")
if (a>=13 and a<18) or (b>=13 and b<18) or (c>=13 and c<18) or (d>=13 and d<18) or (e>=13 and e<18):
        print("you are teenager")
else:
        print("you are old")'''

'''print("Age is not valid, setting age to 0.")
n= int(input())
i= int(input())
for i in range(0,n):
        for i in range(0,i):
                if n<13:
                        print("you are young\n")
                elif n<13 and n>=18:
                        print("you are teenager\n")
                else:
                        print("you are old\n")'''

'''def amIOld(self):
        if self.age in range(13):
            print("You are young.")
        elif self.age in range(13, 18):
            print("You are a teenager.")
        else:
            print("You are old.")

a= int(input())
amIOld(self)'''

'''i =1
a= int(input())
while(True):
        if i<a:
                continue


        print(i, end=" ")
        if i==45:
                break
        i = i + 1'''



'''n=18
number_of_guesses=1
print("Number of guesses is limited to only 9 times: ")
while (number_of_guesses<=9):
    guess_number = int(input("Guess the number :\n"))
    if guess_number<18:
        print("you enter less number please input greater number.\n")
    elif guess_number>18:
        print("you enter greater number please input smaller number.\n ")
    else:
        print("you won\n")
        print(number_of_guesses,"no.of guesses he took to finish.")
        break
    print(9-number_of_guesses,"no. of guesses left")
    number_of_guesses = number_of_guesses + 1

if(number_of_guesses>9):
    print("Game Over")'''

'''n= 18
number_of_guesses=1
print("number of guesses is 9")
while(number_of_guesses <=9):
        guess_number= int(input("enter the guess_number\n"))
        if guess_number<18:
                print("enter the higher number")
        elif guess_number>18:
                print("enter lower number")
        else:
                print("congrats you won")
                print(number_of_guesses,"no.of guesses he took to finish.")
                break
        print(9 - number_of_guesses, "no. of guesses left")
        number_of_guesses= number_of_guesses + 1
if number_of_guesses<9:
        print("game over")'''

#print("5 + 8","=", 5+8)

n= 18
number_of_guesses= 1
print("you only have 9number of guesses")
while(number_of_guesses <=9):
        guess_number= int(input("enter the guess number\n"))
        if guess_number<18:
                print("enter lower number\n")
        elif guess_number>18:
                print("print higher number\n")
        else:
                print("you won")
                print(number_of_guesses,"the number of guesses left")
                break
        print(9-number_of_guesses, "the number_of_guesses of guess left is:")
        number_of_guesses= number_of_guesses + 1
if(number_of_guesses>9):
        print("game over")

'''def rohit():
        number_1=int(input("enter the number\n"))
        if number_1>18:
                print("rohit")
        else:
                print("rohit ()")
rohit()'''












