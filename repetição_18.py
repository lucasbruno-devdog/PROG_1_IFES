def main():

  s = 0
  n = 37
  m = 38

  for i in range(1, 38):
    s += ((n)*(m)) / i
    n -= 1
    m -= 1
  print(s)
  return 0


if __name__ == "__main__":
  main()
