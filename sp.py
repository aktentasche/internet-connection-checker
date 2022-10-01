import speedtest
from pythonping import ping
import csv 
import time

while True:
    s = speedtest.Speedtest(secure=True)
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    s.results.share()

    results_dict = s.results.dict()


    with open(f"speedtest.csv", 'a') as f:
        writer = csv.writer(f) #this is the writer object
        writer.writerow([time.time(), results_dict["download"], results_dict["upload"], results_dict["ping"]])

    time.sleep(120)    

