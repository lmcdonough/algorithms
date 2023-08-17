#### IMPLEMENTATION ONE #####

def spiralOrder(inputMatrix):
    numRows = len(inputMatrix)

    numCols = len(inputMatrix[0])

    topRow = 0
    btmRow = numRows - 1
    leftCol = 0
    rightCol = numCols - 1
    result = []

    while (topRow <= btmRow and leftCol <= rightCol):
        # copy the next top row
        for i in range(leftCol, rightCol+1):
            result.append(inputMatrix[topRow][i])
        topRow += 1

        # copy the next right hand side column
        for i in range(topRow, btmRow+1):
            result.append(inputMatrix[i][rightCol])
        rightCol -= 1

        # copy the next bottom row
        if (topRow <= btmRow):
            for i in range(rightCol, leftCol-1, -1):
                result.append(inputMatrix[btmRow][i])
            btmRow -= 1

        # copy the next left hand side column
        if (leftCol <= rightCol):
            for i in range(btmRow, topRow-1, -1):
                result.append(inputMatrix[i][leftCol])
            leftCol += 1

    return result


##### IMPLEMENTATION 2 ######

# This function finds the busiest period of a given data.
def spiralOrderV2(data):

    # Initialize variables
    count = 0
    max_count = 0
    max_time = 0

    # Loop through data
    for i in range(len(data)):
        # Add or subtract count based on data
        if data[i][2] > 0:
            count += data[i][1]
        else:
            count -= data[i][1]

        # Skip if same time
        if i < len(data) - 1 and data[i][0] == data[i+1][0]:
            continue

        # Update max count and time
        if count > max_count:
            max_count = count
            max_time = data[i][0]

    # Return max time
    return max_time



