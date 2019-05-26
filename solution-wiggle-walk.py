#In The Name Of Almighty God
import numpy as np

def Solution(N, R, C, SR, SC, INS):
    # Get the present position
    # grid
    TheGrid = boxMatrix(C, R)

    # Get the initial positions
    present_posR = SR - 1
    present_posC = SC - 1

    # Mark the current position to ensure not staying there again
    TheGrid[present_posR][present_posC] = 1

    # Check the instructions and Navigate the Bot
    for i in range(0, N):
        if INS[i] == "N":
            present_posR -= 1
        elif INS[i] == "S":
            present_posR += 1
        elif INS[i] == "W":
            present_posC -= 1
        else:
            present_posC += 1

        actualPos = TheGrid[present_posR][present_posC]

        # If the current postion has be stayed before, keep moving,
        while(actualPos == 1):
            if INS[i] == "N":
                present_posR -= 1
            elif INS[i] == "S":
                present_posR += 1
            elif INS[i] == "W":
                present_posC -= 1
            else:
                present_posC += 1

            actualPos = TheGrid[present_posR][present_posC]

        # Mark the current position to ensure not staying there again        
        TheGrid[present_posR][present_posC] = 1

    return "{} {}".format(present_posR + 1, present_posC + 1)

# define the Matrix Give rows and cols
def boxMatrix(R, C):
    npMax = np.zeros((C, R))
    return npMax

# Get the input according to the test instructions
T = int(input())
for i in range(1, T+1):
    NRCSRSRINS = list(map(int, input().split(" ")))
    INS = input()

    print('Case #{}: {}'.format(i, Solution(
        NRCSRSRINS[0], NRCSRSRINS[1], NRCSRSRINS[2], NRCSRSRINS[3], NRCSRSRINS[4], INS)))
