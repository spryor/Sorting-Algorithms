#Author: Stephen Pryor
#Date: December 24, 2012

def sort_merge(lst):
  if len(lst) <= 1:
    return lst
  m = int(len(lst)/2)
  left, right = lst[:m], lst[m:]
  left = sort_merge(left)
  right = sort_merge(right)
  return merge(left, right)

def merge(left, right):
  result = []
  i, j = 0, 0
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1
  return result + left[i:] + right[j:]