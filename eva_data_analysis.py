# Import external packages
import matplotlib.pyplot as plt
import pandas as pd
import sys
import re

def main(input_file, output_file, graph_file):
    print("--START--")

    # Read the data from JSON file
    eva_data = read_json_to_dataframe(input_file)

    # Calculate and add crew size to data
    eva_data = add_crew_size_column(eva_data) # added this line

    # Convert and export data to CSV file
    write_dataframe_to_csv(eva_data, output_file)

    # Sort dataframe by date ready to be plotted (date values are on x-axis)
    eva_data.sort_values('date', inplace=True)

    # Plot cumulative time spent in space over years
    plot_cumulative_time_in_space(eva_data, graph_file)

    print("--END--")


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

def calculate_crew_size(crew):
    """
    Calculate the size of the crew for a single crew entry

    Args:
        crew (str): The text entry in the crew column containing a list of crew member names

    Returns:
        (int): The crew size
    """
    if crew.split() == []:
        return None
    else:
        return len(re.split(r';', crew))-1


def add_crew_size_column(df):
    """
    Add crew_size column to the dataset containing the value of the crew size

    Args:
        df (pd.DataFrame): The input data frame.

    Returns:
        df_copy (pd.DataFrame): A copy of the dataframe df with the new crew_size variable added
    """
    print('Adding crew size variable (crew_size) to dataset')
    df_copy = df.copy()
    df_copy["crew_size"] = df_copy["crew"].apply(
        calculate_crew_size
    )
    return df_copy

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
    df = add_duration_hours(df)
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

def text_to_duration(duration):
    """
    Convert a text format duration "HH:MM" to duration in hours

    Args:
        duration (str): The text format duration

    Returns:
        duration_hours (float): The duration in hours
    """
    hours, minutes = duration.split(":")
    duration_hours = int(hours) + int(minutes)/60  # there is an intentional bug on this line (should divide by 60 not 6)
    return duration_hours


def add_duration_hours(df):
    """
    Add duration in hours (duration_hours) variable to the dataset

    Args:
        df (pd.DataFrame): The input dataframe.

    Returns:
        df_copy (pd.DataFrame): A copy of df with the new duration_hours variable added
    """
    df_copy = df.copy()
    df_copy["duration_hours"] = df_copy["duration"].apply(
        text_to_duration
    )
    return df_copy



if __name__ == "__main__":

    if len(sys.argv) < 3: 
        # Data source: https://data.nasa.gov/resource/eva.json (with modifications)
        input_file = open('./Data/eva_data.json', 'r', encoding='ascii')
        output_file = open('./results/eva_data.csv', 'w', encoding='utf-8')
        print("Using default input and output lines")
    else:
        # Use the input arguments from the command line 
        input_file = sys.argv[1]
        create_results_folder(input_file)
        output_file = sys.argv[2]
        print("Using custom input and output filenames")

    graph_file = './results/cumulative_eva_graph.png'
    main(input_file, output_file, graph_file)


