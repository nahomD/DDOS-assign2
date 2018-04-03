import threading
class MyThread(threading.Thread):
	def __init__(self,func,args,threadId,threadName):
		threading.Thread.__init__(self)
		self.threadId=threadId
		self.threadName=threadName
		self.func=func
		self.args=args
		self._stop_event = threading.Event()
	def run(self):
		try:
			while self._stop_event.is_set()==False:
				self.func(*self.args)
				print("\nAttacking..."+self.threadName+"\n")
		except RuntimeError as e:
			#print("Exception")
			print(e,self.threadName)
			self.stop()
		except Exception as e:
			#print("Exception")
			print(e,self.threadName)
	def stop(self):
		self._stop_event.set()
		# self.join()
