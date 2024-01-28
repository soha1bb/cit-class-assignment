#Program to display the sum of n numbers using a list:
def sum_of_numbers(n):
  num_list = [int(input(f"Enter number {i+1}: ")) for i in range(n)]
  total_sum = sum(num_list)
  return total_sum

# Example usage:
n = 5
result_sum = sum_of_numbers(n)
print(f"Sum of {n} numbers: {result_sum}")
