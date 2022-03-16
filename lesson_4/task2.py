def process_packages(size, packages):
    queue = [None] * size
    time = 0
    tail = 0
    process_end = 0

    for arrival, duration in packages:
        if time < arrival:
            time = arrival

        if process_end < time:
            # print(queue)
            del queue[0]
            queue.append(None)
            tail -= 1

            if queue[0] is not None:
                process_end = time + queue[0]

        if queue[-1] is not None:
            # очередь заполнена
            yield -1
        else:
            yield time
            queue[tail] = duration
            tail += 1


if __name__ == '__main__':
    assert tuple(process_packages(1, [[0, 0]])) == (0,)
    print(tuple(process_packages(1, [[0, 1], [0, 1]])))
    assert tuple(process_packages(1, [[0, 1], [0, 1]])) == (0, -1)
    print(tuple(process_packages(1, [[0, 1], [1, 1]])))
    assert tuple(process_packages(1, [[0, 1], [1, 1]])) == (0, 1)
