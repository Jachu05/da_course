import pandas as pd

data = pd.read_csv("SampleCSVFile_119kb.csv", encoding='unicode_escape', engine='python',
                   names=['side_name', 'owner', 'factor_1', 'factor_2', 'factor_3', 'factor_4', 'side', 'department',
                          'summary'])

# Data filtration
nan_value_summary_mask = data['summary'].isin(['na', 'n/a'])
factor_1_positive_value_mask = data['factor_1'] > 0.0

filtered_data_mask = ~nan_value_summary_mask & factor_1_positive_value_mask

filtered_data = data[filtered_data_mask]
filtered_data["summary"] = pd.to_numeric(filtered_data["summary"], downcast="float")

xd = filtered_data.iloc[7]['summary']
xd = filtered_data['summary'] == '0.570.590.47'

grouped_data = filtered_data.groupby('owner')

# xd = grouped_data.get_group('Adrian Hane')

avg_owner_summary = grouped_data['summary'].mean()