#Python program to print the Fibonacci series:
def fibonacci_series(n):
  fib_series = [0, 1]
  for i in range(2, n):
      fib_series.append(fib_series[-1] + fib_series[-2])
  return fib_series

# Example usage:
fibonacci_length = 8
result_fibonacci = fibonacci_series(fibonacci_length)
print(f"Fibonacci series of length {fibonacci_length}: {result_fibonacci}")
