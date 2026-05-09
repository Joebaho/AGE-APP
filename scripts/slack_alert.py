import requests

# Replace with your actual Slack webhook URL
SLACK_WEBHOOK = "https://hooks.slack.com/services/YOUR/WEBHOOK/URL"

data = {
    "text": "🚨 AGE-APP Alert: High CPU detected or Deployment Issue!"
}

try:
    response = requests.post(SLACK_WEBHOOK, json=data)
    print("✅ Slack alert sent!" if response.status_code == 200 else "❌ Failed to send alert")
except:
    print("❌ Could not send Slack alert")