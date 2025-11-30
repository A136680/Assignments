📘 IoT Security Simulation Project

A Two-Part Demonstration of Secure IoT Data and Device Lifecycle

This project contains two simulation scripts that demonstrate essential security concepts used in IoT and embedded systems. The goal is to provide a clear, educational example of how IoT devices secure their data during transmission and how their full security lifecycle operates from boot to decommissioning.

🔒 Part I — IoT Device Data Encryption Simulation
📌 Overview

This script simulates an IoT temperature & humidity sensor. Before transmitting data to a base station, the device encrypts the readings using AES-GCM, a widely used authenticated encryption mode in resource-constrained IoT environments.

🧠 What It Demonstrates

Generation of sensor readings (temperature & humidity)

Encryption of the data using AES-128 GCM

Transmission of encrypted payload

Decryption and verification on the server side

Secure end-to-end data flow

▶️ How to Run

Install dependencies:

pip install pycryptodome


Run the script:

python iot_encryption_sim.py

✅ Expected Output

You will see:

Original sensor readings (JSON)

AES nonce, ciphertext, and authentication tag

Successfully decrypted data on the server side

Example:

=== Original Sensor Data (Before Encryption) ===
{ ... }

=== Encrypted Data (What goes over the air) ===
Nonce: 9b3a...
Ciphertext: 3caaf7...
Tag: 4f9b...

=== Decrypted Sensor Data (At Base Station) ===
{ ... }


This demonstrates secure and authenticated transmission between an IoT device and a base station.

🔐 Part II — IoT Device Lifecycle Simulation
📌 Overview

This script simulates the five primary security phases in the lifecycle of an IoT/embedded device. Each stage logs messages with timestamps to represent real-world device behavior.

🧬 Lifecycle Stages Simulated

Threat Modeling
Identify assets, entry points, and attacker profiles.

Secure Boot Initialization
Verify bootloader and firmware authenticity before system start.

Secure Key Injection
Device receives cryptographic keys (mock keys in this simulation).

OTA Firmware Update Check
Device checks for available firmware updates and verifies them.

Secure Decommissioning
Wipe keys, revoke credentials, and safely retire the device.

▶️ How to Run
python iot_lifecycle_sim.py

✅ Expected Output

Console logs showing each stage with timestamps, example:

[Stage 1] Threat model created...
[Stage 2] Secure boot verified...
[Stage 3] Keys injected securely...
[Stage 4] OTA update verified...
[Stage 5] Device decommissioned, secrets wiped.


Each log entry includes an ISO-timestamp and descriptive message.
