import hashlib
import math
from one_time_pad import strong_encrypt

# packetize a string
# packet format: header length, check-sum and payload size
def packetize(payload, encrypt=False):
	if not payload: return ''
	if encrypt: payload = strong_encrypt(payload)
	packet_length = len(payload)
	packet_length_length = int(1 + math.log10(packet_length))
	header_length = 13 + packet_length_length
	md5_hash = checksum(payload)[:8]
	packet = '|'.join([str(header_length), md5_hash, str(packet_length), payload])
	return packet


# encode a string and find its md5 checksum 
def checksum(payload):
	return hashlib.md5(payload.encode()).hexdigest()