try:
	from mmsdk import mmdatasdk
	print ("CMU Multimodal SDK found!")
except:
	print ("SDK Not Found, Check Your PYTHONPATH? Did you install SDK correctly?")
	exit(-1)

try:
	import ChallengeHML20   
	print ("Challenge Helpers Found!")
except:
	print ("ACL Challenge Helpers Not Found, Check Your PYTHONPATH?")
	exit(-2)

print ("Welcome to ACL20 Challenge-HML CMU-MOSEI Subchallenge. SDK Works!")

