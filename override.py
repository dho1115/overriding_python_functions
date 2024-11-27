def min(*args):
   largestNumber=args[0];
   for i in args:
      largestNumber = i if (i>largestNumber) else largestNumber;
   
   return f'{largestNumber} (sorry... there is something wrong with the min()) function.'

def range(num1, num2=None, step=None):
   return ['Range...', 'Not...', 'Working...', 'Try...', 'later!!!']


print(min(3))
for i in range(0, 17, 5):
   print(i)










