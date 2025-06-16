import numpy as np

#array5 = 5 * np.ones(27)
#print("Array of 27 elements, all equal to 5:")
#print(array5)

#x_array = np.array(1, 2, 3, 4, 5)
#y_array = np.array(2, 3, 4, 5, 6)
#print(x_array ** y_array)

#matrix = (np.eye(5)+1)*5
#print("5x5 Identity Matrix of 10 and 5:")
#print(matrix)

# This code will create a random number between 1 and 8 using a seed provided by the user.
#randinput = input("Enter a number: ")
#np.random.seed(int(randinput))
#array = np.random.randint(1, 9, size=(1, 1))
#print("Random number between 1 and 8: "+ str(array[0][0]))

# This code will ask for a random number as the seed and then will roll a dice with 12 sides.
#dice_seed = input("Enter a seed for the dice roll: ")
#np.random.seed(int(dice_seed)) 
#dice_roll = np.random.randint(1, 13)
#print("Dice roll result: " + str(dice_roll))


array50 = np.random.randint(1, 11, size=(50))
print("Array of 50 random integers between 1 and 10:")
print(array50)
print("Mean of the array: " + str(np.mean(array50)))
print("Standard deviation of the array: " + str(np.std(array50)))