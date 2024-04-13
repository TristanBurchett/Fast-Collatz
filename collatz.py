def collatz(num, threshold):
  if (num < threshold):
    return True

  if (num == 1):
    return True

  if(num % 2 == 0):
    num/=2
  else:
    num = (num*3 + 1) / 2

  return collatz(num, threshold)

i=3
while True:
  if (i%1000000==1):
    print(i // 1000000, "million!")
  collatz(i, i)
  i+=2