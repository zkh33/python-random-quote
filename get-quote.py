from random import random


import random

from scipy import rand

def main():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = 13
  rnd = random.randint(0,last)
  print(quotes[rnd])

if __name__== "__main__":
  main()