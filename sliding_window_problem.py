"""
Program to find out the min value from a window limit from a given array
"""


def sliding_window(arrayList, numWindow):
    itr = 0
    while itr < len(arrayList) - 1:
        tempArray = arrayList[itr:itr + numWindow]
        val = min(tempArray)
        print(val)
        itr = itr + 1
    return
  
  
sliding_window([1,2,3,4,55,6,7,8], 4)
