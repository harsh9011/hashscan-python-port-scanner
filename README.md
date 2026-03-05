# HashScan 🔎

HashScan is a simple multithreaded port scanner built in Python.  
It scans ports on a target machine and identifies which ports are open.

This project was built to understand networking, socket programming, and multithreading in Python while learning cybersecurity concepts.

---

## Features

- Scans ports **1–1024**
- Detects **open ports**
- Uses **multithreading** for faster scanning
- Handles connection errors with **exception handling**
- Displays **scan completion time**

---

## Technologies Used

- Python
- Socket Programming
- Threading
- Vim (used for writing the code)

---

## How It Works

The program attempts to connect to each port on a target system using Python sockets.  
If the connection is successful, the port is reported as **OPEN**.

Port scanning is commonly used in **cybersecurity reconnaissance** to identify services running on a system.

Example services:

| Port | Service |
|-----|------|
| 22 | SSH |
| 80 | HTTP |
| 443 | HTTPS |

---

## Example Output
enter target : youtube.com
starting HashScan v1.0
Scanning target : youtube.com
port 443  is OPEN
port 80  is OPEN
Scan Completed in :  1.1747219562530518 Seconds
