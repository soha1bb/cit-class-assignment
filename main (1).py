#Program to generate a dictionary of (i, i*i) for integral numbers between 1 and n:
def generate_square_dict(n):
  square_dict = {i: i*i for i in range(1, n+1)}
  return square_dict


number = 5
result_dict = generate_square_dict(number)
print(f"Dictionary of (i, i*i) for numbers from 1 to {number}: {result_dict}")
