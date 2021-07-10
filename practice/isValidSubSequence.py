def validSubSequence(array,sequence):
    arrIdx = 0
    seqIdx = 0

    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1

    return seqIdx == len(sequence)


array = [1,2,4,5,6]
sequence = [2,5]

print(validSubSequence(array,sequence))
