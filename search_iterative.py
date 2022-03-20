def search_iterative(list, item):
    # low and high keep track of which part of the list you'll search in.
    low = 0
    high = len(list) - 1

    # While you haven't narrowed it down to one element ...
    while low <= high:
      # ... check the middle element
      mid = (low + high) // 2
      guess = list[mid]
      # Found the item.
      if guess == item:
        return mid
      # The guess was too high.
      if guess > item:
        high = mid - 1
      # The guess was too low.
      else:
        low = mid + 1
    # Item doesn't exist
    return None


mi_lista = [1, 3, 5, 7, 9, 10, 14, 20]

print("resultado a :",str(search_iterative(mi_lista, 3)))
#print("resultado b: ",str(search_iterative(mi_lista, -3)))