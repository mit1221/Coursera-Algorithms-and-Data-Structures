# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    points = []
    while segments != []:
        start_points = [i.start for i in segments]
        max_index = start_points.index(max(start_points))
        if points == [] or segments[max_index].end < points[-1]:
            points.append(segments[max_index].start)
        del segments[max_index]

    for s in segments:
        points.append(s.start)
        points.append(s.end)
    return points


if __name__ == '__main__':
    # input_ = input("Enter: ")
    # n, *data = map(int, input_.split())
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
