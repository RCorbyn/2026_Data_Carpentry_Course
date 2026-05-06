# Import external packages
import matplotlib.pyplot as plt
import pandas as pd


def read_json_to_dataframe(input_path):
    """
    Read the data from a json file to a pandas dataframe.
    Clean the data by removing any rows where the duration entry is empty. 
    Args:
        input_path (file/string): File object/path to the json file

    Returns:
        eva_df: A pandas dataframe containing the cleaned data. 
    """
    print(f'Reading JSON file {input_path}')
    # Read the data from JSON file into a pandas dataframe
    # eva stands for extra vehicular activity
    eva_df = pd.read_json(input_path, convert_dates=['date'], encoding='ascii')
    eva_df['eva'] = eva_df['eva'].astype(float)
    # Clean the data by removing any rows where duration is missing
    eva_df.dropna(axis=0, subset=['duration', 'date'], inplace=True)
    return eva_df

def write_dataframe_to_csv(df, output_path):
    """
    Writes the pandas dataframe generated in the function 
    read_json_to_dataframe() to a .csv file

    Args:
        df (pandas dataframe): Input pandas dataframe containing data to save
        output_path (file path / string)): file path/object to the save location for the .csv 
    """
    print(f'Saving to CSV file {output_path}')
    # Save the dataframe to CSV file for later analysis
    df.to_csv(output_path, index=False, encoding='utf-8')

def plot_cummulative_time(df, graph_path):
    """
    Plot the cummulative time that all astronauts have spent 
    in space as a function of the date that the spacewalk occurred.

    1. Convert the the date column to number of hours 
    2. Caclulate the sum of all hours spent in space 
    3. Generate a plot of the cumulative time spent in space over the years 
    4. Save the generated plot 

    Args:
        df (pandas dataframe): Contains the cleaned data from the input file
        graph_path (string/path): file path for the generated plot to be saved to.
    """
    # Sort the values of the date column, ready to plot date values on the x axis. 
    df.sort_values('date', inplace=True)
    '''Add a new column to the dataframe to convert duration of 
    spacewalk to hours '''
    df['duration_hours'] = df['duration'].str.split(":").apply(lambda x: int(x[0]) + int(x[1])/60)
    # Caculate the total time spent on spacewalks throughout history
    df['cumulative_time'] = df['duration_hours'].cumsum()

    # plot the date of spacewalk (year) vs time spent on the walk (Hours)
    plt.plot(df['date'], df['cumulative_time'], 'ko-')
    plt.xlabel('Year')
    plt.ylabel('Total time spent in space to date (hours)')
    plt.tight_layout()
    # Save the results
    plt.savefig(graph_path)
    plt.show()
    return(1)

print('-- Start --')

# Data source: https://data.nasa.gov/resource/eva.json (with modifications)
input_file = open('./eva_data.json', 'r', encoding='ascii')
output_file = open('./eva_data.csv', 'w', encoding='utf-8')
graph_file = './cumulative_eva_graph.png'

print(f'Read in data from file {input_file}')
eva_data= read_json_to_dataframe(input_file)

print(f'Save data to file {output_file}')
write_dataframe_to_csv(eva_data, output_file)

print('Plot results')
plot_cummulative_time(eva_data, graph_file)

print('--END--')
