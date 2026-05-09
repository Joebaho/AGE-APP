import random
import time

print("🤖 AI Monitoring Started...")

while True:
    cpu = random.randint(10, 95)
    if cpu > 80:
        print(f"🚨 AI Alert: High CPU Usage detected - {cpu}%")
    else:
        print(f"✅ System Healthy - CPU: {cpu}%")
    time.sleep(30)