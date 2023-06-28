def main():

  s = 0
  d = 1

  for i in range(1, 100, 2):
    s += i / d
    d += 1
  print(s)
  return 0


if __name__ == "__main__":
  main()
