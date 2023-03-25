import csv
import argparse

parser = argparse.ArgumentParser(description='Process a CSV file of hosts and ports.')
parser.add_argument('filename', type=str, help='the name of the CSV file')
args = parser.parse_args()

hosts_by_port = {}

with open(args.filename, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        host = row['Host']
        port = row['Port']
        if port not in hosts_by_port:
            hosts_by_port[port] = set()
        hosts_by_port[port].add(host)

for port in sorted(hosts_by_port.keys(), key=int):
    hosts = hosts_by_port[port]
    print(f"{port}: {','.join(sorted(hosts))}")
