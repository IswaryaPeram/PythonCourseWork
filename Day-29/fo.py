'''
file = open('Day30//demo.txt','r')
print(file.read())
file.seek(0)
print(file.readline())
file.seek(0)
print(file.readlines())
file.close()

with open('Day30//demo.txt','r') as file:
   print(file.read())
   file.seek(0)
   print(file.readline())
   file.seek(0)
   print(file.readlines

with open('Day30//demos.txt','w') as file:
    file.write("hello world")

with open('Day30//demos.txt','w') as file:
    file.write(" \n iswarya")

with open('Day30//demos.txt','a+') as file:
    file.write("hello world")
    file.seek(0)
    print(file.read())
'''

    

