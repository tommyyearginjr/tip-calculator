print(' TIP CALCULATOR'+'\n '+((len('TIP CALCULATOR'))*'-'))

for i in range(0,101,1):
	t = str("{:.2f}".format(round((i*.15),2)))
	i = str(i)
	print("${} ===> ${}".format(i.zfill(3), t.zfill(5)))
