import requests

# Replace with your actual Slack webhook URL
SLACK_WEBHOOK = "https://hooks.slack.com/services/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"

data = {
    "text": "🚨 AGE-APP Alert: High CPU detected or Deployment Issue!"
}

try:
    response = requests.post(SLACK_WEBHOOK, json=data)
    print("✅ Slack alert sent!" if response.status_code == 200 else "❌ Failed to send alert")
except:
    print("❌ Could not send Slack alert")