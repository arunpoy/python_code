def firstNonRepeatingCharacter(string):
    # Write your code here.
    characterFrequencies = {}

    for character in string:
        characterFrequencies[character] = characterFrequencies.get(character, 0) + 1

    for idx in range(len(string)):
        character = string[idx]
        if characterFrequencies[character] == 1:
            return idx


    return -1

print(firstNonRepeatingCharacter("aruna"))