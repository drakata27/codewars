def count_triangles(n):
    if n < 1 or n > 100:
        return 'Invalid input'
    return 3 * n ** 3 + 9 * n ** 2 // 2 + n

print(count_triangles(3))