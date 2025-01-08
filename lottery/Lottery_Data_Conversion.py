# Lottery Data Conversion
# Justin Pizano

"""
Goal: To take the lottery data and convert it into 
summary statistics.
"""

# Import Libraries
import pandas as pnd
import numpy as np
import os
from datetime import datetime

# Create a folder to put files in
os.makedirs('folder', exist_ok = True)

# Read the initial lottery data csv (note: the directory should be unique to your device)
lottery_data = pnd.read_csv('Lottery_Mega_Millions_Winning_Numbers__Beginning_2002.csv')



# Create an array of row numbers
lottery_row_numbers = np.arange(0, len(lottery_data))

# The index list of a winning number set
winner_index = np.arange(0, 5)


class Sheets:
    def __init__(self, name):
        if name == 'Month and Year':
            self.temporal_structure, self.name = 'MY', name
        else:
            self.temporal_structure, self.name = name, name
    
    # Converts the date to seconds from January 1, 2000
    def date_to_seconds(self, date):
        # The year two thousand as a datetime
        year_two_thousand = datetime.strptime('01/01/2000', '%m/%d/%Y')
        # The specific time delta
        spec_delta = date - year_two_thousand
        # returning the total seconds
        return spec_delta.total_seconds()
    
    """
    Function to replace dates with total seconds in a dictionary (adding dates separately)
    - dictionary: the dictionary to be updated (the main dictionary)
    - sub_dict: the dictionary containing the values needed (the sub dictionary)
    - temporal_key: the total seconds
    """
    def date_replacement(self, dictionary, sub_dict, temporal_key):
        # Update the dictionary with the sub dictionary items
        dictionary.update({sub_dict[temporal_key]['Date'] : sub_dict[temporal_key]})
        # Delete the previous temporal_key dictionary entry
        del dictionary[sub_dict[temporal_key]['Date']]
    
    # function to create the different sheets/files
    def statistic_creation(self, temporal_structure):
        # Instantiate the dictionaries
        lottery_dict = {}
        lottery_adv = {}
        # Run a for-loop using the row number array
        for row in lottery_row_numbers:
            # Draw Date
            draw_date = lottery_data['Draw Date'].iloc[row]
            # List of temporal indicators
            indicators = {
                'Year' : [draw_date[6:], 'output_year'],
                'Month' : [draw_date[0:2], 'output_month'],
                'MY' : [draw_date[0:2] + '/' + 
                draw_date[6:], 'output_MY'],
                'Date' : [lottery_data['Draw Date'].iloc[row], 'output_date']}
            # Days to put into structure
            days = {'MY' : 0, 'Date' : draw_date[3:5]}
            # the temporal indicator
            temporal_ind = indicators[temporal_structure][0]
            """
            The given new temporal indicator
            Through if-statements, etc.
            """
            if temporal_structure == 'Date':
                temporal_ind1 = self.date_to_seconds(datetime.strptime(temporal_ind, "%m/%d/%Y"))
            elif temporal_structure == 'MY':
                temporal_ind1 = self.date_to_seconds(datetime.strptime(temporal_ind, "%m/%Y"))
            else:
                temporal_ind1 = temporal_ind
            # The name for a given file
            file_name = indicators[temporal_structure][1]
            # The given winner variable
            winners = lottery_data['Winning Numbers'].iloc[row]
            # The list of given winning numbers
            winner_list = [int(winners[0:2]),
                           int(winners[3:5]), 
                           int(winners[6:8]), 
                           int(winners[9:11]), 
                           int(winners[12:14])]
            lottery_adv.update({temporal_ind1 : {'Variance' : np.var(winner_list), 
                                        'Standard Deviation' : np.std(winner_list)}})
            # try statement to add to the values
            try:
                # The count of the lottery numbers
                lottery_dict[temporal_ind1]['Count'] += 1
                # The sum of the winning numbers
                lottery_dict[temporal_ind1]['Winning Sum'] += sum(
                    winner_list)
                for number in winner_index:
                    # The string of winning number row
                    num_win_string = 'Winner ' + str(number + 1) + ' Total'
                    # Winning numbers each added to the total
                    lottery_dict[temporal_ind][num_win_string] += winner_list[number]
            except:
                # Count, sum, etc., created rather than added
                # Though with about the same process
                lottery_dict.update({temporal_ind1 : {'Count' : 1}})
                lottery_dict[temporal_ind1].update({'Winning Sum' : sum(
                    winner_list)})
                # Include the date depending on the temporal structure
                if temporal_structure == 'Date' or temporal_structure == 'MY':
                    lottery_dict[temporal_ind1].update({'Date' : temporal_ind})
                # loop of winning numbers to add each number
                for number in winner_index:
                    num_win_string = 'Winner ' + str(number + 1) + ' Total'
                    lottery_dict[temporal_ind1].update({num_win_string : winner_list[number]})
        
        
        # Instantiate new dictionaries to help sort data
        sorted_lottery_avgs = {}
        sorted_lottery_dict = {}
        sorted_lottery_adv = {}
        
        # For-loop that runs keys in order and updates them
        for temporal_key in sorted(lottery_dict):
            # Sorted dictionary update
            # Initial Statistics
            sorted_lottery_dict.update({temporal_key : lottery_dict[temporal_key]})
            # Averages
            sorted_lottery_avgs.update({temporal_key : {'Winning Number Average' :
                                            lottery_dict[temporal_key]['Winning Sum']/(
                                                lottery_dict[temporal_key]['Count']*5)}})
            # winning number loop for averages
            for number in winner_index:
                num_win_string = 'Winner ' + str(number + 1) + ' Total'
                num_avg_string = 'Winner ' + str(number + 1) + ' Average'
                sorted_lottery_avgs[temporal_key].update(
                    {num_avg_string :
                     lottery_dict[temporal_key][num_win_string]/(lottery_dict[temporal_key]['Count'])})
            sorted_lottery_adv.update({temporal_key : lottery_adv[temporal_key]})
            
            # temporal condition: replace the dates with the seconds
            if temporal_structure == 'Date' or temporal_structure == 'MY':
                self.date_replacement(sorted_lottery_dict, lottery_dict, temporal_key)
                self.date_replacement(sorted_lottery_adv, lottery_dict, temporal_key)
                
        # Place data into dataframe
        lottery_df = pnd.DataFrame(sorted_lottery_dict)
        
        # Make transpose to set the rows as years
        lottery_df_pr = lottery_df.T
        
        # Perform the same with averages as well as advanced statistics
        avgs_df = pnd.DataFrame(sorted_lottery_avgs)
        avgs_df_pr = avgs_df.T
        advs_df = pnd.DataFrame(sorted_lottery_adv)
        advs_df_pr = advs_df.T
        
        # Create Excel file (With years as the first row)
        with pnd.ExcelWriter('folder/' + file_name + '.xlsx') as writer:
            # temporal structure: update to seconds if the temporal structure
            # is initial a date
            if temporal_structure == 'Date' or temporal_structure == 'MY':
                temporal_structure = 'Seconds (from the beginning of the year 2000)'
            lottery_df_pr.to_excel(writer, sheet_name='Initial Data', index_label = temporal_structure)
            avgs_df_pr.to_excel(writer, sheet_name='Averages', index_label = temporal_structure)
            advs_df_pr.to_excel(writer, sheet_name='Advanced Statistics', index_label = temporal_structure)
        


# Instantiate each class and run each function
year = Sheets('Year')
month = Sheets('Month')
month_year = Sheets('Month and Year')
year = Sheets('Date')

year.statistic_creation('Year')
month.statistic_creation('Month')
month_year.statistic_creation('MY')
year.statistic_creation('Date')


