def priority():
    #         t=  0       1      2     3     4    5      6    7       8
    arrivals = [[1, 2], [3, 4], [6], [5, 7], [], [8, 9], [], [10], [11, 12]]
    leaving = {}

    even_queue = []
    odds_queue = []

    t = 0

    while arrivals or (even_queue or odds_queue):

        if arrivals:
            for item in arrivals.pop(0):
                if item % 2 == 0:
                    even_queue.append((item, t))
                    print(f"Package: {item} Arrived TIME: {t}")
                else:
                    odds_queue.append((item, t))
                    print(f"Package: {item} Arrived TIME: {t}")

        packet = None
        if len(odds_queue) > 0:
            packet = odds_queue.pop(0)
            print(f"Packet {packet[0]} (ODD) leaving  TIME: {t}     even_queue: {len(even_queue)}   odds_queue: {len(odds_queue)}")
        elif len(even_queue) > 0:
            packet = even_queue.pop(0)
            print(f"Packet {packet[0]} (EVEN) leaving TIME: {t}     even_queue: {len(even_queue)}   odds_queue: {len(odds_queue)}")

        if packet:
            leaving[packet[0]] = [packet[1], t]

        t += 1

    print()
    for i in range(1, len(leaving) + 1):
        packet = leaving[i]
        print(f"packet: {i}  arrival: {packet[0]}   leaving: {packet[1]}   delay: {packet[1] - packet[0]}")


    print()
    for i in range(1, len(leaving) + 1):
        packet = leaving[i]
        print(f"{i} {packet[0]} {packet[1]} {packet[1] - packet[0]}")
