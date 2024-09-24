numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = map(lambda x: x ** 2, numbers) # parallel process here, you are sqaruing multiple numbers at once
sum_of_squares = sum(squares)
print(sum_of_squares)