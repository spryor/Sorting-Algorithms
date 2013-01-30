#Author: Stephen Pryor
#Date: September 26, 2012

import random

def sort_quick(lst):
  if len(lst) < 1:
    return lst
  pivot_index = random.randrange(0, len(lst))
  pivot_value = lst[pivot_index]
  del lst[pivot_index]
  below = []
  above = []
  for val in lst:
    if val <= pivot_value:
      below.append(val)
    else:
      above.append(val)
  return sort_quick(below)+[pivot_value]+sort_quick(above)