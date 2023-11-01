def sort(*args):
    ns = sorted([num for num in args if num < 0], reverse=True)
    ps = sorted([num for num in args if num >= 0])
    return (ns, ps)

r = sort(-5, 10, -3, 0, 8, -1)
print(r)  # ([-1, -3, -5], [0, 8, 10])
