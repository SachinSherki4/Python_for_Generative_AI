
## Tuple in Python
1. Tuple faster tham list, collection use to store collection of items
2. immutable : cant change  once created
3. Ordered : once added, can not change the orders
4. duplicate : Allow duplicate's in tuple
5. Hashable : tuple can be use as dictionary key

## Use Cases
1. Many AI/ML libraries like TensorFlow or PyTorch use tuples to store the shape of tensors (like matrix dimensions)
2. shape = (32, 32, 3)  # 32x32 image with 3 color channels (RGB)
3. Returning Multiple Values : While training AI models, sometimes functions return multiple things like (accuracy, loss) in one go
4. Coordinates Storage (Image/AI) : When dealing with images (object detection, face recognition), you need to store (x, y) coordinates, mostly as a tuple
5. Immutable Hyperparameters : In Generative AI model building, hyperparameters like layer size, learning rates, etc., sometimes stored in tuples to ensure they don’t change

## Exercise 
1. Given a tuple of numbers (10, 20, 30, 40, 50), print all numbers greater than 25.
2. You have a tuple of AI model evaluation results: Find the highest accuracy achieved

## Mini Project
1. Store students' names and their marks using tuples.
2. Find the highest scorer.
3. Find the average score.
4. Print all students with their marks.


[Solutions](tuple_exercise.py)