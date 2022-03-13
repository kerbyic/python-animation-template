import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# This is mock data to move a dot in a circle. Replace this with whatever system state data you want to show.
rad = np.linspace(0,6*np.pi,3000)
xhistory = np.cos(rad)
yhistory = np.sin(rad)

# Create the figure for animation. Use this to adjust the size and resolution of the output file (may take experimentation).
fig, ax = plt.subplots(figsize=(5,5)) # Change fig size to adjust size of figure
fig.set_dpi(150.0) # Change this to adjust resolution.

# Setup the framerate and evenly pick frames across the available history for target framerate and time
time = 10 # Time for animation in seconds. Replace with your target time.
framerate = 30 # Frames per second. Replace with your target rate.
nframes = len(xhistory)-1 # Total length of list/tuple that contains data. This could be any list/tuple as long as they are all the same size.
frames = np.linspace(0, nframes, int(time*framerate), dtype=int) # Frame indices to use in the animation. Shouldn't need to edit this line.

# Define how to animate a frame given the index by replacing the contents of this function. 
# This is all setup the same way you'd make a normal plot.
# It'll use index 'i' to choose from your system history.
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
anim = animation.FuncAnimation(fig, animate, frames = frames, interval=1/framerate*1000) # Don't change this line
anim.save('DotAnimation.mp4') # Change name to what you want. It'll automatically change file type given appropriate suffix.
