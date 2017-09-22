import asyncio
import playground
from playground.network.packet import PacketType
from PacketConnect import RequestStringCompare,StringCompareQuestion,StringCompareAnswer,StringCompareResult
from playground.network.common import StackingProtocol,StackingTransport,StackingProtocolFactory
from passthrough import PassThrough1,PassThrough2

class ServerProtocol(asyncio.Protocol):
	def __init__(self):
		self.transport=None
		self._Deserializer = PacketType.Deserializer()

	def connection_made(self,transport):
		self.transport=transport
		self._Deserializer=PacketType.Deserializer()
		peername = transport.get_extra_info('peername')
		print('server(prepare)-->client(prepare):Connection from {}'.format(peername))

	def data_received(self, data):
		self._Deserializer=PacketType.Deserializer()
		self._Deserializer.update(data)
		for pkt in self._Deserializer.nextPackets():
			self.stringclass(pkt)

	def stringclass(self,pkt):
		if isinstance(pkt,RequestStringCompare):
			packet2=StringCompareQuestion()
			#print("Server(giving question)-->client(result): Question of asking compared string received.")
			packet2.id=100
			packet2.STR1="YANG"
			packet2.STR2="LI"
			print("Server(giving question)-->client(result): Question of compared string sent.")
			self.transport.write(packet2.__serialize__())
		if isinstance(pkt,StringCompareAnswer):
			packet4=StringCompareResult()
			print('Server(judge)-->client(final): Answer received and is working on the result...')
			packet4.id=100
			print(pkt.Answer)
			if pkt.Answer=="STR1":
				packet4.output="TRUE"
				print('Server(judge)-->client(FINAL) : The output is {}.'.format(packet4.output))
			if pkt.Answer=="STR2":
				packet4.output="FALSE"
				print('Server(judge)-->client(FINAL) : The output is {}.'.format(packet4.output))
			self.transport.write(packet4.__serialize__())
			self.transport.close()
			print('Server(FINAL) :Close the client socket.')
			

if __name__ == "__main__":
    f = StackingProtocolFactory(lambda: PassThrough1(), lambda: PassThrough2())
    ptConnector = playground.Connector(protocolStack=f)
    playground.setConnector("passthrough", ptConnector)

    loop = asyncio.get_event_loop()
    coro = playground.getConnector('passthrough').create_playground_server(ServerProtocol, 777)
    server = loop.run_until_complete(coro)
    loop.run_forever()
    loop.close()

