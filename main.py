import multiprocessing
from tqdm import tqdm

def function_to_parallelize(params): 
    param1 = params['param1']
    param2 = params['param2']

    result = {}
    result['sum'] = param1+param2
    
    return result
    
# This chooses all cores except 2, unless there are only two or less cores. 
NCPU = multiprocessing.cpu_count() - 2 if multiprocessing.cpu_count() > 2 else 1

X_values = [10,22,35,4,532,12,42,53,23]
params = ({
    'param1': x,
    'param2': 15
} for x in X_values)

with multiprocessing.Pool(processes=NCPU) as p:    
    
    MAX_COUNT = len(X_values)
    
    for res in tqdm(p.imap(function_to_parallelize, params),total=MAX_COUNT):
        if res is not None:
            print(res['sum'])
