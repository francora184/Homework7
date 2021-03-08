def fizzBuzz(x):
  if(x % 3 == 0 and x % 5 == 0):
    return "FizzBuzz"
  if(x % 3 == 0):
    return "Fizz"
  if(x % 5 == 0):
    return "Buzz"

def leapYear(y):
  if (y % 4 == 0):
   if (y % 100 == 0):
       if (y % 400 == 0):
          return "Yes"
       else:
          return "No"
   else:
      return "Yes"
  else:
    return "No"
