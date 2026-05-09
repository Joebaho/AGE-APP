import requests
import os
import sys

# Get Slack webhook from environment variable (secure)
SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK")

def send_slack_alert(message="General Alert from AGE-APP"):
    if not SLACK_WEBHOOK:
        print("⚠️  SLACK_WEBHOOK_URL environment variable is not set!")
        return False

    data = {
        "text": f"🚨 AGE-APP Alert\n{message}"
    }

    try:
        response = requests.post(SLACK_WEBHOOK, json=data, timeout=10)
        if response.status_code == 200:
            print("✅ Slack alert sent successfully!")
            return True
        else:
            print(f"❌ Failed to send Slack alert. Status: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error sending Slack alert: {e}")
        return False


if __name__ == "__main__":
    if len(sys.argv) > 1:
        send_slack_alert(sys.argv[1])
    else:
        send_slack_alert("Test Alert: AGE-APP Monitoring")