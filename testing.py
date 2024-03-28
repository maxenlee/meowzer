import pandas as pd
# import requests
# response = requests.get('http://127.0.0.1:5000/get')
# data = response.json()
# df = pd.DataFrame(data)

df = pd.read_json('http://127.0.0.1:5000/get')
print(f'hours by emp_id')
print(df.drop(columns=['Date']).groupby('ID').sum())
print('')
print(f'Total hours by Date')
print(df.drop(columns=['ID']).groupby('Date').sum())
print()
print(f"Total hours from {df['Date'].min()} to {(df['Date']).max()}")
print(df['Total Hours Worked'].sum())
