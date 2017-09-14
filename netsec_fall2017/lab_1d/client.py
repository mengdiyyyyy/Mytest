import asyncio
import playground
from playground.network.packet import PacketType
from PacketConnect import RequestStringCompare,StringCompareQuestion,StringCompareAnswer,StringCompareResult
import time

class ClientProtocol(asyncio.Protocol):
	def __init__(self):
		self.transport = None
		self._Deserializer = PacketType.Deserializer()	
		#self.transport.write(self.askQuestion())
		#for x in range(0,3):
		#signal.alarm(2)
		#time.sleep(1)

	
	def connection_made(self, transport):
		self.transport=transport
		self._Deserializer = PacketType.Deserializer()
		print("Client(prepare)-->server(preparse):the Client is Connecting to server...")
		self.transport.write(self.askQuestion())
		time.sleep(10)
		self.transport.write(self.askQuestion())
	
		
	def data_received(self, data):
		self._Deserializer.update(data)
		for pkt in self._Deserializer.nextPackets():
			if isinstance(pkt,StringCompareQuestion):
				self.strcompareAnswer(pkt)

	def connection_lost(self, exc):
		print('WARNING!!! Clinet status Lost:The server closed the connection,stop the loop')
		self.transport=None
		self.loop.stop()

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
		print('Client(FINAL):Communication is END now.')


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    coro = playground.getConnector().create_playground_connection(lambda: ClientProtocol(), '20174.1.1.1',888)
    loop.run_until_complete(coro)
    loop.run_forever()
    loop.close()
