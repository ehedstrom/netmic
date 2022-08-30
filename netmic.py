#!/usr/bin/python3
# Netmic


from nettypes import EthernetFrame
from nettypes import IPHeader
from nettypes import TCPsegment
from nettypes import UDPSegment


from pcap import PCAPFile


# Socket will do most of our heavy lifting.
try:
    import socket
except ImportError as error:
    print(error)


# Map processes with packets.
class ProcessCapture:
    def __init__(self):
        pass

#
def main():
    # Create socket connection.
    connection = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

    pcap = PCAPFile('packets.pcap')

    # Listen until stopped.
    while True:
        raw_data, addr = connection.recvfrom(65535)
        pcap.write(raw_data)
        frame = EthernetFrame(raw_data)
        # print(frame)
        if frame.protocol == 8:
            ipheader = IPHeader(frame.leftover_data)
            print(ipheader)
            if ipheader.protocol == 6:
                tcp = TCPsegment(ipheader.leftover_data)
                print(tcp)
            elif ipheader.protocol == 17:
                udp = UDPSegment(ipheader.leftover_data)
                print(udp)

    pcap.close()
    # Main


# Main loop.
if __name__ == "__main__":
    main()
