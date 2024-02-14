#goal is:
#
# Write a script to generate a passphrase by taking words from
# /tmp/words.txt
# The wordNumbers array holds three random numbers. Each number
# corresponds to a word in words.txt. So for example
# wordNumbers[1] is the second word in /tmp/words.txt.
# Put a space between each word and print it out
#
with open("/tmp/randomwordsnumbers.txt", "r") as file:
    data = file.read()

wordNumbers = data.rstrip().split("\n")
with open("/tmp/words.txt", "r") as wordles:
  wn = wordles.readlines()
  #print(wn[int(data[0])] ,wn[int(data[1])] ,wn[int(data[2])]  )
  word1 = wn[0]
  print(wn[0])
  print(wn[1])
  print(wn[2])
  print(wn[3])
  