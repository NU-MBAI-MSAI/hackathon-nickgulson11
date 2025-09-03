import matplotlib.pyplot as plt
import numpy as np

def model_one():
    x = np.arange(-2.0, 2.0, .01)
    # y = np.sin( 2* np.pi * x)
    y = []
    for i in x:
        num = i**2 - 1
        y.append(num)
    plt.plot(x, y, "o")
    plt.xlabel('time (s)')
    plt.ylabel('volts (mV)')
    plt.show()

if __name__ == "__main__":
    model_one()