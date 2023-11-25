# PART 1
print("# # # f(x) = -x^2 + 3x - 2 from a=1 to b=2 # # #")

def f(x):
    return (-(x ** 2) + 3 * x - 2)  # Define the function

x = 1  # To plus 0.1 to judge whether x < 2.1.
sum = 0  # calculate the sum of the f(x)
while x < 2.1:
    print("When x = ", round(x,17), "=> f(x) =", round(f(x),17))  # Use "round" to get the 17 digits
    x += 0.1  # To plus 0.1 to judge whether x < 2.1.
    sum += f(x)  # calculate the sum of the f(x)

# PART 2
print("")  # SPACE
print("# # # Example of Trapezium Rule Values # # #")

h = 0.10  # (b-a)/n = (2-1)/10
first = f(1)
last = f(2)

MiddleSum = sum-f(1)-f(2)

T = (h/2)*(first+2*(MiddleSum)+last)  # Calculate the Trapezium Rule

actual = 1/6
error = ((actual-T)*100)/actual  # Calculate the error

print("First Height: ", first)
print("Last Height: ", last)
print("Middle Sum: ", MiddleSum)
print("Integration is approximately: ", T)
print("True value of integration is 1/6.")
print("Therefore the error is: ", error, "%")  # Print all.

quit()