import socket, glob, json

port = 53
ip = '127.0.0.1'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((ip, port))


def load_zones():
    json_zone = {}
    zonefiles = glob.glob('zones/*.zone')

    for zone in zonefiles:
        with open(zone) as zonedata:
            data = json.load(zonedata)
            zone_name = data["$origin"]
            json_zone[zone_name] = data
    return json_zone

zonedata = load_zones()


def getflags(flags):
    byte_first = bytes(flags[:1])
    QR = '1'
    OPCODE = ''
    for bit in range(1,5):
        OPCODE += str(ord(byte_first)&(1<<bit))

    AA = '1'
    TC = '0'
    RD = '0'
    RA = '0'
    Z = '000'
    RCODE = '0000'

    return int(QR+OPCODE+AA+TC+RD, 2).to_bytes(1, byteorder='big')+int(RA+Z+RCODE, 2).to_bytes(1, byteorder='big')

def getquestiondomain(data):

    state = 0
    expected_length = 0
    domain_string = ''
    domain_parts = []
    x = 0
    y = 0
    for byte in data:
        if state == 1:
            if byte != 0:
                domain_string += chr(byte)
            x += 1
            if x == expected_length:
                domain_parts.append(domain_string)
                domain_string = ''
                state = 0
                x = 0
            if byte == 0:
                domain_parts.append(domain_string)
                break
        else:
            state = 1
            expected_length = byte
        y += 1

    questiontype = data[y:y+2]

    return domain_parts, questiontype

def getzone(domain):
    global zonedata

    zone_name = '.'.join(domain)
    if zone_name in zonedata:

        return zonedata[zone_name]
    else:
        return {'$origin': 'DNE', 'a': [{'name': '@', 'ttl': 400, 'value': '127.0.0.1'}]}

def get_recs(data):
    domain, questiontype = getquestiondomain(data)
    qt = 'a'
    # if questiontype == b'\x00\x01':
    #     qt = 'a'

    zone = getzone(domain)

    return (zone[qt], qt, domain)

def buildquestion(domainname, rectype):
    qbytes = b''

    for part in domainname:
        length = len(part)
        qbytes += bytes([length])

        for char in part:
            qbytes += ord(char).to_bytes(1, byteorder='big')

    if rectype == 'a':
        qbytes += (1).to_bytes(2, byteorder='big')

    qbytes += (1).to_bytes(2, byteorder='big')

    return qbytes

def rectobytes(domainname, rectype, recttl, recval):

    rbytes = b'\xc0\x0c'

    if rectype == 'a':
        rbytes = rbytes + bytes([0]) + bytes([1])

    rbytes = rbytes + bytes([0]) + bytes([1])

    rbytes += int(recttl).to_bytes(4, byteorder='big')

    if rectype == 'a':
        rbytes = rbytes + bytes([0]) + bytes([4])

        for part in recval.split('.'):
            rbytes += bytes([int(part)])
    return rbytes

def buildresponse(data):

    transaction_ID = data[:2]

    Flags = getflags(data[2:4])

    QDCOUNT = b'\x00\x01'

    ANCOUNT = len(get_recs(data[12:])[0]).to_bytes(2, byteorder='big')

    NSCOUNT = (0).to_bytes(2, byteorder='big')

    ARCOUNT = (0).to_bytes(2, byteorder='big')

    dns_header = transaction_ID+Flags+QDCOUNT+ANCOUNT+NSCOUNT+ARCOUNT

    dns_body = b''

    records, rectype, domainname = get_recs(data[12:])

    dns_question = buildquestion(domainname, rectype)

    for record in records:
        # print(record)
        dns_body += rectobytes(domainname, rectype, record["ttl"], record["value"])
    if domainname[0] == 'blacksite' and domainname[1] == 'secrete':
        print(dns_header)
        print(dns_question)
        print(dns_body)
        return dns_header + dns_question + dns_body

print("DNS Started")
while True:
    data, address = sock.recvfrom(512)
    r = buildresponse(data)
    sock.sendto(r, address)
