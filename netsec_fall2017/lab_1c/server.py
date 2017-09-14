import asyncio
from playground.network.packet import PacketType
from playground.network.packet.fieldtypes import UINT32, STRING
from PacketConnect import RequestStringCompare,StringCompareQuestion,StringCompareAnswer,StringCompareResult

class ServerProtocol(asyncio.Protocol):
	def __init__(self):
		self.received=0
		self.transport=None
		self._Deserializer = PacketType.Deserializer()

	def connection_made(self,transport):
		self.transport=transport
		self._Deserializer=PacketType.Deserializer()
		peername = transport.get_extra_info('peername')
		print('server(prepare)-->client(prepare):Connection from {}'.format(peername))

	def data_received(self, data):
		self.received+=1
		self._Deserializer=PacketType.Deserializer()
		self._Deserializer.update(data)
		for pkt in self._Deserializer.nextPackets():
			self.stringclass(pkt)

	def stringclass(self,pkt):
		if isinstance(pkt,RequestStringCompare):
			self.received+=1
			packet2=StringCompareQuestion()
			print("Server(giving question)-->client(result): Question of asking compared string received.")
			packet2.id=100
			packet2.STR1="YANG"
			packet2.STR2="LI"
			print("Server(giving question)-->client(result): Question of compared string sent.")
			self.transport.write(packet2.__serialize__())
		if isinstance(pkt,StringCompareAnswer):
			self.received+=1
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
			print('packetReceived')
			print('SERVER(Received pkt):The total received packet is {}.'.format(self.received))
			print('Server(FINAL) :Close the client socket.')
			

'''
loop = asyncio.get_event_loop()
# Each client connection will create a new protocol instance
coro = loop.create_server(ServerProtocol, '127.0.0.1', 9997)
server = loop.run_until_complete(coro)

# Serve requests until Ctrl+C is pressed
print('Serving on {}'.format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass


# Close the server
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()

'''