"""
Jordan Paul: ECEN 4283 project UDP pinger
Main.py to start both client and server utilizing threading to initialize the server to wait for packets
and to start client to send packets to the server

ipAdress set to your machine IPv4 address

will need server.py and client.py from repository
"""
if __name__ == '__main__':
    from threading import Thread
    from time import sleep
    import server
    import client

    #  Your machines IPv4 address
    ipAddress = '172.16.218.19'

    # Start a thread to run the server side of UDP pinger
    server_thread = Thread(target=server.Server, daemon=True, args=(ipAddress,))
    server_thread.start()

    sleep(1)  # add delay between server and client setup

    # Start a thread to run the client side of UDP pinger
    client_thread = Thread(target=client.Client, daemon=True, args=(ipAddress,))
    client_thread.start()
    client_thread.join()  # wait for client to finish
    server_thread.join()

    # server thread will terminate upon clients_thread finishing
