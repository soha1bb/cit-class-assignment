#Python Program to count unique values inside a list:
def count_unique_values(lst):
  unique_values = set(lst)
  count = len(unique_values)
  return count


my_list = [1, 2, 3, 1, 2, 4, 5]
result = count_unique_values(my_list)
print(f"Number of unique values in the list: {result}")
