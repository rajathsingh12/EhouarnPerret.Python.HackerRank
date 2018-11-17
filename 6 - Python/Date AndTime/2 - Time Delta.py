from datetime import datetime

fmt = "%a %d %b %Y %H:%M:%S %z"  # http://strftime.org/ For the format
T = int(input())
for _ in range(T):
	dt1 = datetime.strptime(input(), fmt)
	dt2 = datetime.strptime(input(), fmt)
	print(abs(int((dt1 - dt2).total_seconds())))
