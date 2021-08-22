
#Program 3 missing please check Day 3 Slides and materials and download file done.py 
#Program 3 incorrect please check Day 3 Slides and materials and download file done.py 
count = 0
total = 0
avg = 0
keepgoing = True
while keepgoing:
  prompt1 = 'Enter a number : '
  line = input (prompt1)
  try:
     line = float(line)
     count = count + 1 
     total = total + line
     max= total
     avg = total / count
     min = avg
  except:
    if line == 'Done' or line == 'done':
      break
    else:
      print ('Invalid Input')
      continue
print (count, total, avg, max, min)

num1 = 2
num2 = 2

num1 <= num2