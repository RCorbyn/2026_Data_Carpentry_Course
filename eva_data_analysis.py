# Import external packages
import matplotlib.pyplot as plt
import pandas as pd

# Data source: https://data.nasa.gov/resource/eva.json (with modifications)
input_file = open('./eva_data.json', 'r', encoding='ascii')
output_file = open('./eva_data.csv', 'w', encoding='utf-8')
graph_file = './cumulative_eva_graph.png'
# Read data into a pandas dataframe 
eva_df = pd.read_json(input_file, convert_dates=['date'], encoding='ascii')
# Convert the 'eva' column in the code to a float 
eva_df['eva'] = eva_df['eva'].astype(float)
# Remove any NAN values in the dataframe. 
eva_df.dropna(axis=0, subset=['duration', 'date'], inplace=True)
# Export eva_dataframe to a csv file
eva_df.to_csv(output_file, index=False, encoding='utf-8')
# Sort the values of the date column
eva_df.sort_values('date', inplace=True)
'''Add a new column to the dataframe to convert duration of 
 spacewalk to hours '''
eva_df['duration_hours'] = eva_df['duration'].str.split(":").apply(lambda x: int(x[0]) + int(x[1])/60)
# Caculate the total time spent on spacewalks throughout history
eva_df['cumulative_time'] = eva_df['duration_hours'].cumsum()
print(eva_df)

# plot the date of spacewalk (year) vs time spent on the walk (Hours)
plt.plot(eva_df['date'], eva_df['cumulative_time'], 'ko-')
plt.xlabel('Year')
plt.ylabel('Total time spent in space to date (hours)')
plt.tight_layout()
# Save the results
plt.savefig(graph_file)
plt.show()