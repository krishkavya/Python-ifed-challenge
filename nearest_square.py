def nearest_square(limit):
    if limit < 0:
        return 0
    
    while limit > 3:
        i = 2
        while i <= limit//2:
            square = i*i
            if square == limit:
                return square
            else:
                i += 1
        limit -= 1
    return 1
    