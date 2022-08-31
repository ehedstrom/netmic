from struct import pack
import time


# Builds and manages libpcap file.
# wiki.wireshark.org/Development/LibcapFileFormat
class PCAPFile:
    def __init__(self, filename):
        # Requires WB flag.
        self.fp = open(filename, "wb")

        # Create PCAP header
        # magic number, major version, minor version, GMT to Local,
        # accuracy, max length of packets in octects, data link type
        header = pack('!IHHiIII', 0xa1b2c3d4, 2, 4, 0, 0, 65535, 1)

        # Write the header.
        self.fp.write(header)

    def write(self, data):
        seconds, mseconds = [int(part) for part in str(time.time()).split(".")]
        length = len(data)
        message = pack("!IIII", seconds, mseconds, length, length)
        self.fp.write(message)
        self.fp.write(data)

    def close(self):
        self.fp.close()

