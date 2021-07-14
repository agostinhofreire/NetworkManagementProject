import socket

class SNMP:


    def send_request(self, OID, ip="127.0.0.1", port=161):
        try:
            snmp_msg = self.__mountHeader(OID)

            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.settimeout(5)

            s.sendto(snmp_msg, (ip, port))

        except:
            return "Error while getting the OID value"

        # AGUARDANDO SNMP GETREQUEST REPLY
        while True:
            try:
                Rxbuf = s.recv(2000)
                Rxbuf = list(Rxbuf)
                valor = ""
          
                for a in Rxbuf:
                    if 65 <= a <= 90 or 97 <= a <= 122 or 48 <= a <= 57 or a in [32, 58,]:
                        valor = valor + chr(a)
                break
            except socket.timeout:
                valor = "Error while getting the OID value"
                break
            
        s.close()

        return valor


    def __mountHeader(self, OID):

        # MONTANDO VARBIND
        TypeVal= b'\x05'
        lenVal_b = b'\x00'#
        SVal = TypeVal + lenVal_b
        lenSVal_i = 2

        b = OID.split(".")
        b = b[2:]
        oid = chr(0x2b)

        for i in range(len(b)):
            oid = oid + chr(int(b[i]))

        oid = oid.encode()

        lenOID_b = chr(len(oid)).encode()
        lenOID_i = len(oid)
        TypeOid = b'\x06'
        SOid = TypeOid + lenOID_b + oid
        lenSOid_i = 2 + lenOID_i

        TypeVarbind = b'\x30'
        lenVar_i = lenSOid_i + lenSVal_i
        lenVar_b = lenVar_i.to_bytes(1,'little')
        SVarbind = TypeVarbind + lenVar_b + SOid + SVal

        # MONTANDO VARBINDLIST
        TypeVarbindList = b'\x30'
        lenVarList_i = 2 + lenVar_i
        lenVarList_b = lenVarList_i.to_bytes(1,'little')
        SVarbindList = TypeVarbindList + lenVarList_b+ SVarbind

        # MONTANDO REQUEST ID
        lenRqID_i = 3
        SRqID = b'\x02' + b'\x01' + b'\x01'

        # MONTANDO ERROR
        lenErr_i = 3
        SErr = b'\x02' + b'\x01' + b'\x00'

        # MONTANDO ERROR INDEX
        lenErrIndex_i = 3
        SErrIndex = b'\x02' + b'\x01' + b'\x00'

        # MONTANDO SNMP PDU
        TypeSPDU = b'\xa0'
        lenPDU_i = lenRqID_i + lenErr_i + lenErrIndex_i + (2 + lenVarList_i)
        lenPDU_b = lenPDU_i.to_bytes(1,'little')
        SPDU = TypeSPDU + lenPDU_b + SRqID + SErr + SErrIndex + SVarbindList

        # MONTANDO COMMUNITY STRING
        TypeComm = b'\x04'
        Comm = b'public'
        CommChr = Comm.decode()
        lenComm_b = chr(len(CommChr)).encode()
        lenComm_i = len(Comm)
        SComm = TypeComm + lenComm_b + Comm

        # MONTANDO VERSION
        TypeVersao = b'\x02'
        lenVersao_b = b'\x01'
        lenVersao_i = 3
        Versao = b'\x00'
        SVersao = TypeVersao + lenVersao_b + Versao

        # MONTANDO SNMP MESSAGE (GETREQUEST)
        MsgType = b'\x30'
        lenSSnmpMsg_i = lenVersao_i + (2 + lenComm_i)+ (2 + lenPDU_i)
        lenSSnmpMsg_b = lenSSnmpMsg_i.to_bytes(1,'little')
        SSnmpMsg =  MsgType + lenSSnmpMsg_b + SVersao + SComm + SPDU

        return SSnmpMsg

# snmp = SNMP()
# print(snmp.send_request("1.3.6.1.2.1.1.6.0"))
