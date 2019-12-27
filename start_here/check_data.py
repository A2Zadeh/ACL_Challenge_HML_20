import mmsdk
from mmsdk import mmdatasdk

folders=["cmumosei_"+x for x in ["raw","extra","highlevel","labels"]]

output=open("stats.st","w")
for f in folders:

	c=mmdatasdk.mmdataset(f)
	for key in c.keys():
		keyys=list(c[key].keys())
		print(str(key)+" "+str(len(keyys))+" "+str(c[key][keyys[0]]["features"].shape),file=output)


