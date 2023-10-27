
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
        print(f"  PINGS - sent: {sent_count} response: {received_count} loss: {sent_count - received_count}")
        print(f" % LOSS - {100 * (sent_count - received_count)/sent_count:.2f}%")
        print(f"AVG RTT - {avg_rtt:10.2f} ms")
        print(f"MIN RTT - {min_rtt:10.2f} ms")
        print(f"MAX RTT - {max_rtt:10.2f} ms")

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

                print(f"\nSENT - {message}")

                # receive from the socket using `recvfrom`
                response, addr = sock.recvfrom(2048)

                # print the received message

                print(f"RECEIVED - {response.decode()}")

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

                print(f"      RTT - {telapsed:10.2f} ms")
                rtt_stats()

                # fill-2 ends

            except socket.timeout:
                print("TIMEOUT - #" + str(i) + " Requested Time out\n")

    finally:
        print(f"\nclosing socket")
        rtt_stats()

        sock.close()

