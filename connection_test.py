import requests
import time

def test_internet_connectivity():
    url = "http://www.google.com"
    timeout = 10  # Set the timeout for the request (in seconds)

    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()  # Check for any HTTP errors
        assert response.status_code == 200, "Internet connection test failed"
    except requests.RequestException:
        assert False, "Internet connection test failed"

    # If the function doesn't raise an assertion error, the test is successful

def test_download_speed():
    # Replace YOUR_DOWNLOAD_URL with the URL of a large file for download speed testing
    url = "https://youtu.be/S8vs_vmCxyU"
    start_time = time.time()

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for any HTTP errors
        assert response.status_code == 200, "Download speed test failed"
    except requests.RequestException:
        assert False, "Download speed test failed"

    end_time = time.time()
    download_speed = len(response.content) / (end_time - start_time) / 1_000_000  # Convert to Mbps
    assert download_speed is not None, "Download speed test failed"

    print(f"Download Speed: {download_speed:.2f} Mbps")

def test_upload_speed():
    url = "https://file.io"
    file_to_upload = open("file_to_upload.txt", "rb")
    start_time = time.time()

    try:
        response = requests.post(url, files={"file": file_to_upload})
        response.raise_for_status()  # Check for any HTTP errors
        assert response.status_code == 200, "Upload speed test failed"
    except requests.RequestException:
        assert False, "Upload speed test failed"

    end_time = time.time()
    upload_speed = len(file_to_upload.read()) / (end_time - start_time) / 1_000_000  # Convert to Mbps
    assert upload_speed is not None, "Upload speed test failed"

    print(f"Upload Speed: {upload_speed:.2f} Mbps")
    file_to_upload.close()

# Test internet connectivity
test_internet_connectivity()

# Test download speed
test_download_speed()

# Test upload speed
test_upload_speed()

# If no assertion error is raised, all the tests are successful
print("All tests passed.")
