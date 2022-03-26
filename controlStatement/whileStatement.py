# While 문

i = 0
while i <= 10:
  print(i)
  i += 1
  
## continue, break, pass
i = 0

while i < 20:
  if i == 10:
    print('===================')
    break
  elif i % 2 == 0:
    print(i)
    i += 1
  else:
    i += 1
    continue
  print('짝수입니다')