"""The aim here is to replicate Conway's game of life. Why you ask? Dude..it's so cool man
    I happened to stumble upon it a couple of times in the last week. I think it's the universe's 
    message. I am being willed into doing this xD """

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import argparse

# Make sure you understand what you're doing in this one. Don't be a bitch

# If a cell is on its value will be 255
# If it's off, its value will be 0
ON = 255
OFF = 0
vals = list(ON,OFF)

