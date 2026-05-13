from flask import Flask, render_template, request, jsonify
from datetime import datetime
import random
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# NEW CODE GENERATION: first 3 letters of day - age - random number
def generate_code(day_name, age):
    """
    day_name: full day name, e.g. 'Monday'
    age: integer age
    returns: e.g. 'MON-25-8472'
    """
    day_prefix = day_name[:3].upper()          # first three letters, uppercase
    random_num = random.randint(10000, 99999)  # 5‑digit random number
    return f"{day_prefix}-{age}-{random_num}"

def get_primary_category(age):
    if age <= 17: return "Minor"
    elif age <= 24: return "Young Adult"
    elif age <= 44: return "Adult"
    elif age <= 64: return "Middle Age"
    else: return "Senior"

def get_secondary_category(age):
    if age <= 1: return "Infant"
    elif age <= 3: return "Toddler"
    elif age <= 12: return "Child"
    elif age <= 19: return "Adolescent/Teen"
    elif age <= 35: return "Young Adult"
    elif age <= 55: return "Middle Adult"
    elif age <= 74: return "Senior Adult"
    else: return "Elderly"

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            birthday_input = request.form.get('birthday')

            birthday = datetime.strptime(birthday_input, "%Y-%m-%d")
            today = datetime.today()
            age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))

            day_of_week = birthday.strftime("%A")

            # Use the NEW generate_code with day name and age
            user_code = generate_code(day_of_week, age)

            result = {
                'first_name': first_name,
                'last_name': last_name,
                'birthday': birthday_input,
                'day': day_of_week,
                'age': age,
                'primary_category': get_primary_category(age),
                'secondary_category': get_secondary_category(age),
                'user_code': user_code
            }
            logger.info(f"Profile generated for {first_name} {last_name} | User code: {user_code}")
            return render_template('index.html', result=result)
        except Exception as e:
            logger.error(f"Error: {str(e)}")
            return "<h3 style='color:red'>Invalid date format. Use YYYY-MM-DD.</h3>"

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)