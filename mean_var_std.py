import numpy as np

def calculate(list_of_digits):
    matrix = np.array(list_of_digits).reshape(3, 3)
    
    # Calculate statistics
    mean_rows = np.mean(matrix, axis=1)
    mean_cols = np.mean(matrix, axis=0)
    mean_elements = np.mean(matrix)
    
    var_rows = np.var(matrix, axis=1)
    var_cols = np.var(matrix, axis=0)
    var_elements = np.var(matrix)
    
    std_rows = np.std(matrix, axis=1)
    std_cols = np.std(matrix, axis=0)
    std_elements = np.std(matrix)
    
    max_rows = np.max(matrix, axis=1)
    max_cols = np.max(matrix, axis=0)
    max_elements = np.max(matrix)
    
    min_rows = np.min(matrix, axis=1)
    min_cols = np.min(matrix, axis=0)
    min_elements = np.min(matrix)
    
    sum_rows = np.sum(matrix, axis=1)
    sum_cols = np.sum(matrix, axis=0)
    sum_elements = np.sum(matrix)
    
    # Return results as a dictionary
    calculations = {
        'mean': [mean_rows.tolist(), mean_cols.tolist(), mean_elements],
        'variance': [var_rows.tolist(), var_cols.tolist(), var_elements],
        'standard deviation': [std_rows.tolist(), std_cols.tolist(), std_elements],
        'max': [max_rows.tolist(), max_cols.tolist(), max_elements],
        'min': [min_rows.tolist(), min_cols.tolist(), min_elements],
        'sum': [sum_rows.tolist(), sum_cols.tolist(), sum_elements]
    }
    
    return calculations


digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = calculate(digits)
print(result)

