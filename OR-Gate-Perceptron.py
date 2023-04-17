import random

threshold = 0.2
learningRate = 0.1
epochs = 5

def desiredOutput(inputs, index):
    if (inputs[index][0] == 1 or inputs[index][1] == 1):
        return 1
    else:
        return 0

def initialWeights():
    return round(random.uniform(-0.5, 0.5), 1), round(random.uniform(-0.5, 0.5), 1)

def actualOutput(weight1, weight2, inputs, index, threshold):
    result = (inputs[index][0] * weight1) + (inputs[index][1] * weight2)
    if (result >= threshold):
        return 1
    else:
        return 0

def finalWeights(weight1, weight2, inputs, index, learningRate):
    fWeight1 = weight1 + (learningRate * inputs[index][0] * error)
    fWeight2 = weight2 + (learningRate * inputs[index][1] * error)
    return round(fWeight1, 1), round(fWeight2, 1)

inputs = [(0,0), (0,1), (1,0), (1,1)]
weight1, weight2 = initialWeights()
for i in range (epochs):
    print('-' * 100)
    print(f"Epoch {i+1}\n")
    for j in range (4):
        index = j
        desireOutput = desiredOutput(inputs, index)
        actOutput = actualOutput(weight1, weight2, inputs, index, threshold)
        error = desireOutput - actOutput
        if(desireOutput == actOutput):
            fWeight1, fWeight2 = weight1, weight2
        else:
            fWeight1, fWeight2 = finalWeights(weight1, weight2, inputs, index, learningRate)
        print("Inputs \t Desired Output \t Initial weights \t Actual output \t Error  Final Weights \n")
        print(f"{inputs[index][0]}   {inputs[index][1]}\t\t{desireOutput}\t\t {weight1}   {weight2}\t\t {actOutput}\t\t {error}\t {fWeight1}   {fWeight2}\n")
        print('-' * 100)
        weight1 = fWeight1
        weight2 = fWeight2