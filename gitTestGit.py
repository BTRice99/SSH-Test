import time

x = 6

while x > 3:
  f = open("gitOutput.txt", "a")
  f.write(str("It Worked Again!!!!"))
  f.close()
  time.sleep(15)
