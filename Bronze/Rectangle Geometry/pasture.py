import sys


def main():
    sys.stdin = open("Bronze/Rectangle Geometry/square.in", "r")
    sys.stdout = open("Bronze/Rectangle Geometry/square.out", "w")
    rectangle_1 = list(map(int, input().split()))
    rectangle_2 = list(map(int, input().split()))
    max_x2 = max(rectangle_1[2], rectangle_2[2])
    max_y2 = max(rectangle_1[3], rectangle_2[3])
    min_x1 = min(rectangle_1[0], rectangle_2[0])
    min_y1 = min(rectangle_1[1], rectangle_2[1])
    answer = (max((max_x2-min_x1), (max_y2-min_y1)))
    answer = answer * answer
    return answer


print(main())
