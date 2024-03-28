from flask import Flask, jsonify
import requests
import os

# Flask app to get hours from airtable. 

app = Flask(__name__)

url = 'https://api.airtable.com/v0/app9blsVedknHXPFF/denver_hours'
 
bearer_token = os.getenv('BEARER_TOKEN')

@app.route('/get')
def aggregate_hours():
    """
    Aggregate hours worked by each employee per day.

    Fetches records from an Airtable base and aggregates the total hours
    worked by each employee for each day. The response is formatted into JSON.

    Returns:
        JSON response containing aggregated hours worked per employee per day,
        or an error message with the corresponding status code if the request fails.
    """
    
    headers = {
        'Authorization': f'Bearer {bearer_token}'
    }
    # Url has all of the dates and the hours worked.
    response = requests.get(url=url, headers=headers)
    data = response.json()
    
    # If the call is succeeds returns the records.
    if response.status_code == 200 and 'records' in data:
        aggregates = {}
        for record in data['records']:
            fields = record['fields']
            employee_id = fields['ID']
            date = fields['Date']
            hours_worked = fields.get('Hours Worked', 0)
            key = (employee_id, date)
            # get values if key exists. Add and append hours worked if key exists
            aggregates[key] = aggregates.get(key,0)+hours_worked
		# put the aggregate records into a list
        result = []
        for (employee_id, date), hours_worked in aggregates.items():
            result.append({
                'ID': employee_id,
                'Date': date,
                'Total Hours Worked': hours_worked
            })
        # test with test.py
        return jsonify(result)
    else:
        return jsonify({'error': 'Failed to fetch data from Airtable'}), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
