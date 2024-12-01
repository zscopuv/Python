from math import sqrt

# Explanation of program's functionality
print ("This is a program for solving quadratic equations.\nAll quadratic equations are in a form of ax² + bx + c = 0")

# If invalid input is given, the question will be asked repetetively
while True:
    
    # Asking whether to solve a quadratic equation or to display its form according to the roots given
    start= input("Do you know the roots and want to know the coefficients or do you know the coefficients and want to know the roots?\nType r if you know roots\nType c if you know the coefficients\n")
    
    if start.lower() == "r":
        # If invalid input is given, the question will be asked repetetively
        while True:
            
            roots_loop = input("Does your equation has 1 or 2 roots with a = 1? \nType 1 for 1 root and 2 for 2 roots. ")
            
            if roots_loop.lower() == "1":
                # Checking for invalid input                 
                try:
                    x1 = int(input("What is your one root? "))
                    # Calculating for 1 root using the formula (a-b)²= a²-2ab+b² or (a+b)²= a²+2ab+b² when we are sure that a=1, which is in the question.
                    a = 1
                    b = 2* -x1
                    c = (-x1)**2
                    # Displaying the result based on whether it is positive or negative, not to display additional + or -
                    if x1 > 0:
                        print(f"The form of the quadratic equation with 1 root {x1} is x²{b}x+{c} = 0")
                    elif x1 < 0:
                        print(f"The form of the quadratic equation with 1 root {x1} is x²+{b}x+{c} = 0")
                    else:
                        print(f"The form of the quadratic equation with 1 root {x1} is x²+x+{x1} = 0")
                    # Stopping the loop because a result is already given                     
                    break
                
                # If invalid input is given, it will ask you again                 
                except:
                    print ("Invalid input. Type an integer.")
                    
            elif roots_loop.lower()== "2":
                # Checking for invalid input
                try:
                    x1 = int(input("What is your first root? "))
                    x2 = int(input("What is your second root? "))
                    # Calculating using the Vieta's formulas                     
                    a = 1
                    b = -x1 + -x2
                    c = -x1 * -x2
                    # Making sure not to display 1 or -1 before x                      
                    if b == 1:
                        if x1 < 0 and x2 < 0:
                            print(f"The form of the quadratic equation with 2 roots {x1},{x2} is x²+x+{c} = 0")
                        elif x1 < 0 and x2 > 0 or x1 > 0 and x2 < 0:
                            print(f"The form of the quadratic equation with 2 roots {x1},{x2} is x²+x{c} = 0")
                        elif x1 > 0 and x2 > 0:
                            print(f"The form of the quadratic equation with 2 roots {x1},{x2} is x²+x+{c} = 0")
                    elif b == -1:
                        if x1 < 0 and x2 < 0:
                            print(f"The form of the quadratic equation with 2 roots {x1},{x2} is x²-x+{c} = 0")
                        elif x1 < 0 and x2 > 0 or x1 > 0 and x2 < 0:
                            print(f"The form of the quadratic equation with 2 roots {x1},{x2} is x²-x{c} = 0")
                        elif x1 > 0 and x2 > 0:
                            print(f"The form of the quadratic equation with 2 roots {x1},{x2} is x²-x+{c} = 0")
                    else:   
                        if x1 < 0 and x2 < 0:
                            print(f"The form of the quadratic equation with 2 roots {x1},{x2} is x²+{b}x+{c} = 0")
                        elif x1 < 0 and x2 > 0 or x1 > 0 and x2 < 0:
                            print(f"The form of the quadratic equation with 2 roots {x1},{x2} is x²{b}x{c} = 0")
                        elif x1 > 0 and x2 > 0:
                            print(f"The form of the quadratic equation with 2 roots {x1},{x2} is x²{b}x+{c} = 0")
                    # Stopping the loop because a result is already given
                    break
                
                # If invalid input is given, it will ask you again
                except:
                    print ("Invalid input. Type an integer.")
        
        # Stopping the whole roots loop         
        break
    
    elif start.lower()== "c":
        # If invalid input is given, the question will be asked repetetively         
        while True:
            # Checking for invalid input
            try:
                a = int(input("What is your number a? "))
                b = int(input("What is your number b? "))
                c = int(input("What is your number c? "))
                # Making sure it is a quadratic equation                 
                if a != 0:
                    d = b**2 - 4*a*c
                    # Calculating using discriminant                     
                    if d > 0:
                        x1 = (-b +sqrt(d)) / (2*a)
                        x2 = (-b -sqrt(d)) / (2*a)
                        # If the 1st decimal place is 0, it will round to the nearest integer                         
                        if x1 % 1==0:
                            x1=round (x1)
                        if x2 % 1==0:
                            x2=round (x2)
                        print(f"The solution of this quadratic equation is: {x1},{x2}")
                    elif d == 0:
                        x1 = (-b + d) / (2*a)
                        # If the 1st decimal place is 0, it will round to the nearest integer
                        if x1 % 1 == 0:
                            x1 = round (x1)
                        print(f"The solution of this quadratic equation is: {x1}") 
                    else:
                        print ("The Discriminant is a negative number so the solution is None")
                else:
                    #Calculating linear equation                     
                    if c > 0:
                        x1 = -c / b
                    else:
                        x1 = +c / b
                    # If the 1st decimal place is 0, it will round to the nearest integer
                    if x1 % 1 == 0:
                        x1 = round (x1)
                    print(f"The solution of this quadratic equation is: {x1}")
                    
                # Stopping the loop because a result is already given
                break
                
             # If invalid input is given, it will ask you again
            except:
                print ("Invalid input. Type an integer.")
                
        #Stopping the whole coefficients loop         
        break
        


    