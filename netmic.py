#!/usr/bin/python3
# Netmic

# Socket will do most of our heavy lifting.
try:
    import socket
except ImportError as error:
    print(error)

# Socket will do most of our heavy lifting.
try:
    import nettypes
except ImportError as error:
    print(error)

import time
from pcap import PCAPFile

# Import local scripts
import utils
from nettypes import EthernetFrame
from nettypes import IPHeader
from nettypes import TCPsegment
from nettypes import UDPSegment
from nettypes import UDPPayload

# Track unique devices.
contacts = []


# Map processes with packets.
class ProcessCapture:
    def __init__(self):
        pass


#
def main():
    # Start watch.
    stopwatch = time.time()
    next_chirp = stopwatch + 30

    # Create socket connection.
    connection = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

    # Create a new pcap file.
    pcap = PCAPFile('netmic.pcap')

    # Listen until stopped.
    while True:
        # Waits until it receives a connection
        raw_data, addr = connection.recvfrom(65535)

        # Add to current pcap
        pcap.write(raw_data)

        frame = EthernetFrame(raw_data)

        if frame.protocol == 8:
            # Extract the header.
            ipheader = IPHeader(frame.leftover_data)

            # Add unique addresses to contact list for tracking.
            if ipheader.source_addr not in contacts:
                contacts.append(ipheader.source_addr)
                ip_addr = ipheader.source_addr
                dns_name = utils.get_dns(ipheader.source_addr)
                machine = "NEW:" + str(ip_addr) + " " + str(dns_name)
                print(machine)

            if ipheader.protocol == 6:
                tcp = TCPsegment(ipheader.leftover_data)
                # print(tcp)
            elif ipheader.protocol == 17:
                udp = UDPSegment(ipheader.leftover_data)
                # print(udp)
                payload = UDPPayload(udp.leftover_data)

        # Repeat List Every 30 Seconds. Append new.



    pcap.close()
    # Main


# Main loop.
if __name__ == "__main__":
    main()
