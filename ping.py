import time
from pythonping import ping
import csv

import argparse

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('--nameserver',
                    choices=["swisscom", "google", "cloudflare"],
                    action="store")

args = parser.parse_args()

nameservers = {"swisscom":"195.186.1.192", "google":"8.8.8.8", "cloudflare":"1.1.1.1"}

while True:
    ping_response = ping(nameservers[args.nameserver], verbose=True, size=1024, interval=0.5, count=20)

    with open(f"ping_{args.nameserver}.csv", 'a') as f:
        writer = csv.writer(f) #this is the writer object
        writer.writerow([time.time(), ping_response.rtt_avg_ms, ping_response.rtt_min_ms, ping_response.rtt_max_ms, ping_response.packet_loss])
