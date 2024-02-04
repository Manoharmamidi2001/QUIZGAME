print()
print("WELCOME TO QUIZ")
print()
print("note**In this quiz 4 quetions are there, for each quetion 4 options are given (A, B, C, D). From these options you have to pick the one correct option.\n")
print("-->For one right answer you will get 1 point.\n")
print("-->If you pick the wrong answer you will not get any point.\n")
print("ALL THE BEST")
def qz(n,c):
    if n==1:
        print()
        print("1) In which year india got independence?")
        print()
        print('''
    A) 1932

    B) 1901

    C) 1947

    D) 1928''')
        print()
        ans=input("Choose the correct option A, B, C or D : ")
        print()
        ans=ans.upper()
        if ans=='C':
            print("Hurray, 1947 is right answer")
            print()
            c+=1
        elif ans=='A' or ans=='B' or ans=='D':
            print("Wrong answer")
            print()
            print("Correct answer is 1947")
        else:
            print("Please Enter only A, B, C or D")
            qz(n,c)

    if n==2:
        print()
        print("2) How many times indian cricket team won world cup?")
        print()
        print('''
    A) 4

    B) 2

    C) 6

    D) 3''')
        print()
        
        ans=input("Choose the correct option A, B, C or D : ")
        print()
        ans=ans.upper()
        if ans=='B':
            print("Hurray, 2 is the right answer")
            c+=1
        elif ans=='A' or ans=='C' or ans=='D':
            print("Wrong answer")
            print()
            print("Correct answer is 2")
        else:
            print("Please Enter only A, B, C or D")
            qz(n,c)
    
    if n==3:
        print()
        print("3) Who is the present captain of indian cricket team?")
        print()
        print('''
    A) Rohit sharma

    B) M.S Dhoni

    C) Virat kohli

    D) Sachin Tendulkar''')
        print()
        
        ans=input("Choose the correct option A, B, C or D : ")
        print()
        ans=ans.upper()
        if ans=='A':
            print("Hurray, Rohit sharma is the right answer")
            c+=1
        elif ans=='B' or ans=='C' or ans=='D':
            print("Wrong answer")
            print()
            print("Correct answer is Rohit sharma")
        else:
            print("Please Enter only A, B, C or D")
            qz(n,c)
    
    if n==4:
        print()
        print("4) Who is the present prime minister of india?")
        print()
        print('''
    A) Sonia gandhi

    B) Rahul gandhi

    C) Manmohan singh

    D) Narendra modi''')
        print()
        
        ans=input("Choose the correct option A, B, C or D : ")
        print()
        ans=ans.upper()
        if ans=='D':
            print("Hurray, Narendra modi is the right answer")
            c+=1
        elif ans=='A' or ans=='C' or ans=='B':
            print("Wrong answer")
            print()
            print("Correct answer is Narendra modi")
        else:
            print("Please Enter only A, B, C or D")
            qz(n,c)
        
    return c

c=0
for i in range(1,5):
    c= qz(i,c)

print()
print("Your total Score is : ",c)