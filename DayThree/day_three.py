map_file = open("map.txt", "r")

# Part One

index = 0
tree_count = 0
row_list = map_file.read().split('\n')

for row in row_list:
    if row[index] == "#":
        tree_count = tree_count + 1
    index = (index + 3) % len(row)

print("Part one:", tree_count)


# Part Two

def findTreeBySlope(right, rows):
    index = 0
    tree_count = 0
    for row in rows:
        if row[index] == "#":
            tree_count = tree_count + 1
        index = (index + right) % len(row)
    return tree_count


print("Part Two:", findTreeBySlope(1, row_list) * findTreeBySlope(3, row_list) *
      findTreeBySlope(5, row_list) * findTreeBySlope(7, row_list) * findTreeBySlope(1, row_list[::2]))
