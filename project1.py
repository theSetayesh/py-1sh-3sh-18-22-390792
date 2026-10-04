students=[
    [
        "Setayesh Aberoumand","Setayesh","1234",20,19,20,20
    ]
]

while True:
    print("\n1. Sign up")
    print("\n2. Sign in")
    print("\n3. exit")

    choice=input("\n enter number: ")

    match choice :
        case"1":
            print("\n SIGN UP")
            name=input("name: ")
            username=input("username: ")
            password=input("password: ")
            python=float(input("python: "))
            java=float(input("java: "))
            html=float(input("html: "))
            js=float(input("js: "))

            student=[name,username,password,python,java,html,js]

            students.append(student)

            print("\n Sign up SUCCESSFULLY")
        case"2":
            print("\n SIGN IN")
            username=input("username: ")
            password=input("password: ")

            for student in students:
                if student[1]==username and student[2]==password:
                    print( student[0],"WELCOME")
                    break
            
            else:
                    print("\n username or password is not correct!")
        case"3":
            print("EXIT")
            break
                    