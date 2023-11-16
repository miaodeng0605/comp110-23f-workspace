def value_exists(test_dict: dict[str, int], val: int) -> bool:
    for elem in test_dict:
        if test_dict[elem] == val:
            return True
    return False
        
