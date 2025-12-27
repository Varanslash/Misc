finalTileData = []

base = input("Enter tile data here: ").split()
for item in base:
    if "$" not in item:
        newtile = "$" + item + ", "
        finalTileData.append(newtile)
    else:
        newtile = item + ", "
        finalTileData.append(newtile)

finalTileData[-1] = finalTileData[-1][:-2]  # Remove the last comma and space


print("    db " + "".join(finalTileData))