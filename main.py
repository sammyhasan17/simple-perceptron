# Course: CS3642
# Student name: Sammy Hasan-Silva
# Student ID:000917482
# Assignment #: 3
# Due Date:
# Signature: Sammy Hasan-Silva
# Score:
from random import random

class Perceptron:

    def __init__(self, inputSize):
        self.inputLayerSize = inputSize
        self.weights = []
        self.bias = random()

        for i in range(inputSize):
            self.weights.append(random())

    def activation_function(self, val):
        # represents bright
        if val >= 2:
            return 1
        else:
            # dark
            return 0

    def summation_function(self, input):
        sum = self.bias

        for i in range(len(input)):
            sum += float(input[i]) * self.weights[i]
            # print("weights"+str(self.weights[i]))
            # print(sum)
        return sum

    def training(self, data):
        for val in data:

            temp = 0
            target = 0
            for i in val:
                temp += int(i)
            if (temp > 1):
                target = 1

            sum = self.summation_function(val)

            output = self.activation_function(sum)

            error = output - target
            # print("error", error)
            if (output != target):
                # change weights
                for i in range(len(val)):
                    self.weights[i] += self.weights[i] * error * -0.1

    def predict(self, input):
        sum = self.summation_function(input)
        output = self.activation_function(sum)
        return output

# generate 16 samples permutation
def generate(ones, zeros, string, _len, array):
    if _len == len(string):
        array.append(string)
        return
    generate(ones + 1, zeros, string + "1", _len, array)

    if (ones > zeros):
        generate(ones, zeros + 1, string + "0", _len, array)

input = ""
all_samples = []
generate(4, 0, input, 4, all_samples)
print(all_samples)

perc = Perceptron(4)
perc.summation_function(all_samples[1])
epochs = 100
for i in range(epochs):
    print("Epoch #:" + str(i))
    perc.training(all_samples)

print(perc.predict("0101"))
print("^ this is the prediction")
