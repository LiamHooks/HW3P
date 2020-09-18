def digit_sum(n):
  if n == 0:
    return 0
  else:
    return(digit_sum(n // 10) + (n % 10))


def run():
  num = int(input("Enter an int: "))
  print("sum of digits of " + str(num) + " is " + str(digit_sum(num)) + ".")

if __name__ == "__main__":
  run()
