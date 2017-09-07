from playground.network.packet import PacketType
from playground.network.packet.fieldtypes import INT32,UINT32,STRING,BUFFER,BOOL

#packet1 
class RequestStringCompare(PacketType):
	DEFINITION_IDENTIFIER="lab1b.student_mengdi.RequestStringCompare"
	DEFINITION_VERSION="1.0"
	FIELDS=[]

#packet2
class StringCompareQuestion(PacketType):
	DEFINITION_IDENTIFIER="lab1b.student_mengdi.StringCompareQuestion"
	DEFINITION_VERSION="1.0"

	FIELDS=[
		("id",INT32),
		("STR1",STRING),
		("STR2",STRING)
		]

#packet3
class StringCompareAnswer(PacketType):
	DEFINITION_IDENTIFIER="lab1b.student_mengdi.StringCompareAnswer"
	DEFINITION_VERSION="1.0"

	FIELDS=[
		("id",INT32)
		]

#packet4
class StringCompareResult(PacketType):
	DEFINITION_IDENTIFIER="lab1b.student_mengdi.StringCompareResult"
	DEFINITION_VERSION="1.0"

	FIELDS=[
		("id",INT32),
		("output",STRING),
		("checker",BOOL)
		]

def basicUnitTest():
	#using deserialize to verify packet1
	packet1=RequestStringCompare()
	packet1Bytes=packet1.__serialize__()
	packet1A=RequestStringCompare.Deserialize(packet1Bytes)
	assert packet1==packet1A

	#using deserialize to verify packet2
	packet2 = StringCompareQuestion()
	packet2.STR1="the color is yellow"
	packet2.STR2="this is banana"
	packet2.id=100
	packet2Bytes=packet2.__serialize__()
	packet2B=StringCompareQuestion().Deserialize(packet2Bytes)
	assert packet2==packet2B

	#using deserialize to verify packet3
	packet3=StringCompareAnswer()
	packet3.id=100
	packet3Bytes=packet3.__serialize__()
	packet3B=StringCompareAnswer().Deserialize(packet3Bytes)
	assert packet3==packet3B

	#using deserialize to verify packet4
	packet4=StringCompareResult()
	packet4.id=100
	#experimenting with the BOOL,if the packet4.checker=True or False, the output of program will report the name of the input is not defined
	packet4.checker=True
	packet4.checker=False
	#Verifying deserialize using list 
	packet4.list=['physics','chemistry',2000]
	packet4.output="right"
	packet4Bytes=packet4.__serialize__()
	packet4B=StringCompareResult().Deserialize(packet4Bytes)
	assert packet4==packet4B

	print('ALL result is right')
	
	#Using deserializer to assert 
	deserializer=PacketType.Deserializer()
	pktBytes = packet1.__serialize__() + packet2.__serialize__() + packet3.__serialize__()+packet4.__serialize__()	
	print('Starting with {} bytes of data'.format(len(pktBytes)))
	while len(pktBytes) > 0:
		# let’s take of a 10 byte chunk
		chunk, pktBytes = pktBytes[:10], pktBytes[10:]
		deserializer.update(chunk)
		print('Another 10 bytes loaded into deserializer. Left={}'.format(len(pktBytes)))
		for packet in deserializer.nextPackets():
			print('got a packet!')
			if packet == packet1: print('It’s packet 1!')
			elif packet == packet2: print('It’s packet 2!')
			elif packet == packet3: print('It’s packet 3!')
			elif packet == packet4: print('It’s packet 4!')


	
	

if __name__=="__main__":
	basicUnitTest()

	

	
		
