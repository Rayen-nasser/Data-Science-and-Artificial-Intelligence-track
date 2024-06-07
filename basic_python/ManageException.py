try:
    x = int(input("Enter number 1: "))
    y = int(input("Enter number 2: "))
    assert (x != 0 or y != 0), "Both numbers are zero"

    result = x / y  # This will raise ZeroDivisionError if y is zero

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Invalid input. Please enter an integer.")
except AssertionError as e:
    print("AssertionError:", e)
else:
    print("Result =", result)
finally:
    print("Completed")

age = int(input("enter you age: "))

if(age < 18):
    raise Exception("You Age Not Allowed")