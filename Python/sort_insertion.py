#Author: Stephen Pryor
#Date: September 26, 2012

def sort_insertion(lst):
  for i in range(1, len(lst)):
    iVal = lst[i]
    iIndex = i
    while iIndex > 0 and lst[iIndex - 1] > iVal:
      lst[iIndex] = lst[iIndex - 1]
      iIndex = iIndex - 1
    lst[iIndex] = iVal
  return lst