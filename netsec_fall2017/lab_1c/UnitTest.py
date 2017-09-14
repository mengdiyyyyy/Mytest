from playground.asyncio_lib.testing import TestLoopEx
#from playground.network.packet import PacketType
from playground.network.testing import MockTransportToStorageStream
from playground.network.testing import MockTransportToProtocol
from server import ServerProtocol
from client import ClientProtocol
import asyncio
from PacketConnect import RequestStringCompare,StringCompareQuestion,StringCompareAnswer,StringCompareResult

def basicUnitTest():
    # asyncio.set_event_loop(TestLoopEx())
   clientProtocol = ClientProtocol()
   serverProtocol = ServerProtocol()
   cTransport, sTransport = MockTransportToProtocol.CreateTransportPair(clientProtocol, serverProtocol)
   serverProtocol.connection_made(sTransport)
   clientProtocol.connection_made(cTransport)
   

   '''
   packet1 = RequestStringCompare()
   packet1.Question= "What is the compared string?"
   client.transport.write(packet1.__serialize__())
   '''

if __name__ == "__main__":
    # p_logging.EnablePresetLogging(p_logging.PRESET_TEST)
    basicUnitTest()
    print("Basic Unit Test Successful.")


