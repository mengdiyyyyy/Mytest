import asyncio
import playground
from playground.network.common import StackingProtocol, StackingTransport, StackingProtocolFactory

class PassThrough1(StackingProtocol):
	
	def connection_made(self,transport):
		print('stack1:connection made')
		self.transport=transport
		higherTransport=StackingTransport(self.transport)
		self.higherProtocol().connection_made(higherTransport)
		

	def data_received(self,data):
		print('stack1:Data Transfering...')	
		self.higherProtocol().data_received(data)
	

	def connection_lost(self,exc):
		print('stack1:connection end and is close now')
		self.higherProtocol().connection_lost(exc)
		

class PassThrough2(StackingProtocol):

	def connection_made(self,transport):
		print('stack2:connection made')		
		self.transport=transport
		higherTransport=StackingTransport(self.transport)
		self.higherProtocol().connection_made(higherTransport)

	def data_received(self,data):
		print('stack2:Data Transfering')		
		self.higherProtocol().data_received(data)
		

	def connection_lost(self,exc):
		print('stack2:connection end and close now')		
		self.higherProtocol().connection_lost(exc)
		
