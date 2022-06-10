from random import randint
from threading import Timer
import time
print("One of the most important factors in Calculus is speed. This doesn't only apply for a test or quiz, but also your AP exam.")
time.sleep(3)
print("Find the derivitive of the equation as fast as you can!")

problems = ["6x^3 - 9x +4", "3x^7 - 3", "5x - 6x", "2x^4 - 10x^2 + 13x", "x", "5x - 4", "cosx", "x^10", "7", "70x^3 + 32x^2 + 15"]

solutions = ["18x^2 - 9", "21x^6", "5 - 6", "8x^3 - 20x + 13", "1", "5", "-sinx", "9x^9", "0", "210x^2 + 64x"]

equations = {"6x^3 - 9x +4":"18x^2 - 9", 
             "3x^7 - 3":"21x^6",
             "5x - 6x":"5 - 6",
             "2x^4 - 10x^2 + 13x":"8x^3 - 20x + 13",
             "x":"1",
             "5x - 4":"5",
             "cosx":"-sinx",
             "x^10":"9x^9",
             "7":"0",
             "70x^3 + 32x^2 + 15":"210x^2 + 64x"
}

wrong = 0
timeout = 20
correct = 0

time.sleep(3)
while wrong < 3:
  if timeout < 5:
      timeout = 5
  rand = randint(0,9)
  t = Timer(timeout, print, ['Sorry, times up'])
  t.start()
  print(problems[rand])
  prompt = "You have %d seconds to find the derivitive of the equation...\n" % timeout
  answer = input(prompt)
  if answer == solutions[rand]:
      print("You got it!")
      correct = correct + 1
  elif answer == "":
      print("next")
  else:
      print("Wrong!")
      wrong = wrong + 1
      t.cancel()
  t.cancel()
  timeout = timeout - 1
print("Game Over!")
print("You got %d points") % correct
