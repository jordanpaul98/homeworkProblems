"""
Jordan Paul: ECEN 4283 project UDP pinger
Main.py to start both client and server utilizing threading to initialize the server to wait for packets
and to start client to send packets to the server

ipAddress set to your machine IPv4 address

will need server.py and client.py from repository
records RTT, average RTT, min RTT and max RTT

heartbeat implementation:

server_heartbeat.py and client_heartbeat.py will implement a heartbeat to let the server know that the client is
still connected. Also the client will sent the server a seq which represents the number of packets sent,
the server will compare that to it acknowledge sequence number and will report and return to client a list of
leading up sequence numbers missing
"""
if __name__ == '__main__':
    from threading import Thread
    from time import sleep
    import server
    import client

    #  Your machines IPv4 address
    ipAddress = ''

    # Start a thread to run the server side of UDP pinger
    server_thread = Thread(target=server.Server, daemon=True, args=(ipAddress,))
    server_thread.start()

    sleep(1)  # add delay between server and client setup

    # Start a thread to run the client side of UDP pinger
    client_thread = Thread(target=client.Client, daemon=True, args=(ipAddress,))
    client_thread.start()
    client_thread.join()  # wait for client to finish

    # dont include this if not using server_heartbeat.py and client_heartbeat.py as server wont exit upon client stopping
    server_thread.join()

    # server thread will terminate upon clients_thread finishing
