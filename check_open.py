'''fo = open("foo.txt", "w")
print ("Name of the file: ", fo.name)
print ("Closed or not : ", fo.closed)
print ("Opening mode : ", fo.mode)
fo.close()'''
# Open a file
'''fo = open("foo.txt", "r+")
#print ("Name of the file: ", fo.name)
#fo.write( "Python is a great language.\nYeah its great!!\n")
str1 = fo.read(10)
print ("Read String is : ", str1)
# Close opened file
fo.close()'''
#import os
# Rename a file from test1.txt to test2.txt
#os.rename( "foo.txt", "foo1.txt" )
#os.remove("foo1.txt")
#sero-dision error
#d=10/0
#print(d)
'''
try:
    d=10/0
except ZeroDivisionError as e :
    #print("you cant divide by zero {0}".format(e))
    print("you cant divide by 0",e)

print("proceed")

l=[]
try:
    print(l[0])
except IndexError as e :
    #print("you cant divide by zero {0}".format(e))
    print("Not assigned any value to the index".format(e))

#index error
#l=[]
#print(l[1])

#attribute Error
#l=[]
#print(l.get())'''
#name error

#l=9
#print(l)

import math
def sqrt(x):
    if not isinstance(x, (int,float)):
        raise TypeError('x must be integer')
    elif x < 0 :
        raise ValueError(' x cannot be negative')
    else:
        return math.sqrt(x)
'''
try:
    print(sqrt("9"))
    print(sqrt(12))
except Exception as e:
    print("Error:", e)
'''
#print(sqrt("9"))
print(sqrt(12))