def main():

  s = 0
  m = 1

  for i in range(1, 11):
    s = s + (i/i**2) * m
    m = m * -1
    
  print(s)
  return 0


if __name__ == "__main__":
  main()
