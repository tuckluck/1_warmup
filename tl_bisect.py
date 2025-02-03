#Main function
def bisect_warmup(equation,lower,upper):
    
    from sympy import symbols, sympify, Eq, solve, sign, sin
    

    # Parse the equation string & get zero on right hand side of equation.
    x = symbols('x')
    lhs, rhs = equation.split('=')    #splits the equation into two when "=" is found
    new_lhs = sympify(lhs.strip()) - sympify(rhs.strip()) 
    new_equation = Eq(new_lhs,0)      #new equation with zero only on right hand side

    # user input lower and upper bounds become a and b, c is created as the algebraic mid point
    a = lower
    b = upper
    c = (a+b)/2

    #solve equation for user input a and b, also solve for calculated c
    f_a = (new_lhs).subs(x, a)
    f_b = (new_lhs).subs(x, b)
    f_c = (new_lhs).subs(x, c)

    #input error checking
    if f_b == f_a:                      #error upper and lower are the same
        print('error, lower and upper bound are equal')
        return 
    if sign(f_a) == sign(f_b):          #check if answer exists between lower and upper bound
        print('error, no solution or multiple solutions between lower and upper bound')
        return
   
    else:
    
        # set the initial difference f(upper) and f(lower)
        difference = abs(f_b - f_a)
    
        # continue looping until the difference between f(a) and f(b) is less than specified value
        while difference > .0001:         #arbitrary value for how close result must be to break loop
            f_c = (new_lhs).subs(x, c)    #calculates value for new f(c)
            f_a = (new_lhs).subs(x, a)    #calculates value for new f(a)
            if sign(f_c) == sign(f_a):
                a = c                     #if f(c) is on same side of the solution as f(a), c becomes new a
            else:
                b = c                     #otherwise must mean f(c) is on f(b) side of the solution, c becomes new b
            c = (a+b)/2                   # new c calculated
            f_a = (new_lhs).subs(x, a)    #calculates value for new f(a)
            f_b = (new_lhs).subs(x, b)    #calculates value for new f(b)
            difference = abs(f_b - f_a)   # checks the absolute difference between f(b) and f(a) to determine if the while loop should continue
            
    
        outputd = solve(new_equation)     #actual answer or answers for comparision purposes
        print("possible answer/s",outputd)#prints actual answers
        print("bisect method answer",c)   #prints bisect method answer which should be one of the actual answers
        return c
    


