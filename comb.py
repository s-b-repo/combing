from itertools import product

def generate_unique_case_combinations(text):
    # Find positions of alphabetic characters
    letter_positions = [i for i, char in enumerate(text) if char.isalpha()]
    
    # Generate all unique combinations of cases
    unique_combinations = set()
    for bits in product([0, 1], repeat=len(letter_positions)):
        new_text = list(text)
        for i, bit in zip(letter_positions, bits):
            new_text[i] = new_text[i].upper() if bit else new_text[i].lower()
        unique_combinations.add("".join(new_text))  # Add to set to avoid duplicates
    
    return list(unique_combinations)

def save_combinations_to_file(combinations, filename="unique_case_combinations.txt"):
    with open(filename, "w") as file:
        for combo in combinations:
            file.write(combo + "\n")
    print(f"Unique combinations saved to {filename}")

# Example usage
input_text = "aA1"
combinations = generate_unique_case_combinations(input_text)
save_combinations_to_file(combinations)
