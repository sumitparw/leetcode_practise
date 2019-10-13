points = [[3, 3], [5, -1], [-2, 4]]
K = 2
points.sort(key = lambda P: P[0]**2 + P[1]**2)
print(points[:K])