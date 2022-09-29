import speedtest
from pythonping import ping

foo = ping('127.0.0.1', verbose=True)

servers = [3188] # iway.ch server
# If you want to test against a specific server
# servers = [1234]

threads = None
# If you want to use a single threaded test
# threads = 1

s = speedtest.Speedtest(secure=True)
s.get_servers(servers)
s.get_best_server()
s.download()
s.upload()
s.results.share()

results_dict = s.results.dict()
pass