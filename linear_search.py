from verify import verify, numbers

def linear_search(list, target):
  for i in range(0, len(list)):
    if list[i] == target:
      return i
  return None

result = linear_search(numbers, 6)
verify(result)

result = linear_search(numbers, 12)
verify(result)