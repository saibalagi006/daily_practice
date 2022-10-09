"""
This code helps us to execute the try, except, else and finally block

"""

try:
    a=1
    f = open("file.txt")
    #a = b
### put specific exception at the top and generic after that 
except FileNotFoundError as e: 
    print("file is not found")
    #print(e)
except Exception as e:
    #print(e)
    print("some error")
else: ## else block executes if there is not except error
    print(f.read())
    f.close()
finally:
    print("code in finally executes irrepective of try-except error")
    print("this code will execute even if the exception is not caught in the try-except")


