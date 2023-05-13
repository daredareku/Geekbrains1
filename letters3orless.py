# Request input array of strings
input_array = input("Enter an array of strings separated by commas: ").split(",")

# Create a new array containing only strings with length less than or equal to 3 characters
output_array = []
for string in input_array:
    if len(string.strip()) <= 3:
        output_array.append(string.strip())

# Print the result to the console
print(output_array)