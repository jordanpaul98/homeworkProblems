
def Client(ipAddress):
    import socket
    import time

    # Fill-1
    # create an UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Specify server address and port number
    server_addr = (ipAddress, 12000)

    # set timeout for the socket
    sock.settimeout(4)

    # Fill-1 ends

    try:
        for i in range(10):
            start = time.perf_counter_ns()
            message = 'Ping #' + str(i) + " " + time.ctime(time.time())
            try:
                # Fill-2: do a send and receive

                # send to the socket using `sendto`

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

                # print RTT

                print(f"RTT: {telapsed}us")

                # fill-2 ends

            except socket.timeout:
                print("#" + str(i) + " Requested Time out\n")

    finally:
        print("closing socket")
        sock.close()

