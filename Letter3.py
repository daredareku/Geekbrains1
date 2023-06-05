# Input the initial array from the keyboard
arr = input("Enter an array of strings separated by spaces: ").split()

# Create an empty array to store the results
result = []

# Loop through each string in the initial array
for s in arr:
    # Add the string to the result if its length is less than or equal to 3
    if len(s) <= 3:
        result.append(s)

# Print the result to the screen
print(result)
