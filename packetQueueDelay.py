'''
Jordan Paul 
Homework problem P.6 part A, B, C, D

       2    4         7         9              12
a ->   1    3    6    5         8         10   11    (arriving)
t ->   0 -- 1 -- 2 -- 3 -- 4 -- 5 -- 6 -- 7 -- 8 -- 9 -- ....
l ->      1 ....                                     (leaving)    

Assuming FIFO service, indicate the time at which packet 2 trhough 12 each leave the queue.
for each packet, what is the delay between its arrival and transmitted
'''
def fifo():
    arrivals = [[1, 2], [3, 4], [6], [5, 7], [], [8, 9], [], [10], [11, 12]]

    queue = []
    leaving = {}

    t = 0

    while arrivals or queue:
        if arrivals:
            for item in arrivals.pop(0):
                queue.append([item, t])
                print(f"Package: {item} Arrived TIME: {t}")

        if queue:
            packet, arrive = queue.pop(0)
            leaving[packet] = [arrive, t]
            print(f"Packet {packet}  leaving TIME: {t}   queue: {len(queue)}")

        t += 1

    print("")
    leaving = {packet: leaving[packet] for packet in range(1, len(leaving) + 1)}

    avg_dly = 0
    for packet, leave in leaving.items():
        arrive, depart = leave
        print(f"packet: {packet}  arrival: {arrive}   leaving: {depart}   delay: {depart - arrive}")
        avg_dly += depart - arrive

    print("Average delay: ", round(avg_dly / len(leaving), 4))

'''
Now assume a priority service, and assume that odd-numbered packets are high prioroty, and
even-numbered packets are low priority
'''
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

'''
Now assume round robin server. Assume that packets 1, 2, 3, 4, 6, 11, 12 are from class 1,
and packets 4, 5, 7, 8, 9, 10 are from class 2
'''
def round_robin():
    #         t=  0       1      2     3     4    5      6    7       8
    arrivals = [[1, 2], [3, 4], [6], [5, 7], [], [8, 9], [], [10], [11, 12]]

    class1 = [1, 2, 3, 6, 11, 12]
    class2 = [4, 5, 7, 8, 9, 10]
    class_n = []

    for c1, c2 in zip(class1, class2):
        class_n.extend([c1, c2])

    queue = {}
    leaving = []

    t = 0

    while arrivals or class_n:
        if arrivals:
            for item in arrivals.pop(0):
                queue[item] = t
                print(f"Package: {item} Arrived TIME: {t}")


        if class_n and class_n[0] in queue:
            c = class_n.pop(0)

            packet = [c, queue.pop(c), t]

            leaving.append(packet)

            print(f"Packet {c} Leaving:    TIME: {t}      queue: {len(queue)}")


        t += 1

    ordered = {}
    for packet_leaving in leaving:
        packet, arrive, leave = packet_leaving
        ordered[packet] = [arrive, leave]

    print("\n")
    for i in range(1, len(ordered) + 1):
        arrive, leave = ordered[i]
        print(f"packet: {i}  arrival: {arrive}   leaving: {leave}   delay: {leave - arrive}")

'''
Now assume weighted fair queuing (WFQ) service. Assume that odd-numbered packets are from class 1,
and even0numbered packes are from class 2. Class 1 has weight of 2, while class 2 has WFG weight of 1

#NOTE think this isnt fully done correctly
'''
def weighted_fair():
    #         t=  0       1      2     3     4    5      6    7       8
    arrivals = [[1, 2], [3, 4], [6], [5, 7], [], [8, 9], [], [10], [11, 12]]

    class1 = [1, 3, 5, 7, 9, 11]
    class2 = [2, 4, 6, 8, 10, 12]

    weight1, weight2 = 2, 1

    queue = {}
    leaving = []

    weight = {}

    t = 0

    while arrivals or (class1 or class2):
        if arrivals:
            for item in arrivals.pop(0):
                queue[item] = t
                print(f"Package: {item} Arrived TIME: {t}")

        if class1 and class1[0] in queue and class1[0] // weight1 < class2[0] // weight2:
            c = class1.pop(0)
            packet = [c, queue.pop(c), t]
            leaving.append(packet)
            print(f"Packet {c} Leaving:    TIME: {t}      queue: {len(queue)}")
        elif class2 and class2[0] in queue:
            c = class2.pop(0)
            packet = [c, queue.pop(c), t]
            leaving.append(packet)
            print(f"Packet {c} Leaving:    TIME: {t}      queue: {len(queue)}")

        t += 1

    ordered = {}
    for packet_leaving in leaving:
        packet, arrive, leave = packet_leaving
        ordered[packet] = [arrive, leave]

    print("\n")
    for i in range(1, len(ordered) + 1):
        arrive, leave = ordered[i]
        print(f"packet: {i}  arrival: {arrive}   leaving: {leave}   delay: {leave - arrive}")




