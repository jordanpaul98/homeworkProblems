
def Client(ipAddress):
    import socket
    import time

    # Fill-1
    # create an UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Specify server address and port number
    server_addr = (ipAddress, 12000)

    # set timeout for the socket
    sock.settimeout(1)

    # Fill-1 ends

    # Extra

    def rtt_stats():
        print(f"pings sent: {sent_count} ping responses: {received_count}  Packet Loss: {sent_count - received_count}")
        print(f"Packet Loss Percent {100 * (sent_count - received_count)/sent_count:5.2f}%")
        print(f"Average RTT: {avg_rtt:8.2f}us")
        print(f"Minimum RTT: {min_rtt:8.2f}us")
        print(f"Maximum RTT: {max_rtt:8.2f}us")

    min_rtt, max_rtt, avg_rtt = 2 ** 63, 0, 0
    sent_count, received_count = 0, 0
    ping_amount = 10


    try:
        for i in range(ping_amount):
            start = time.perf_counter_ns()
            message = 'Ping #' + str(i) + " " + time.ctime(time.time())
            try:
                # Fill-2: do a send and receive

                # send to the socket using `sendto`
                sent_count += 1
                sock.sendto(message.encode(), server_addr)

                # print the sent message

                print(message)

                # receive from the socket using `recvfrom`
                response, addr = sock.recvfrom(2048)

                # print the received message

                print(response.decode())

                # store current time to `endt`

                endt = time.perf_counter_ns()

                # compute the elapsed time
                telapsed = (endt - start)/1000

                # compute max and min RTT
                min_rtt = min((min_rtt, telapsed))
                max_rtt = max((max_rtt, telapsed))

                # compute the average RTT with rolling average
                avg_rtt = (received_count * avg_rtt + telapsed) / (received_count + 1)
                received_count += 1

                # print RTT

                print(f"RTT: {telapsed}us")
                rtt_stats()

                # fill-2 ends

            except socket.timeout:
                print("#" + str(i) + " Requested Time out\n")

    finally:
        print(f"\nclosing socket")
        rtt_stats()

        sock.close()

