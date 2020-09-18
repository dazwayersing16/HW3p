# Author: Adam Warsing ajw6150@psu.edu

def digit_sum(n):
  if n == 0:
    return 0
  else:
    return int(n%10 + digit_sum((n - n%10)/10))

def run():
  num = int(input("Enter an int: "))
  print("sum of digits of {} is {}.".format(num,digit_sum(num)))

if __name__ == '__main__':
  run() 