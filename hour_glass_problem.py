"""
Hour Glass problem:


Output : 

[
  [18, 25, 3, 4],
  [38, 45, 7, 8],
  [1, 2, 3, 4],
  [5, 6, 7, 8]
]
"""



def do_process(array_data, i, j):
    sum_val = 0
    if not j and len(array_data[i:][:3]) == 3:
        data = array_data[i:][:3]
        for itr in range(0, len(data)):
            if itr != 1:
                sum_val += sum(data[itr][j:][:3])
            else:
                sum_val += (data[itr][j+1])
        array_data[i][j] = sum_val
        array_data = do_process(array_data, i+1, 0)
    elif j and len(array_data[i:][:3]) == 3:
        data = array_data[i:][:3]
        for itr in range(0, len(data)):
            if itr != 1:
                sum_val += sum(data[itr][j:][:3])
            else:
                sum_val += (data[itr][j+1])
        array_data[i][j] = sum_val
        array_data = do_process(array_data, i+1, j)
    elif not j:
        array_data = do_process(array_data, 0, 1)
    return array_data


if __name__ == '__main__':
    data_array = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [1, 2, 3, 4],
        [5, 6, 7, 8],
    ]
    print(do_process(data_array, 0, 0))
