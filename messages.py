RESERVED=0x00
CONNECT = 0x01
CONNACK = 0x02
PUBLISH = 0x03
PUBACK = 0x04
PUBREC = 0x05
PUBREL = 0x06
PUBCOMP = 0x07
SUBSCRIBE = 0x08
SUBACK = 0x09
UNSUBSCRIBE = 0x0A
UNSUBACK = 0x0B
PINGREQ = 0x0C
PINGRESP = 0x0D
DISCONNECT = 0x0E
AUTH = 0x0F

class PacketTypes:

    indexes = range(0, 15)
    RESERVED, CONNECT, CONNACK, PUBLISH, PUBACK, PUBREC, PUBREL, PUBCOMP, SUBSCRIBE, SUBACK, UNSUBSCRIBE, UNSUBACK, PINGREQ, PINGRESP, DISCONNECT, AUTH = indexes
    Names = ["reserved", "Connect", "Connack", "Publish", "Puback", "Pubrec", "Pubrel", "Pubcomp", "Subscribe", "Suback", "Unsubscribe", "Unsuback", "Pingreq", "Pingresp", "Disconnect", "Auth"]