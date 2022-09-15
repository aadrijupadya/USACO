import sys
fin, fout = open("billboard.in"), open(
    "billboard.out", "w")

x1, y1, x2, y2 = (map(int, fin.readline().split()))
x3, y3, x4, y4 = (map(int, fin.readline().split()))
if x1 <= x3 <= x2 and y1 <= y3 <= y2 and x1 <= x4 <= x2 and y1 <= y4 <= y2:
    fout.write(str(0))

list1 = [x1, y1, x2, y2]
list2 = [x2, y3, x4, y4]


def intersect(s1, s2) -> bool:
    bl_a_x, bl_a_y, tr_a_x, tr_a_y = s1[0], s1[1], s1[2], s1[3]
    bl_b_x, bl_b_y, tr_b_x, tr_b_y = s2[0], s2[1], s2[2], s2[3]

    if (bl_a_x >= tr_b_x or tr_a_x <= bl_b_x
            or bl_a_y >= tr_b_y or tr_a_y <= bl_b_y):
        return False
    else:
        return True


if not intersect:
    a = (x2-x1) * (y2-y1)
    fout.write(str(a))

if intersect:
    if (y3 == y1 and y2 == y4):
        print('oho')
        a = abs(x3-x2) * abs(y2-y3)
    elif (x1 == x3 and x2 == x4):
        print('yema')
        a = (abs(y3-y2) * abs(x2-x1))
    else:
        a = (x2-x1) * (y2-y1)
        fout.write(str(a))
