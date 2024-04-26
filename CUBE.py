>>> import matplotlib.pyplot as plt
... import numpy as np
... 
... # First five cubic numbers
... x = np.arange(1, 6)
... y = x ** 3
... 
... plt.figure(figsize=(10, 5))
... 
... plt.subplot(1, 2, 1)
... plt.bar(x, y, color='blue')
... plt.title('First Five Cubic Numbers')
... plt.xlabel('Number')
... plt.ylabel('Cube')
... 
... # First 5000 cubic numbers
... x_5000 = np.arange(1, 5001)
... y_5000 = x_5000 ** 3
... 
... plt.subplot(1, 2, 2)
... plt.scatter(x_5000, y_5000, c=y_5000, cmap='viridis')
... plt.colorbar(label='Cube')
... plt.title('First 5000 Cubic Numbers')
... plt.xlabel('Number')
... plt.ylabel('Cube')
... 
... plt.tight_layout()
... plt.show()
