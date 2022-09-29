import speedtest
from pythonping import ping


servers = [3188] # iway.ch server

s = speedtest.Speedtest(secure=True)
s.get_servers(servers)
s.get_best_server()
s.download()
s.upload()
s.results.share()

results_dict = s.results.dict()
