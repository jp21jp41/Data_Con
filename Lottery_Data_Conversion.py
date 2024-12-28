# Lottery Data Conversion
# Justin Pizano

"""
Goal: To take the lottery data and convert it into 
summary statistics.
"""

# Import Libraries
import pandas as pnd
import numpy as np


# Read the initial lottery data csv
lottery_data = pnd.read_csv('C:/Users/justi/OneDrive/Documents/All_Backups_etc/Lottery_Mega_Millions_Winning_Numbers__Beginning_2002.csv')

# Instantiate the dictionary
lottery_dict = {}

# Create an array of row numbers
lottery_row_numbers = np.arange(0, len(lottery_data))

# The index list of a winning number set
winner_index = np.arange(0, 5)

# Run a for-loop using the row number array
for row in lottery_row_numbers:
    # The given year variable
    year = lottery_data['Draw Date'].iloc[row][6:]
    # The given winner variable
    winners = lottery_data['Winning Numbers'].iloc[row]
    # The list of given winning numbers
    winner_list = [int(winners[0:2]),
                   int(winners[3:5]), 
                   int(winners[6:8]), 
                   int(winners[9:11]), 
                   int(winners[12:14])]
    # try statement to add to the values
    try:
        # The count of the lottery numbers
        lottery_dict[year]['Count'] += 1
        # The sum of the winning numbers
        lottery_dict[year]['Winning Sum'] += sum(
            winner_list)
        for number in winner_index:
            # The string of winning number row
            num_win_string = 'Winner ' + str(number + 1) + ' Total'
            # Winning numbers each added to the total
            lottery_dict[year][num_win_string] += winner_list[number]
    except:
        # Count, sum, etc., created rather than added
        # Though with about the same process
        lottery_dict.update({year : {'Count' : 1}})
        lottery_dict[year].update({'Winning Sum' : sum(
            winner_list)})
        for number in winner_index:
            num_win_string = 'Winner ' + str(number + 1) + ' Total'
            lottery_dict[year].update({num_win_string : winner_list[number]})
    

# Instantiate new dictionary to help sort data
sorted_lottery_dict = {}

# For-loop that runs keys in order and updates them
for year_key in sorted(lottery_dict):
    # Sorted dictionary update
    # Initial Statistics
    sorted_lottery_dict.update({year_key : lottery_dict[year_key]})
    # Winning Average
    sorted_lottery_dict[year_key].update(
        {'Winning Average' : 
         lottery_dict[year_key]['Winning Sum']/(lottery_dict[year_key]['Count']*5)}
            )

# Place data into dataframe
lottery_df = pnd.DataFrame(sorted_lottery_dict)

# Make transpose to set the rows as years
lottery_df_pr = lottery_df.T

# Create CSV (With years as the first row)
lottery_df_pr.to_csv(
    'lottery_year_results.csv', index_label = 
        'Year')



