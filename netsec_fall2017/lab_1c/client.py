import asyncio
from playground.network.packet import PacketType
from playground.network.packet.fieldtypes import UINT32, STRING
from PacketConnect import RequestStringCompare,StringCompareQuestion,StringCompareAnswer,StringCompareResult

class ClientProtocol(asyncio.Protocol):
	def __init__(self):
		self.transport = None
		self._Deserializer = PacketType.Deserializer()
		self.receivedpkt=1

	def connection_made(self, transport):
		self.receivedpkt+=1
		self.transport=transport
		self._Deserializer = PacketType.Deserializer()
		print("Client(prepare)-->server(prepare):the Client is Connecting to server...")
		self.askQuestion()
		

	def data_received(self, data):
		self.receivedpkt+=1
		self._Deserializer.update(data)
		for pkt in self._Deserializer.nextPackets():
			if isinstance(pkt,StringCompareQuestion):
				self.strcompareAnswer(pkt)

	def connection_lost(self, exc):
		print('WARNING!!! Clinet status Lost:The server closed the connection,stop the loop')
		self.transport=None
		#self.transport.stop()

	def askQuestion(self):
		packet1=RequestStringCompare()
		packet1.Question="What is the two compared strings?"
		print('Client(asking)-->(server(giving question)):Asking Question of compared string,sent.')
		self.transport.write(packet1.__serialize__())	
		
	def strcompareAnswer(self,pkt):
		print('Client(result)-->server(judge) :The question is received and answering now...')
		packet3=StringCompareAnswer()
		packet3.id=100
		packet3.Answer="STR1"
		print('Client(result)-->server(judge):sent the Answer.The Answer is 1.')
		self.transport.write(packet3.__serialize__())
		print('Client(Received pkt):The total received packet is {}.'.format(self.receivedpkt))
		print('Client(FINAL):Communication is END now.')



'''
loop = asyncio.get_event_loop()
coro = loop.create_connection(lambda: ClientProtocol(),'127.0.0.1', 9997)
loop.run_until_complete(coro)
loop.run_forever()
loop.close()
'''
