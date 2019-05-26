#In the name of the Almighty God

import numpy as np


def Solution(N, R, C, SR, SC, INS):
    # Get the present position
    # grid

    TheGrid = boxMatrix(C, R)

    present_posR = SR - 1
    present_posC = SC - 1

    actualPos = TheGrid[present_posR][present_posC] = 1

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
        TheGrid[present_posR][present_posC] = 1

    return "{} {}".format(present_posR + 1, present_posC + 1)


def boxMatrix(R, C):
    npMax = np.zeros((C, R))
    return npMax


T = int(input())
for i in range(1, T+1):
    N = int(input())
    R = int(input())
    C = int(input())
    SR = int(input())
    SC = int(input())
    INS = input()

    print('Case #{}: {}'.format(i, Solution(N,R,C,SR,SC,INS)))
