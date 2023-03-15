generating_code ={
    'CRC-32-IEEE_normal' : 0x04C11DB7,
    'CRC-32-IEEE_reversed': 0xEDB88320,
    'CRC-32-IEEE_reversedFromNormal' : 0x82608EDB
    'CRC-32C_normal' : 0x1EDC6F41,
    'CRC-32C_reversed' : 0x82F63B78,
    'CRC-32C_reversedFromNormal' : 0x8F6E37A0,
    'CRC-32K_normal' : 0x741B8CD7,
    'CRC-32K_reversed' : 0xEB31D82E,
    'CRC-32K_reversedFromNormal' : 0xBA0DC66B,
    'CRC-32Q_normal': 0x814141AB,
    'CRC-32Q_reversed': 0xD5828281,
    'CRC-32Q_reversedFromNormal': 0xC0A0A0D5
}



def crc_hash(object, method=generating_code['CRC-32-IEEE_normal']):
    pass

def getpolynom(object):
    res = [0 for i in range(len(object))]
    for k,i in enumerate(object):
        res[k] = 
