# Find the two entries that sum to 2020.
# Multiply those two numbers together.

# Open file.
inFile = open("num.txt", "r")

# Create a list.
number_list = []

# Read line and add to the number list.
for line in inFile:
    number = int(line.strip())
    number_list.append(number)


def getFirstProduct(number_list):
    for index in number_list:
        for second_index in number_list:
            if index + second_index == 2020:
                return index * second_index


def getSecondProduct(number_list):
    for index in number_list:
        for second_index in number_list:
            for third_index in number_list:
                if index + second_index + third_index == 2020:
                    return index * second_index * third_index


output = getFirstProduct(number_list)
output_two = getSecondProduct(number_list)

print("The first number is:", output)
print("The second number is:", output_two)

# Close file.
inFile.close()
