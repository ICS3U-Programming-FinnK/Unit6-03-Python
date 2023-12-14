#!/usr/bin/env python3
# Created by: Finn Kitor
# Created on: December 14th, 2023
# this program generates 10 numbers between 0 to 100 and it finds the minimum value of the list.
import random

MAX_ARRAY_SIZE = 10
MIN_NUM = 0
MAX_NUM = 100


def find_min_value(arr):
    # Checking if the array is empty
    if len(arr) == 0:
        raise ValueError("Input array is empty.")

    # Initializing the minimum value with the maximum possible value
    min_value = MAX_NUM + 1

    # Looping through each element in the array
    for num in arr:
        # Updating the minimum value if a smaller value is found
        if num < min_value:
            min_value = num

    return min_value


def main():
    # Generating 10 random numbers between MIN_NUM and MAX_NUM
    random_numbers = [random.randint(MIN_NUM, MAX_NUM) for _ in range(MAX_ARRAY_SIZE)]

    # Printing the generated numbers
    print("Generated Numbers:")
    print(random_numbers)

    # Finding the minimum value using the find_min_value function
    min_value = find_min_value(random_numbers)

    # Displaying the minimum value
    print(f"Minimum Value: {min_value}")


# Calling the main function to run the program
if __name__ == "__main__":
    main()
