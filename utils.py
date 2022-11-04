try:
    import dns.resolver
except ImportError as error:
    print(error)



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
    resolver.nameservers = ["8.8.8.8"]

    # Try to resolve, but fail quietly.
    try:
        name = resolver.resolve(ip)
        return name
    except TypeError:
        return "Type Error"
    except dns.exception.DNSException as e:
        return e


