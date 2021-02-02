objects = [1, 2, 1, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 55, 67, 77777, 7, 7, 7, 7, 7]
ans = 0
current = []
for obj in objects:
    if obj not in current:
        current.append(obj)
        ans += 1
print(ans)

print(len(set(map(id, objects))))