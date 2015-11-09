from sulley import *
from hyper.packages.hpack.hpack import Encoder, Decoder
import json

def json_hpack_encoder(json_headers):
    e = Encoder()
    headers = json.loads(json_headers)
    header_pairs = []
    for name, value in headers.iteritems():
        header_pairs.append((name.lower(), value))
    s = e.encode(header_pairs)
    return s


########################################################################################################################
# Magic frame(Preamble packet) in HTTP/2 protocol
########################################################################################################################
s_initialize("HTTP/2 Magic")
s_static(b"PRI * HTTP/2.0\r\n\r\nSM\r\n\r\n")

########################################################################################################################
# Settings packet for disable push  in HTTP/2 protocol
########################################################################################################################
s_initialize("HTTP/2 Settings disable push")
s_bit_field(6, 24, endian=">", fuzzable=False) # length(bytes number) of payload in frame
s_bit_field(4, 8, fuzzable=False)  # type of frame
s_bit_field(0, 8, fuzzable=False)  # flags of frame
s_bit_field(0, 32, endian=">", fuzzable=False) # stream ID
# payload
s_bit_field(2, 16, endian=">", fuzzable=False) # settings enable_push
s_bit_field(0, 32, endian=">", fuzzable=False) # disable

########################################################################################################################
# Settings packet for ACK in HTTP/2 protocol
########################################################################################################################
s_initialize("HTTP/2 Settings ACK")
s_bit_field(0, 24, endian=">", fuzzable=False) # length(bytes number) of payload in frame
s_bit_field(4, 8, fuzzable=False)  # type of frame
s_bit_field(1, 8, fuzzable=False)  # flags of frame
s_bit_field(0, 32, fuzzable=False) # stream ID

########################################################################################################################
# Headers packet in HTTP/2 protocol
########################################################################################################################
def set_header_frame(headers):
    s_initialize("HTTP/2 Headers")
    s_size("headers payload", endian=">", length=3, format="binary", fuzzable=False) # length(bytes number) of payload in frame
    s_bit_field(1, 8, fuzzable=False)  # type of frame
    s_bit_field(4, 8, fuzzable=False)  # flags of frame, End Headers
    s_bit_field(1, 32, endian=">", fuzzable=False, name="header stream id") # stream ID
    # payload (Header block fragment)
    if s_block_start("headers payload", encoder=json_hpack_encoder):
        # make it in json form
        s_static("{")

        count = 0
        for name, value in headers.iteritems():
            # name
            s_static("\"" + name + "\": ")

            # value
            s_static("\"")
            if isinstance(value, list):
                s_group(name+"_group", values=value)
                if s_block_start(name+"_block", group=name+"_group"):
                    s_static("")
                s_block_end()
            else:
               s_static(value)
            
            s_static("\"")

            if count + 1 != len(headers):
                s_static(", ")
            count = count + 1
            
        s_static("}")

        """
        e = Encoder()
        header_pairs = []
        for name, value in headers.iteritems():
            header_pairs.append((name.lower(), value))
        s_string(e.encode(header_pairs), encoding="binary", fuzzable=False)
        """

        """
        for key, value in headers:
            s_bit_field(1+len(key), 32, fuzzable=False)
            s_string(":"+key, encoding="binary", fuzzable=False, max_length=0)
            s_bit_field(len(value), 32, fuzzable=True)
            s_string(value, encoding="binary", fuzzable=False, max_length=0)
        """
    s_block_end()

########################################################################################################################
# Datas packet in HTTP/2 protocol
########################################################################################################################
s_initialize("HTTP/2 Datas")
s_size("datas payload", endian=">", length=3, format="binary", fuzzable=False) # length(bytes number) of payload in frame
s_bit_field(0, 8, fuzzable=False)  # type of frame
s_bit_field(1, 8, fuzzable=False)  # flags of frame, End Stream
s_bit_field(1, 32, endian=">", fuzzable=False, name="data stream id") # stream ID
# payload (Header block fragment)
if s_block_start("datas payload"):
    s_string("", encoding="binary", max_len=100, fuzzable=True)
s_block_end()

