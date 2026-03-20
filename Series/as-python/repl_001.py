import numpy as np

print(np.array([1, 2, 3]))
try:
    1 / 0
except ZeroDivisionError as error:
    print(f"Error: {error}")
