# Par ou Ímpar
N = int(input())
i = 0
while i < N:
  num = int(input())
  if num > 0 and num%2==0:
    print("EVEN POSITIVE")
  elif num < 0 and num%2==0:
    print("EVEN NEGATIVE")
  elif num < 0 and num%2==1:
    print("ODD NEGATIVE")
  elif num > 0 and num%2==1:
    print("ODD POSITIVE")
  else:
    print("NULL")
  i +=1