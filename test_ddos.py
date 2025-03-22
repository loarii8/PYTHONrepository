import requests
import multiprocessing

def send_request():
    url = "http://localhost:8000/qrqr.html"
 # Adjust to your local server URL
    try:
        response = requests.get(url)
        print(f"Response: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    processes = []
    for _ in range(100):  # Number of concurrent requests
        p = multiprocessing.Process(target=send_request)
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
