#!/usr/bin/python
from libyate import Yate
from libvbts import YateMessenger
import base64
import logging
import sys

class YateOriginator:
	""" initialize the object """
	def __init__(self):
		self.app = Yate()
		self.app.__Yatecall__ = self.yatecall
		self.log = logging.getLogger("libvbts.yate.VBTS_Originate_Call.YateOriginator")
		self.ym = YateMessenger.YateMessenger()

	def yatecall(self, d):
		self.app.Output("YateSMSSender Event: " + self.app.type )

	def originate(self, args):
		self.app.Yate("call.execute")
		self.app.params = []
		self.app.params.append(["callto", "tone/dial"])
		self.app.params.append(["caller", "IMSI460010018073482"])
		self.app.params.append(["direct", "sip/sip:IMSI460010018073482@127.0.0.1:5062"])
		self.app.Dispatch() 
		     
	def close(self):
		self.app.close()
		
if __name__ == '__main__':
	import getopt
	logging.basicConfig(filename="/tmp/VBTS.log", level="DEBUG")
	logging.getLogger("libvbts.yate.VBTS_Originate_Call.__main__")
	y = YateOriginator()
	y.originate(sys.argv[1:])
	y.close()