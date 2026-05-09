import requests
import time
import sys

APP_URL = "http://YOUR_LOADBALANCER_DNS"   # Change after deployment

def check_app():
    try:
        response = requests.get(f"{APP_URL}/health", timeout=5)
        if response.status_code == 200:
            print("✅ Application is Healthy")
            print(response.json())
        else:
            print(f"⚠️ Application returned status: {response.status_code}")
    except Exception as e:
        print(f"❌ Application is Down or Unreachable: {e}")

if __name__ == "__main__":
    print("🚀 Starting Application Monitor...")
    while True:
        check_app()
        time.sleep(30)   # Check every 30 seconds