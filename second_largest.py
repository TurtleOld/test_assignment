def second_largest(listing):
    if len(listing) < 2:
        return int(''.join(map(str, listing)))
    elif len(listing) == 0:
        return None
    return sorted(listing)[1]


print(second_largest([61,32,68,36,73,3,34]))
print(second_largest([1,2]))
print(second_largest([2]))
