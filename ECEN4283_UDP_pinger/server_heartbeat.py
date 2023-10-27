
def Server(ipAddress):
    import random
    from socket import socket, AF_INET, SOCK_DGRAM, timeout
    from threading import Thread
    import time
    # UDPPingerServer.py
    # We will need the following module to generate randomized lost packets

    # Create a UDP socket
    # Notice the use of SOCK_DGRAM for UDP packets
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    # Assign IP address and port number to socket
    serverSocket.bind((ipAddress, 12000))
    serverSocket.settimeout(6)
    print("[SERVER]  Started UDP server on port 12000")

    last_response = time.time_ns()
    last_sequence = 0

    keep_alive = True

    def monitor_heartbeat():
        nonlocal keep_alive
        while True:
            if (time.time() - last_response) > 5:
                print("\n[SERVER]  Client stopped responding after 5 seconds stopping server")
                keep_alive = False
                break
            time.sleep(0.01)

    Thread(target=monitor_heartbeat, daemon=True).start()

    while keep_alive:
        # Receive the client packet along with the address it is coming from
        try:
            message, address = serverSocket.recvfrom(1024)
            message = message.decode()

            if "Ping" in message:

                #print("[SERVER]  Ping Message Received")

                # Capitalize the message from the client
                items = message.split(" ")
                message = message.upper()

                # If rand is less is than 4, we consider the packet lost and do not respond
                rand = random.randint(0, 10)
                if rand < 4:
                    continue

                # record the sequence if we actually "Acknowledge" the message
                last_sequence = int(items[1].replace("#", "")) + 1

                # Otherwise, the server responds
                time.sleep((25 + random.randint(0, 10)) / 1000)  # adding some random delay to packet
                serverSocket.sendto(message.encode(), address)

            elif "heartbeat" in message:

                print("\n[SERVER]  Heartbeat Message Received")

                body, sequence, time_stamp = message.split(',')
                last_response = float(time_stamp) / 10 ** 9

                if False:
                    print(f"[SERVER]  sequence received: {sequence}"
                          f"  current sequence: {last_sequence}"
                          f"  Timestamp: {last_response}")

                transport_delay = time.time_ns() - float(time_stamp)
                missing_packets = [i for i in range(last_sequence, int(sequence))]

                print(f"[SERVER]  Transport delay - {(transport_delay)/10**6} ms")
                if missing_packets:
                    print(f"[SERVER]  Missing packets detected")
                    print(f"[SERVER]  Acknowledge Sequence: {last_sequence} ")
                    print(f"[SERVER]     Expected Sequence: {sequence} ")
                    print(f"[SERVER]    SENT - Missing Seq: {missing_packets}")
                else:
                    print(f"[SERVER]  No missing packets detected")

                time.sleep((25 + random.randint(0, 10)) / 1000)  # adding some random delay to packet
                serverSocket.sendto(f"hello:{missing_packets}".encode(), address)
        except timeout:
            pass
    serverSocket.close()
