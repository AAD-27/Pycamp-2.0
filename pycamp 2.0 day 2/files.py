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
f = open('demo.txt','w')            #Writes the entire file
f.write("Content gone!!!\n")
f.close()

#Appending a file
f = open('demo.txt','a')            #Writes the entire file
f.write("New content coming up")
f.close()

"""
4.2 Create a file ‘input.txt’ , write four statements to file (each on new line) and copy the data on#input file to ‘output.txt’ file
"""

f1 = open('input.txt','w')                                  #Creating this file in writing mode
f1.write('\nHello all \n')                                  #writing 4 statements
f1.write('Welcome  \n')
f1.write('To\n')
f1.write('Python Programming')
f1.close()                                                  #Closing of file in writing mode
infile=open('input.txt','r')                                # file named "input.txt", will be opened with the reading mode
outfile=open('output.txt','w')                              #creating new output.txt file in writing mode
for line in infile.readlines():
    outfile.writelines(line)                                #copying contents in output.txt
infile.close()
outfile.close()
f = open('output.txt','r')
content = f.read()                                          #all the statements are copied into content
print(content)                                              #printing these statements
f.close()