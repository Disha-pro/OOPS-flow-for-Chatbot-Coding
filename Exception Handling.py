#EXCEPTION
An exception is an error that occurs while your program is running.
number = 10
result = number / 0

Python gives:

#ZeroDivisionError
Without handling it, the program stops.
----------------------------------------------------------------------------------------
#Try and Except
We can handle the error:
try: #The try block should contain the code that might fail
    number = 10
    result = number / 0
except:
    print("Something went wrong")
#But don't use a generic except unnecessarily
Instead use below :
try:
    number = 10
    result = number / 0

except ZeroDivisionError:
    print("Cannot divide by zero")
-------------------------------------------------------------------------------------------
try:
    # code that might fail

except SomeError:
    # what to do if that error occurs
--------------------------------------------------------------------------------------------------
  number = int(input("Enter a number: "))

try:
    a = 100 / number
    print(a)

except ZeroDivisionError:
    print("Cannot divide by zero")
  ------------------------------------------------------------------------------------------------------
#How Python chooses the except
try
 │
 ├── ValueError? ──────→ except ValueError
 │
 └── ZeroDivisionError? → except ZeroDivisionError
  #It executes the matching handler.

-------------------------------------------------------------------------------------------------
#MULTIPLE EXCEPT:
number = input("Enter the number: ")

try:
    number = int(number)
    result = 100 / number
    print(result)

except ValueError:
    print("Invalid number")

except ZeroDivisionError:
    print("Cannot divide by zero")

#Think of try as a protective area:
try:
 ┌──────────────────────────────┐
 │ int(input())                 │ ← ValueError can happen
 │                              │
 │ 100 / number                 │ ← ZeroDivisionError can happen
 └──────────────────────────────┘
             ↓
        error occurs
             ↓
      matching except

#You can put the conversion directly inside:
try:
    number = int(input("Enter the number: "))
    result = 100 / number
    print(result)

except ValueError:
    print("Invalid number")

except ZeroDivisionError:
    print("Cannot divide by zero")
-----------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------
Now we'll add:

else → runs only when there is no error
finally → runs always, whether there is an error or not

#ELSE
#else runs only if the try block succeeds.
try:
    number = int(input("Enter the number: "))
    result = 100 / number

except ValueError:
    print("Invalid number")

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Calculation successful")
    print(result)


#FINALLY
#finally runs no matter what happens.
                 finally
                    ↓
             ALWAYS EXECUTES
          -----------------------
try:
    number = int(input("Enter the number: "))
    result = 100 / number

except ValueError:
    print("Invalid number")

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Calculation successful")

finally:
    print("Program finished")
-------------------------------------------------------------------------------------------------
try:
    # risky code

except:
    # error handling

else:
    # successful execution

finally:
    # always execute


try:
    number = input("Enter the number")
    result = 100 / int(number)
    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid Number")

else:
    print("Calculation successfully")

finally:
    print("Program Finished")
    ---------------------------------------------------------------------------------------------
    #RAISE
#raise → intentionally create an exception
But sometimes you want to tell Python that something is invalid yourself.
That's when we use raise.

def ask_chatbot(question):
    if question == "":
        raise ValueError("Question cannot be empty")
    return "Question"


try:
    question = "What is RAG"
    result = ask_chatbot(question)
    print(result)

except ValueError as e:
    print(e)

#FLOW
Function
   ↓
Validate input
   ↓
raise error if invalid
   ↓
try calls function
   ↓
except handles the error

#IMP
#raise stops the current function and sends the exception to the nearest matching except.
def ask_chatbot(question):
    if question == "":
        raise ValueError("question cannot be empty")

    return question


try:
    question = "What is LLM?"
    result = ask_chatbot(question)
    print(result)

except ValueError as e:
    print(e)
-------------------------------------------------------------------------------------------------
#EXCERCISE
def retrieve_document(query):

    if query == "":
        raise ValueError("Query cannot be empty")
 #Create/throw an error.
    return "Retrieving documents for your query"


try:
    query = ""#Store a value.
    result = retrieve_document(query) #CALLING THE QUERY
    print(result)

except ValueError as e:
    print(e)#Catch/handle that error.
