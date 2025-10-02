# Two parts of a floor need tiling. One part is 9 tiles wide by 7 tiles long, 
# the other is 5 tiles wide by 7 tiles long. Tiles come in packages of 6.

#     How many tiles are needed?
#     You buy 17 packages of tiles containing 6 tiles each. How many tiles will be left over?

part1 = 9 * 7
part2 = 5 * 7
total = part1 + part2

print(total)

tile_pack = 6
purchase_tile = 17

print(purchase_tile * tile_pack - total)
