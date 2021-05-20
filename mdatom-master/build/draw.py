from os import posix_fallocate
import sys
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
import numpy as np
import math
import time

def getNewPositions(frameNumber, *fargs):

    positions, numSamples, numAtoms, boxSize = fargs


    offset = 3*numAtoms * (frameNumber)


    xVals = [positions[x]   for x in range(offset, offset+numSamples*3, 3)]
    yVals = [positions[x+1] for x in range(offset, offset+numSamples*3, 3)]
    zVals = [positions[x+2] for x in range(offset, offset+numSamples*3, 3)]

    print("Currently at " + str(offset/len(positions)*100) + "%")

    ax = plt.axes(projection="3d")

    ax.set_xlim3d((0, boxSize))
    ax.set_ylim3d((0, boxSize))
    ax.set_zlim3d((0, boxSize))

    ax.set_xlabel("x")

    return ax.scatter(xVals, yVals, zVals)



def animatePositions(file, numAtoms=1000):


    numSamples = 1000

    boxSize = 10.436    

    positions = pd.read_csv(file, header=None, skiprows=1, dtype=float).to_numpy().flatten()


    fig = plt.figure()

    frameCount = math.floor(len(positions) / (3*numAtoms))

    animation = FuncAnimation(fig, getNewPositions, frames = frameCount, fargs=[positions, numSamples, numAtoms, boxSize])

    animation.save("molecule_simulation.mp4", writer="ffmpeg", fps=math.floor(frameCount/5))


def main():

    print("Started with drawing...")

    tStart = time.time()

    filename = sys.argv[1]

    animatePositions(filename)

    print("Ended drawing. \n Drawing took " + str(time.time() - tStart) + " seconds")



if __name__ == "__main__":
    main()