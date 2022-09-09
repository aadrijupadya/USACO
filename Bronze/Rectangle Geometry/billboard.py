import sys


class Rect:
    def __init__(self):
        self.x1, self.y1, self.x2, self.y2 = map(int, input().split())

    def area(self):
        return (self.y2 - self.y1) * (self.x2 - self.x1)


def intersect(p, q):
    x_overlap = max(0, min(p.x2, q.x2) - max(p.x1, q.x1))
    y_overlap = max(0, min(p.y2, q.y2) - max(p.y1, q.y1))
    return x_overlap * y_overlap


sys.stdin = open("billboard.in", "r")
sys.stdout = open("billboard.out", "w")

rects = []
for _ in range(3):
    rects.append(Rect())

print(rects[0].area() + rects[1].area() -
      intersect(rects[0], rects[2]) - intersect(rects[1], rects[2]))

# area function
# def area(bl_x: int, bl_y: int, tr_x: int, tr_y: int) -> int:
#     	length = tr_y - bl_y
# 	width = tr_x - bl_x
# 	return length * width

# checking for intersection
# def intersect(s1, s2) -> bool:
#     	bl_a_x, bl_a_y, tr_a_x, tr_a_y = s1[0], s1[1], s1[2], s1[3]
# 	bl_b_x, bl_b_y, tr_b_x, tr_b_y = s2[0], s2[1], s2[2], s2[3]

# 	# no overlap
# 	if (bl_a_x >= tr_b_x or tr_a_x <= bl_b_x
# 			or bl_a_y >= tr_b_y or tr_a_y <= bl_b_y):
# 		return False
# 	else:
# 		return True
# finding area of intersection
# def inter_area(s1, s2) -> int:
#     	bl_a_x, bl_a_y, tr_a_x, tr_a_y = s1[0], s1[1], s1[2], s1[3]
# 	bl_b_x, bl_b_y, tr_b_x, tr_b_y = s2[0], s2[1], s2[2], s2[3]

# 	return (
# 		(min(tr_a_x, tr_b_x) - max(bl_a_x, bl_b_x))
# 		* (min(tr_a_y, tr_b_y) - max(bl_a_y, bl_b_y))
# 	)
