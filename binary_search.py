from verify import verify, numbers

def binary_search(list, target):
  first = 0
  last = len(list) - 1

  while first <= last:
    midpoint = (first + last)//2

    if list[midpoint] == target:
      return midpoint
    elif list[midpoint] < target:
      first = midpoint + 1
    else:
      last = midpoint - 1

  return None

result = binary_search(numbers, 6)
verify(result)

result = binary_search(numbers, 12)
verify(result)