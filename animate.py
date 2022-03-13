import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# This is mock data to move a dot in a circle. Replace this with whatever system state data you want to show.
rad = np.linspace(0,6*np.pi,3000)
xhistory = np.cos(rad)
yhistory = np.sin(rad)

# Create the figure for animation
# Use this to adjust the size and resolution of the output file
fig, ax = plt.subplots(figsize=(5,5))
fig.set_dpi(150.0)

# Setup the framerate and evenly pick frames across the available history for target framerate and time
time = 10 # time for animation in seconds
framerate = 144 # frames per second
nframes = len(xhistory)-1 # total number of saved system states
frames = np.linspace(0, nframes, int(time*framerate), dtype=int) # frame indices to use in the animation

# Define how to animate a frame given the index. This is all setup the same way you'd make a normal plot.
def animate(i):
    
    ax.clear() # clear the plot so previous frames don't show up again
    coordinate = (xhistory[i], yhistory[i]) # get the coordinates of the dot at a given time in history
    diameter = 0.5 # set the size of the dot
    ax.add_artist(plt.Circle(coordinate, diameter, facecolor='tab:green')) # plot the dot
    ax.set_ylim(-2,2) # set axis bondaries and aspect ratio
    ax.set_xlim(-2,2)
    ax.set_aspect('equal')
    
    fig.tight_layout() # tight layout so it looks nicer (assuming there are things to arrange)
    
# Create the animation and save to file. Recommend mp4 over gif (faster render and smaller file size), but requires ffmpeg.
anim = animation.FuncAnimation(fig, animate, frames = frames, interval=1/framerate*1000)
anim.save('DotAnimation.mp4')
