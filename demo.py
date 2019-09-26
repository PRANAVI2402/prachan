# l=[3,1,8,6,5]
# print("Before soting {0}".format(l))
# l.sort()
# print("after sorting {0}".format(l))
"""
def getValues(a, pi=3.141, c=None):
    print(pi)
    input("Hold")
    if c is not None:
        print(c)
        return a + pi + c
    return a + pi


def getsum(a, b):
    return a + b


def getdiff(a, b):
    if isinstance(a,(int, float)):
        return a - b
    else:
        print("pass either int or float to performthis operation")
        return -1


print("hi")
if __name__ == '__main__':
    print("bye")
    a = 2
    b = 5
    print(getValues(4, 10, 5))
"""

'''
    # print((a==b))
    # print(id(a))
    # print(id(b))
    # print(getsum(a,b))
    # print(getdiff(a,b))
'''

import xlrd
loc = ("sample.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
#print sheet
sheet.cell_value(0, 0)
for i in range(sheet.nrows):
	#for k in range(sheet.cell_value):
		#print k
	print(sheet.cell_value(i, 1))

