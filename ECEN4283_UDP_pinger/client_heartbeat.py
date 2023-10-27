
def Client(ipAddress):
    import socket
    import time
    import random

    # Fill-1
    # create an UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Specify server address and port number
    server_addr = (ipAddress, 12000)

    # set timeout for the socket
    sock.settimeout(1)

    def rtt_stats():
        print(f"[CLIENT]     PINGS - sent: {sent_count} response: {received_count} loss: {sent_count - received_count}")
        print(f"[CLIENT]    % LOSS - {100 * (sent_count - received_count)/sent_count:.2f}%")
        print(f"[CLIENT]  LOST SEQ - {lost_packets}")
        print(f"[CLIENT]   AVG RTT - {avg_rtt:10.2f} ms")
        print(f"[CLIENT]   MIN RTT - {min_rtt:10.2f} ms")
        print(f"[CLIENT]   MAX RTT - {max_rtt:10.2f} ms")

    min_rtt, max_rtt, avg_rtt = float('inf'), 0, 0
    sent_count, received_count = 0, 0

    lost_packets = []

    def send_heartbeat():
        heart_beat_message = f'heartbeat,{sent_count},{time.time_ns()}'
        try:
            time.sleep((25 + random.randint(0, 10))/1000) # adding some random delay to packet

            sock.sendto(heart_beat_message.encode(), server_addr)
            print(f"\n[CLIENT]  SENT - Heartbeat")
            response, addr = sock.recvfrom(2048)
            response = response.decode()

            import ast
            message, losses = response.split(':')
            lost_packets.extend([seq for seq in ast.literal_eval(losses) if seq not in lost_packets])
        except socket.timeout:
            pass

    try:
        for i in range(10):
            start = time.perf_counter_ns()
            message = 'Ping #' + str(i) + " " + time.ctime(time.time())
            try:
                # Fill-2: do a send and receive

                # send to the socket using `sendto`
                sent_count += 1
                time.sleep((25 + random.randint(0, 10)) / 1000)  # adding some random delay to packet
                sock.sendto(message.encode(), server_addr)

                # print the sent message

                print(f"\n[CLIENT]      SENT - {message}")

                # receive from the socket using `recvfrom`
                response, addr = sock.recvfrom(2048)

                # print the received message

                print(f"[CLIENT]  RECEIVED - {response.decode()}")

                # store current time to `endt`

                endt = time.perf_counter_ns()

                # compute the elapsed time
                telapsed = (endt - start)/10 ** 6

                # compute max and min RTT
                min_rtt = min((min_rtt, telapsed))
                max_rtt = max((max_rtt, telapsed))

                # compute the average RTT with rolling average
                avg_rtt = (received_count * avg_rtt + telapsed) / (received_count + 1)
                received_count += 1

                # print RTT
                print(f"[CLIENT]       RTT - {telapsed:10.2f} ms")
                rtt_stats()

                # fill-2 ends

            except socket.timeout:
                print("[CLIENT]   TIMEOUT - #" + str(i) + " Requested Time out")

            # send a heart beat after each message
            send_heartbeat()

    finally:
        print(f"\n[CLIENT]  closing socket")
        rtt_stats()

        sock.close()
