import numpy as np

def calculate(input_list):
    try:
        if len(input_list) != 9:
            raise ValueError("List must contain nine numbers.")
        
        np_array = np.array(input_list).reshape(3,3)
        result = {}

        result.update({"mean": [np.mean(np_array, axis=0).tolist(),np.mean(np_array, axis=1).tolist(),float(np.mean(np_array))]})
        result.update({"variance": [np.var(np_array, axis=0).tolist(),np.var(np_array, axis=1).tolist(),float(np.var(np_array))]})
        result.update({"standard deviation": [np.std(np_array, axis=0).tolist(),np.std(np_array, axis=1).tolist(),float(np.std(np_array))]})
        result.update({"max": [np.max(np_array, axis=0).tolist(),np.max(np_array, axis=1).tolist(),int(np.max(np_array))]})
        result.update({"min": [np.min(np_array, axis=0).tolist(),np.min(np_array, axis=1).tolist(),int(np.min(np_array))]})
        result.update({"sum": [np.sum(np_array, axis=0).tolist(),np.sum(np_array, axis=1).tolist(),int(np.sum(np_array))]})
        
        return result


    except ValueError as e:
        raise e