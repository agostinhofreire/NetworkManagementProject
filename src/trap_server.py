from pysnmp.carrier.asynsock.dispatch import AsynsockDispatcher
from pysnmp.carrier.asynsock.dgram import udp, udp6
from pyasn1.codec.ber import decoder
from pysnmp.proto import api
import threading
import queue


my_queue = queue.Queue()
resp_dict = {}


def cbFun(transportDispatcher, transportDomain, transportAddress, wholeMsg):
    #print('cbFun is called')
    global resp_dict
    while wholeMsg:
        #print('loop...')
        msgVer = int(api.decodeMessageVersion(wholeMsg))
        if msgVer in api.protoModules:
            pMod = api.protoModules[msgVer]
        else:
            #print('Unsupported SNMP version %s' % msgVer)
            return
        reqMsg, wholeMsg = decoder.decode(
            wholeMsg, asn1Spec=pMod.Message(),
            )
        # print('Notification message from %s:%s: ' % (
        #     transportDomain, transportAddress
        #     )
        # )
        reqPDU = pMod.apiMessage.getPDU(reqMsg)
        if reqPDU.isSameTypeWith(pMod.TrapPDU()):
            if msgVer == api.protoVersion1:
                str_enterprise = pMod.apiTrapPDU.getEnterprise(reqPDU).prettyPrint()
                agent_adress  = pMod.apiTrapPDU.getAgentAddr(reqPDU).prettyPrint()
                generic_trap = pMod.apiTrapPDU.getGenericTrap(reqPDU).prettyPrint()
                specifc_trap =pMod.apiTrapPDU.getSpecificTrap(reqPDU).prettyPrint()
                Uptime = pMod.apiTrapPDU.getTimeStamp(reqPDU).prettyPrint()
            varBinds = pMod.apiTrapPDU.getVarBinds(reqPDU)
            message = varBinds[-1]
            nome_traper = varBinds[1]
            message = message[-1].prettyPrint()
            nome_traper = nome_traper[-1].prettyPrint()
            resp_dict = {
                'str_enterprise': str_enterprise,
                'agent_adress': agent_adress,
                'generic_trap': generic_trap,
                'specifc_trap': specifc_trap,
                'uptime': Uptime,
                'message':message,
                'cliente':nome_traper
            }
    return wholeMsg
#def start_service():


def thread_gambs():
    global resp_dict,my_queue
    while True:
        #print('comp ',resp_dict)
        if resp_dict == {}:
            continue

        break
    #print('fim')
    my_queue.put(resp_dict)
    return resp_dict

def th_gambs2():
    global th_gambs,my_queue
    while resp_dict == {}:
        pass
    return True

th_gambs = None


def start_server():
    global th_gambs,resp_dict
    resp_dict = {}
    th_gambs = threading.Thread(target=thread_gambs)
    transportDispatcher = AsynsockDispatcher()

    transportDispatcher.registerRecvCbFun(cbFun)

    # UDP/IPv4
    transportDispatcher.registerTransport(
        udp.domainName, udp.UdpSocketTransport().openServerMode(('192.168.0.108', 162))
    )

    # UDP/IPv6
    transportDispatcher.registerTransport(
        udp6.domainName, udp6.Udp6SocketTransport().openServerMode(('::1', 162))
    )

    transportDispatcher.jobStarted(1)


    th_gambs.start()
    try:
        # Dispatcher will never finish as job#1 never reaches zero
        print('run dispatcher')
        transportDispatcher.runDispatcher()

    except:

        transportDispatcher.closeDispatcher()


