import torch
import numpy as np
import matplotlib.pyplot as plt
from src.core import generate_3d_model

def main():
    # Generate a 3D model
    model = generate_3d_model()
    # Plot the model
    plt.plot(model)
    plt.show()
if __name__ == '__main__':
    main()