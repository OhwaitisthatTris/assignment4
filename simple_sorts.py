# simple_sorts.py
# bubble sort, selection sort, insertion sort
# Strongly suggest you turn off LLMs like
# GitHub Copilot, TabNine, etc. when working on this file.
# Writing a sorting algorithm yourself is the best
# way to learn how it works.
# Modified by: Tristan Crawford Jr

def bubble_sort(lst):
    n = len(lst)
     for i in range(n):
        swapped = False

      for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst
    pass

def selection_sort(lst):
    n = len(lst)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if lst[j] < lst[min_index]:
                min_index = j

        lst[i], lst[min_index] = lst[min_index], lst[i]

    return lst
    pass

def insertion_sort(lst):
    for i in range(1,len(1st)):
    key = 1st[i]
    j = i - 1

    while j >= 0 and 1st[j] > key:
        1st[j + 1] + 1st[j]
        j -= 1

    1st[j +1] = key
return list
    pass
