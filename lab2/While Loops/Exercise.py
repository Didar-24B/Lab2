#1
Which statement is a correct syntax to break out of a loop?
#break

#2
i = 1
while i < 6:
  print(i)
  i += 1
#while

#3
i = 1
while i < 6:
  if i == 3:
    break
  i += 1
#break

#4
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
#continue

#5
i = 1
while i < 6:
  print(i)
  i += 1
  else:
  print("i is no longer less than 6")
#else: