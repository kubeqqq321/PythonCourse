#exception - events detected during execution that interrupt the flow of a program


try:
    numerator = int(input("Enter the number to divide: "))
    denominator = int(input("Enter the number to divide by: "))
    result = numerator/denominator

        # except ZeroDivisionError:
        #     print("You can't divided by zero! idiot!")
        # except ValueError:
        #     print("Enter only numbers plz!")
        # except Exception:
        #     print("Something went wrong")
    #e is optional
except ZeroDivisionError as e:
    print(e)
    print("You can't divided by zero! idiot!")
except ValueError as e:
    print(e)
    print("Enter only numbers plz!")
except Exception as e:
    print(e)
    print("Something went wrong")
else:
    print(result)
finally:
    print("This will always execute")
