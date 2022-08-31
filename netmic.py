#!/usr/bin/python3
# Netmic


from nettypes import EthernetFrame
from nettypes import IPHeader
from nettypes import TCPsegment
from nettypes import UDPSegment
from nettypes import UDPPayload
import time
import utils

import datetime

from pcap import PCAPFile

# Track unique devices.
contacts = []



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
    # Start watch.
    stopwatch = time.time()
    next_chirp = stopwatch + 30

    # Create socket connection.
    connection = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

    # Create a new pcap file.
    pcap = PCAPFile('netmic.pcap')

    # Listen until stopped.
    while True:
        raw_data, addr = connection.recvfrom(65535)

        pcap.write(raw_data)

        frame = EthernetFrame(raw_data)

        # print(frame)
        if frame.protocol == 8:
            ipheader = IPHeader(frame.leftover_data)
            # print(ipheader)
            if ipheader.source_addr not in contacts:
                contacts.append(ipheader.source_addr)
                ip_addr = ipheader.source_addr
                dns_name = utils.get_dns(ipheader.source_addr)
                machine = str(ip_addr) + " " + str(dns_name)
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
