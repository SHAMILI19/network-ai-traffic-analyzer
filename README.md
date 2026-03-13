# Network AI Traffic Analyzer

A Python-based project for capturing, analyzing, and classifying network traffic using machine learning models. This tool processes network packets, extracts features, and predicts traffic patterns to help with network monitoring and cybersecurity research.

## Features

- Capture network traffic from `.pcap` files or live network interfaces.
- Extract relevant features for analysis using `packet_extractor.py`.
- Train machine learning models to classify network traffic.
- Predict traffic patterns in real-time using `detect_traffic.py`.
- Save and load trained models (`network_model.pkl`) for reuse.

## Project Structure
network_ai_project/
├── detect_traffic.py # Script to detect and classify traffic
├── packet_extractor.py # Script to extract features from packets
├── train_model.py # Script to train the ML model
├── network_dataset.csv # Dataset generated from packet capture
├── traffic_capture.pcap # Sample packet capture file
├── network_model.pkl # Trained ML model
└── README.md # Project overview and instructions

## Requirements
- Python 3.8 or higher
- Packages: `scikit-learn`, `pandas`, `numpy`, `scapy`, `joblib`
Install dependencies using:
```bash
pip install -r requirements.txt
Usage
1. Extract features from a pcap file
python packet_extractor.py -i traffic_capture.pcap -o network_dataset.csv
2. Train the model
python train_model.py -d network_dataset.csv -m network_model.pkl
3. Detect network traffic
python detect_traffic.py -m network_model.pkl -i traffic_capture.pcap
Contributing

Contributions are welcome! Feel free to fork the repository, make improvements, and submit pull requests.
Author
SHAMILI MANNEM
pip install -r requirements.txt
