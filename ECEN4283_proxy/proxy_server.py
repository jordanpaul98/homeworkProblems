
from socket import *
import sys
if False and len(sys.argv) <= 1:
    print('Usage: "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address of the Proxy Server')
    sys.exit(2)

# Create a server socket, bind it to a port and start listening
tcpSerPort = 8000
tcpSerSock = socket(AF_INET, SOCK_STREAM)
# Prepare a server socket
tcpSerSock.bind(('', tcpSerPort))
tcpSerSock.listen(5)

while True:
    # Start receiving data from the client
    print('Ready to serve...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('Received a connection from: ', addr)
    message = tcpCliSock.recv(1024).decode()

    # Extract the filename from the given message
    if "favicon.ico" in message:
        continue
    host_and_path = message.split()[1]
    print(f"host and path: {host_and_path}")

    if host_and_path.count("/") == 1:
        hostn = host_and_path.split("/")[1]
        filename = ""
    else:
        _, hostn, filename = host_and_path.split("/", 2)
        filename = "" + filename

    # filename = message.split()[1].partition("/")[2]
    # print(message.split()[1].partition("/"))
    print("hostn: {}".format(hostn))
    print("filename: {}".format(filename))

    fileExist = "false"
    filetouse = "/" + hostn + filename
    try:
        # Check whether the file exists in the cache
        f = open(filetouse[1:], "rb")
        outputdata = f.read()
        fileExist = "true"

        # ProxyServer finds a cache hit and generates a response message
        tcpCliSock.send("HTTP/1.0 200 OK\r\n".encode())
        tcpCliSock.send("Content-Type:text/html\r\n\r\n".encode())

        # Fill in start
        # send each `inputdata` using `send` method of the socket

        print(outputdata)
        tcpCliSock.send(outputdata)

        print('Read from cache')

        f.close()
        # Fill in end
        # Error handling for file not found in cache

    except IOError:
        print('File Exist: ', fileExist)
        if fileExist == "false":

            # Create a socket on the proxyserver
            c = socket(AF_INET, SOCK_STREAM)

            # hostn = filename.replace("www.", "", 1)
            # print("filename: {}".format(filename))
            # print('Host Name: ', hostn)

            try:
                # Connect to the socket to port 80
                print(hostn)
                c.connect((hostn, 80))

                # Create a temporary file on this socket and ask port 80
                # for the file requested by the client
                fileobj = c.makefile('rwb', 0)
                request = None
                if message.split()[0] == "GET":
                    request = ("GET /{} HTTP/1.0\r\nHost: {}\r\n\r\n".format(filename, hostn))
                else:
                    request = ("POST /{} HTTP/1.0\r\nHost: {}\r\n\r\n".format(filename, hostn))

                print(request)
                fileobj.write(request.encode())

                if "POST" in request:
                    fileobj.write(message.split("\r\n\r\n")[1].encode())

                # Fill in start
                # Read the response into buffer

                buffer = fileobj.read()

                if buffer.split()[1] == b'404':
                    print("404 caught")
                    tcpCliSock.send("HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n".encode() + "404 not found....  Page not cached".encode())

                    tcpCliSock.close()
                    continue

                tcpCliSock.send(buffer)

                # Fill in end

                # Create a new file in the cache for the requested file.
                # Also send the response in the buffer to client socket
                # and the corresponding file in the cache
                tmpFile = open("./" + hostn + filename, "wb")

                buffer = buffer.decode()

                data = buffer.split("\r\n\r\n")[1]

                tmpFile.write(buffer.split("\r\n\r\n")[1].encode())
                tmpFile.close()

                # Fill in start
                # for each item in `buff`, write to `tmpFile` and send using the
                # socket
                # Fill in end
            except Exception as e:
                print('Illegal request')
                print(e)
            else:
                # HTTP response message for file not found
                print('File Not Found')
                # Close the socket and the server sockets
    tcpCliSock.close()
# Fill in start
tcpSerSock.close()
# Fill in end
