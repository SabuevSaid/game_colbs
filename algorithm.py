def are_elements_equal(value_colors_in_colbs, index1, index2):
    array1 = value_colors_in_colbs[index1] if len(value_colors_in_colbs)>0 else [[]]
    array2 = value_colors_in_colbs[index2] if len(value_colors_in_colbs)>0 else [[]]
    return array1[0][0] == array2[0][0]

def check_free_space(colb, n):
    return len(colb) < n