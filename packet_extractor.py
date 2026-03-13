import pandas as pd
from scapy.all import rdpcap
#input and output filenames
import sys

if len(sys.argv) != 3:
    print("Usage: python3 packet_etractor.py <input.pcap> <output.csv>")
    sys.exit(1)
pcap_file = sys.argv[1]
csv_file = sys.argv[2]
#read packets
packets = rdpcap(pcap_file)
#extract basic info for each packet
data = []
for pkt in packets:
    pkt_dict = {
        "time": pkt.time,
        "len": len(pkt),
        "summary": pkt.summary()
    }
    data.append(pkt_dict)
#convert to dataframe
df = pd.DataFrame(data)
#save CSV
df.to_csv(csv_file, index=False)
print(f"CSV file generated successfully")
