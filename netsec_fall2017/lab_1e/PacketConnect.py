from playground.network.packet import PacketType
from playground.network.packet.fieldtypes import INT32,UINT32,STRING,BUFFER,BOOL


#packet1 
class RequestStringCompare(PacketType):
	DEFINITION_IDENTIFIER="lab1b.student_mengdi.RequestStringCompare"
	DEFINITION_VERSION="1.0"
	FIELDS=[
		("Question",STRING)
		]

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
		("id",INT32),
		("Answer",STRING)
		]

#packet4
class StringCompareResult(PacketType):
	DEFINITION_IDENTIFIER="lab1b.student_mengdi.StringCompareResult"
	DEFINITION_VERSION="1.0"

	FIELDS=[
		("id",INT32),
		("output",STRING),
		]



	

