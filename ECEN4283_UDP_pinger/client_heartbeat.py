
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
        print(f"[CLIENT]  pings sent: {sent_count} ping responses: {received_count}  Packet Loss: {sent_count - received_count}")
        print(f"[CLIENT]  Packet Loss Percent {100 * (sent_count - received_count)/sent_count:5.2f}%")
        print(f"[CLIENT]  Heartbeat Reported Losses: {reported_losses}")
        print(f"[CLIENT]  Average RTT: {avg_rtt:8.2f} us")
        print(f"[CLIENT]  Minimum RTT: {min_rtt:8.2f} us")
        print(f"[CLIENT]  Maximum RTT: {max_rtt:8.2f} us")

    min_rtt, max_rtt, avg_rtt = float('inf'), 0, 0
    sent_count, received_count = 0, 0
    ping_amount = 10

    reported_losses = 0

    def send_heartbeat():
        nonlocal reported_losses
        heart_beat_message = f'heartbeat,{sent_count - 1},{time.time()}'
        try:
            sock.sendto(heart_beat_message.encode(), server_addr)
            response, addr = sock.recvfrom(2048)
            response = response.decode()

            message, losses = response.split(',')
            reported_losses += int(losses)
        except socket.timeout:
            pass

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

                print("[CLIENT]  ", message)

                # receive from the socket using `recvfrom`
                response, addr = sock.recvfrom(2048)

                # print the received message

                print("[CLIENT]  ", response.decode())

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

                print(f"[CLIENT]  RTT: {telapsed} us")
                rtt_stats()

                # fill-2 ends

            except socket.timeout:
                print("[CLIENT]  #" + str(i) + " Requested Time out\n")

            # send a heart beat after each message
            send_heartbeat()

    finally:
        print(f"\n[CLIENT]  closing socket")
        rtt_stats()

        sock.close()

