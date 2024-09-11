# Function to generate all 7-digit combinations with a specific suffix
def generate_combinations(suffix, filename):
    with open(filename, 'w') as f:
        for i in range(1000000, 2000000):  # 7-digit combinations range from 0000000 to 9999999
            combination = f"{i:07d}" + suffix  # Ensure the number is 7 digits long
            f.write(combination + "\n")

# Usage
generate_combinations("0863", "combinations.txt")
