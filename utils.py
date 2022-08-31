# TODO Wrap this in a try.
import dns.resolver


class Server:
    def __init__(self, ip, mac):
        self.ip = ip
        self.mac = mac
        self.name = ""

    def __str__(self):
        return f"{self.name} - {self.ip}"


class Contact:
    def __init__(self, ip):
        self.ip = ip


def get_dns(ip):
    # Create a new resolver using Google's public DNS.

    resolver = dns.resolver.Resolver()

    # This is a single point of failure.
    resolver.nameservers = ["8.8.4.4"]

    # Try to resolve, but fail quietly.
    try:
        # sorted({resolver.resolve(ip)[0].address for i in range(4)})
        name = resolver.resolve(ip)
        return name
    except TypeError:
        return "Type Error"


