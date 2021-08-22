"""
r : reads file
w : Clears entire content of the file and  writes the file
a : appends(adds) contents to the file 
"""

#Reading a file
f = open('demo.txt','r')           #Opens the file/ Creates file pointer     
content = f.read()                 #Reading the content
print(content)                     #Printing the content
f.close()                          #Closing the file

#Writing a file
f = open('demo.txt','w')           #Opens the file/ Creates file pointer     
f.write("New content coming up!!")
f.close()
"""
Create a file ‘input.txt’ , write four statements to file (each on new line) and copy the data of #input file to ‘output.txt’ file
"""

f1 = open('input.txt','w')                                  #Creating this file in writing mode
f1.write('\nHello  \n')                                     #writing 4 statements
f1.write('Welcome  \n')
f1.write('To\n')
f1.write('Python Programming')
f1.close()

infile = open('input.txt','r')
outfile = open('output.txt','w')

for line in infile.readlines():
    outfile.writelines(line)                                #copying contents in output.txt
infile.close()
outfile.close()

f = open('output.txt','r')
content = f.read()
print(content)
f.close()