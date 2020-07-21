def insertion_sort(lst):
  pass
  # seperate the first element
  # think of it as sorted

  # for all unsorted items
  for i in range(1, len(lst)):
    # mark the current item we are conscidering
    current = lst[i]
    
    # look left until we find the proper place to insert current item
    j = i
    while j >= 0 and current < lst[j - 1]:
      # # as we are looking left, we need ot shift items right
      lst[j] = lst[j - 1]
      j -= 1

    # when item to the left is less than current.
    # or there isnt any items to the left.
    lst[j] = current
      # insert item