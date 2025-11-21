# Funtions: Block of statements in a group or collection of statements. reusability is the best feature for funtion.
   *   Syntas:  def add():
                    a= int(input("enter a number"))
                    b= int(input("enter b number"))
                    c=a+b
                    print(c)
                add()
# Jump statements in function:
                * break: exit from the loop
                * Continue: exit from current itteration and continue still the end of loop
                * pass: it wont do nothing..just for skip the statement.
                * return: return the  value. return statement is used within a function to exit the function's execution and send a value back to the point where the function was called.
* while calling function we need both function define and function call as well.

                    def sum():   # function definition
                        a=int(input("enter a number"))
                        b=int(input("enter a number"))
                        c = a+b
                        print(c)
                    sum()   # function call
# Function with arguments:
    * def add(a,b): defination of funcation
      add(10,20)   -> function call
    * in function definition what ever we are passing variables those are parameters, in function call what ever we are passing those are arguments.

# Arguments types:
     * positional arguments: mul(10,20)
     * default arguments: we can pass arguments at function definition only ..Ex.. def add(a=20,b=30    )
     * keyword arguments: parameter name also we can mention..mul(a=20,b=30)
     * Arbitory arguments: we can pass multiple function calls ..def hey(*x)
     * Arbitory keywords: we can pass multiple key values under funtion call.
# Return:return a value to the  functional calling area and exit from the function.
# local vs global variables:
        * local variables:  variables define and used in a function definition.
        * local variables are accessiable with in that function definition only.
        # Global variables:we can declare  variables outside the  function definitaion 
# Variable :
      * scope: region wise we can check the scope
      * visibility: memory based
      * lifetime: duration of time in which varialbe exits in memory, execution of program.
       