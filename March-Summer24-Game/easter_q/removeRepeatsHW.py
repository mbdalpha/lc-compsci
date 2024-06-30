import random

drum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(0, 6):
    draw_index = random.randint(0, len(drum)-1)
    draw = drum[draw_index]
    drum.remove(draw)
    print(draw)