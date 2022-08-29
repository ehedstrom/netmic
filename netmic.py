#!/usr/bin/python3
# Netmic

from struct import unpack

# Socket will do most of our heavy lifting.
try:
    import socket
except ImportError as error:
    print(error)

#
class EthernetFrame:
    def __init__(self):
        unpacked_data = unpack("!6s6sH", data[0:self.length])
        self.protocol = socket.ntohs(unpacked_data)
        self.destination = data[0:6]
        self.source = data[6:12]
        self.leftover_data = data[self.length]


# Map processes with packets.
class ProcessCapture:
    def __init__(self):
        pass

# Temporary build of class that will store our collected packets.
class PCAPFile:
    def __init__(self, filename):
        self.fp = open(filename, "wb")

    def write(self, data):
        self.fp.write(data)

    def close(self):
        self.fp.close()


#
def main():
    # Create socket connection.
    connection = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

    # Listen until stopped.
    while True:
        raw_data, addr = connection.recvfrom(65535)
        print(raw_data)

    # Main


# Main loop.
if __name__ == "__main__":
    main()
