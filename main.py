import numpy as np
def steps(first, last, step):
    iterator = first
    iterations = (last - first) / step
    counter = 1
    steps = []

    while not counter == iterations:
        iterator += step
        steps.append(iterator)
        counter += 1
    return steps

def generateLes(initialMatrix, first, last, step):
    column = 0
    matrix = initialMatrix

    for row in range(0, len(matrix)):
        currentStep = steps(first, last, step)[row - 1]
        if row != 0 and column != 4:
            matrix[row][column] = -2 - 0.02 * currentStep
            matrix[row][column - 1] = 0.975
            matrix[row][column + 1] = 1.025
        elif column == 4:
            matrix[row][column] = -2 - 0.02 * currentStep
            matrix[row][column - 1] = 0.975

        column += 1
    return matrix

def fillSpecialRow(initialMatrix, values, index):
    initialMatrix[index] = values
    return initialMatrix

def solveLes(initialMatrix, d_row):
    return np.linalg.solve(initialMatrix, d_row)

initialMatrix = np.zeros((5, 5))
dRow = [0, 0.02, 0.02, 0.02, 0.02]
initialMatrix = generateLes(initialMatrix, 1.4, 2.4, 0.2)
initialMatrix = fillSpecialRow(initialMatrix, [0.9375, 0.5, 0, 0, 0], 0)
print("Система: ", '\n', initialMatrix, '\n', "Розв'язок: ", solveLes(initialMatrix, dRow), sep="")
