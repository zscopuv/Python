# In this case, we're finding the next 15 numbers in the sequence.
reps = 15 

# The number you input will be included in the output along with the number before it.
number = 1

# Set 'greater' to the starting number and 'smaller' to the number before it (number-1).
# (number variable stands for number 1).
greater, smaller = number, number-1

# First, we print the two starting numbers.
print(smaller, greater)

# This loop will run for the number of repetitions we want.
# (reps variable stands for 15 times).
for i in range(reps):

    # Swap values: 'temp' will temporarily hold the value of 'smaller', 
    # then we update 'smaller' to be the previous 'greater'.
    temp, smaller = smaller, greater

    # 'greater' becomes the sum of the previous two numbers.
    greater = temp + smaller

    # Print the new 'greater' value, which is the next number in the sequence.
    print(greater)
