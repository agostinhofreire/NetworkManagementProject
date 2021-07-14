from pysnmp import debug
from pysnmp.entity.rfc3413.oneliner import cmdgen

class OidFinder:
    def __init__(self):

        self.cmdGen = cmdgen.CommandGenerator()

    def __output_formatter(self, oid_list):
        new_output = []

        if oid_list:

            for idx, name in enumerate(oid_list):
                line = f"OID Address {idx:04d} < {name} >"
                
                new_output.append((line, name))

            return new_output
        
        else:
            new_output = [("No OID found", "")]

        return new_output



    def getList(self, ip="127.0.0.1"):
        
        oid_list = []

        try:
            _, _, _, varBind = self.cmdGen.nextCmd(
                        cmdgen.CommunityData('public'),
                        cmdgen.UdpTransportTarget((ip, 161)),
                        '1.3.6',
                        lexicographicMode=True,
                        ignoreNonIncreasingOid=True
                    )
        except:
            varBind = []
            varBindTableRow = []

        for varBindTableRow in varBind:
            for name, _ in varBindTableRow:
                oid_list.append(str(name))

        return self.__output_formatter(oid_list)


# print(len(varBind)) #prints number of oids
# print(OidFinder().getList())