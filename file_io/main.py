#read a file:
# f=open('myfile.txt','r')
# text=f.read()
# f.close()

# print(text)

# write a file:
# f=open('myfile.txt','w')
# f.write("this is written by command")    #this is write to the file and delete the old text
# f.close()
# print(f)

# append mode write the file and append to the end 
f2=open('myfile.txt','a')
f2.write("this is appended")
f2.close()

#create a file
# f3=open('myfile3.txt','x')
# print(f3)

#binary (b): used to handle binary files (images, pdfs, etc).
# f=open('myfile.txt','rb')
# text=f.read()
# print(text)

#open with automatically close the file
with open('myfile.txt', 'r') as f:
   text=f.read()
   print(text)