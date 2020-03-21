for name_1 in names_1: # O(n)
    for name_2 in names_2: # O(n)
        if name_1 == name_2:
            duplicates.append(name_1)
