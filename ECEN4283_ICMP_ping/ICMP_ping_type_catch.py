import os
import sys
import struct
import time
import select
import socket
import binascii

ICMP_ECHO_REQUEST = 8

rtt_min, rtt_max, rtt_avg, rtt_cnt = float('inf'), 0, 0, 0
pings_sent, pings_lost = 0, 0


def checksum(str):
    csum = 0
    countTo = (len(str) / 2) * 2

    count = 0
    while count < countTo:
        thisVal = str[count + 1] * 256 + str[count]
        csum = csum + thisVal
        csum = csum & 0xffffffff
        count = count + 2

    if countTo < len(str):
        csum = csum + str[len(str) - 1]
        csum = csum & 0xffffffff

    csum = (csum >> 16) + (csum & 0xffff)
    csum = csum + (csum >> 16)
    answer = ~csum
    answer = answer & 0xffff
    answer = answer >> 8 | (answer << 8 & 0xff00)
    return answer


def receiveOnePing(mySocket, ID, timeout, destAddr):
    global rtt_min, rtt_max, rtt_avg, rtt_cnt, pings_lost
    timeLeft = timeout
    while 1:
        startedSelect = time.time()
        whatReady = select.select([mySocket], [], [], timeLeft)
        howLongInSelect = (time.time() - startedSelect)
        if whatReady[0] == []:  # Timeout
            pings_lost += 1
            return "Request timed out."
        else:
            timeReceived = time.time()
            recPacket, addr = mySocket.recvfrom(1024)

            # Fill in start
            # Fetch the ICMP header from the IP packet

            icmp_header = recPacket[20:28]
            ip_header = recPacket[:20]
            message_body = recPacket[28:]

            ttl_time = struct.unpack("B", ip_header[8:9])[0]
            type, code, checksum, id, sequence = struct.unpack("BBHHH", icmp_header)
            data = float(struct.unpack("d", message_body)[0])

            match type:
                case 0:  # nothing to do here
                    pass
                case 3:
                    return "Destination Unreachable"
                case 4:
                    return "Source Quench (Deprecated)"
                case 5:
                    return "Redirect"
                case 6:
                    return "Alternate Host Address"
                case 8:
                    return "Echo"
                case 11:
                    return "Time Exceeded"
                case _:
                    return f"Type code: {type}"

            print("ICMP Type:", type)
            print("ICMP Code:", code)
            print("ICMP Checksum:", checksum)
            print("ICMP ID:", id)
            print("ICMP Sequence:", sequence)
            print("IP TTL", ttl_time)
            print("ICMP Data: ", data)
            print("")

            rtt = (timeReceived - data) * 1000

            rtt_min = min(rtt, rtt_min)
            rtt_max = max(rtt, rtt_max)
            rtt_avg = (rtt_avg * rtt_cnt + rtt) / (rtt_cnt + 1)
            rtt_cnt += 1

            print(f"RTT: {rtt:.1f}ms   Packet Lost: {100 * pings_lost / pings_sent:.2f}%   Pings Sent: {pings_sent}"
                  f"\nRTT Min: {rtt_min:.1f}ms\nRTT Max: {rtt_max:.1f}ms\nRTT Avg: {rtt_avg:.1f}ms\n")

            return rtt

            # Fill in end

        timeLeft = timeLeft - howLongInSelect
        if timeLeft <= 0:
            pings_lost += 1
            return "Request timed out."


def sendOnePing(mySocket, destAddr, ID):
    # Header is type (8), code (8), checksum (16), id (16), sequence (16)
    global pings_sent

    myChecksum = 0
    # Make a dummy header with a 0 checksum.
    # struct -- Interpret strings as packed binary data
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)
    data = struct.pack("d", time.time())
    # Calculate the checksum on the data and the dummy header.
    myChecksum = checksum(header + data)

    # Get the right checksum, and put in the header
    if sys.platform == 'darwin':
        myChecksum = socket.htons(myChecksum) & 0xffff
        # Convert 16-bit integers from host to network byte order.
    else:
        myChecksum = socket.htons(myChecksum)

    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)

    packet = header + data

    pings_sent += 1
    mySocket.sendto(packet, (destAddr, 1))  # AF_INET address must be tuple, not str
    # Both LISTS and TUPLES consist of a number of objects
    # which can be referenced by their position number within the object


def doOnePing(destAddr, timeout):
    icmp = socket.getprotobyname("icmp")
    # SOCK_RAW is a powerful socket type. For more details see: http://sock-raw.org/papers/sock_raw

    mySocket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)

    myID = os.getpid() & 0xFFFF  # Return the current process i
    sendOnePing(mySocket, destAddr, myID)
    delay = receiveOnePing(mySocket, myID, timeout, destAddr)

    mySocket.close()
    return delay


def ping(host, timeout=1):
    # timeout=1 means: If one second goes by without a reply from the server,
    # the client assumes that either the client's ping or the server's pong is lost
    dest = socket.gethostbyname(host)
    print("Pinging " + dest + " using Python:")
    print("")
    # Send ping requests to a server separated by approximately one second
    while 1:
        delay = doOnePing(dest, timeout)

        if delay == "Destination Unreachable":
            print("Destination Unreachable: exiting")

        print(f"Delay: {delay}\n")
        time.sleep(1)  # one second

    return delay

# ping("google.com")
ping("yahoo.co.jp")
# ping("alibaba.com")
# ping("domain.com.au")
