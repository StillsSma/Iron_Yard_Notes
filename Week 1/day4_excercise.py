# input 1 = "programming is fun"
# input 2 = "m"
# output = [6, 7]

sentence = "i decided to learn how to program and it was a good decision"
letter = " "
output = []


for current_location, current_letter in enumerate(sentence):
    if current_letter == letter:
        output.append(current_location)

print (output)
