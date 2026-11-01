import numpy as np

def calculate(lst):
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(lst).reshape(3, 3)

    funcs = {
        'mean': np.mean,
        'variance': np.var,
        'standard deviation': np.std,
        'max': np.max,
        'min': np.min,
        'sum': np.sum,
    }

    return {
        name: [
            f(matrix, axis=0).tolist(),  # down each column
            f(matrix, axis=1).tolist(),  # across each row
            f(matrix).item(),            # whole matrix
        ]
        for name, f in funcs.items()
    }