import csv
import argparse

parser = argparse.ArgumentParser(description='Process a CSV file of hosts and ports.')
parser.add_argument('filename', type=str, help='the name of the CSV file')
args = parser.parse_args()
#filename = "filename.csv"  # Replace with the name of your CSV file

with open(args.filename) as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header row
    
    # Create a dictionary to store the hosts and ports for each name
    names_dict = {}
    
    # Loop through each row and add the host and port to the dictionary for the corresponding name
    for row in reader:
        host = row[0]
        protocol = row[1]
        port = row[2]
        name = row[3]
        
        if name not in names_dict:
            names_dict[name] = []
        names_dict[name].append((host, port))
        
    # Print the list of hosts and ports for each name
    for name, hosts_ports in names_dict.items():
        print(f"{name}:")
        for host, port in hosts_ports:
            print(f" {host}:{port}")
