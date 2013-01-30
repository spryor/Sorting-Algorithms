#Author: Stephen Pryor
#Date: September 26, 2012

def sort_bubble(lst):
  updated = True
  while updated:
    updated = False
    for i in range(len(lst)-1):
      if lst[i] > lst[i+1]:
        lst[i], lst[i+1] = lst[i+1], lst[i]
        updated = True
  return lst
  

