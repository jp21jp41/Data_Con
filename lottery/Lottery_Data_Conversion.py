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
from scipy import optimize

# Sinusoidal function to map (for later implementation)
def sinusoidal(x, a, b, c, d, z):
    return a * np.sin(b*x) + c * np.cos(d*x) + z

# Function to calculate the result of a polynomial
def poly_exp(x_value, coefficients):
    power = len(coefficients) - 1
    poly_value = coefficients[0]*(x_value**power)
    if power == 0:
        return poly_value
    return poly_value + poly_exp(x_value, coefficients[1:])

# Create a folder to put files in
os.makedirs('folder', exist_ok = True)

# Read the initial lottery data csv
lottery_data = pnd.read_csv(os.getcwd() + '\\Lottery_Mega_Millions_Winning_Numbers__Beginning_2002.csv')

# Create an array of row numbers
lottery_row_numbers = np.arange(0, len(lottery_data))

# The index list of a winning number set
winner_index = np.arange(0, 5)

# Class to create an excel file with various sheets
class Sheets:
    # Initializer
    def __init__(self, name):
        if name == 'Month and Year':
            self.temporal_structure, self.name = 'MY', name
        else:
            self.temporal_structure, self.name = name, name
        self.timelist = []
        self.avrlist = []
    
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
    def statistic_creation(self):
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
            # the temporal indicator
            temporal_ind = indicators[self.temporal_structure][0]
            """
            The given new temporal indicator
            Through if-statements, etc.
            """
            if self.temporal_structure == 'Date':
                temporal_ind1 = self.date_to_seconds(datetime.strptime(temporal_ind, "%m/%d/%Y"))
            elif self.temporal_structure == 'MY':
                temporal_ind1 = self.date_to_seconds(datetime.strptime(temporal_ind, "%m/%Y"))
            else:
                temporal_ind1 = temporal_ind
            # Store the file name
            self.file_name = indicators[self.temporal_structure][1]
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
                if self.temporal_structure == 'Date' or self.temporal_structure == 'MY':
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
            
            self.timelist.append(temporal_key)
            self.avrlist.append(sorted_lottery_avgs[temporal_key]['Winning Number Average'])
            
            # temporal condition: replace the dates with the seconds
            if self.temporal_structure == 'Date' or self.temporal_structure == 'MY':
                self.date_replacement(sorted_lottery_dict, lottery_dict, temporal_key)
                self.date_replacement(sorted_lottery_adv, lottery_dict, temporal_key)
                
        # Place data into dataframe
        lottery_df = pnd.DataFrame(sorted_lottery_dict)
        
        # Make transpose to set the rows as years
        lottery_df_pr = lottery_df.T
        
        # Final Time of Collections Listed
        self.final = int(self.timelist[len(self.timelist) - 1])
        
        # Perform the same with averages as well as advanced statistics
        avgs_df = pnd.DataFrame(sorted_lottery_avgs)
        avgs_df_pr = avgs_df.T
        advs_df = pnd.DataFrame(sorted_lottery_adv)
        advs_df_pr = advs_df.T
        
        # Store dataframes
        self.lottery_df = lottery_df_pr
        self.avgs_df = avgs_df_pr
        self.advs_df = advs_df_pr
        
    
    
    
    # Function to run a predictive model 
    def predictive_model(self, prediction_start, prediction_end, 
                         prediction_increment, y_data, y_data_index, 
                         model_set = ["poly", 1]):
        if self.name != "Month":
            prediction_x = prediction_start + prediction_increment
            if model_set[0] == "poly":
                model = np.polyfit([int(x) for x in self.timelist], y_data, model_set[1])
                y_data_index += " (Polynomial)"
            elif model_set[0] == "sinusoidal":
                model, cov = optimize.curve_fit(sinusoidal, [int(x) for x in self.timelist], y_data)
                y_data_index += " (Sinusoidal)"
            predictions = {}
            while prediction_x < prediction_end:
                if model_set[0] == "poly":
                    prediction_y = poly_exp(prediction_x, model)
                elif model_set[0] == "sinusoidal":
                    prediction_y = sinusoidal(prediction_x, 
                                              model[4], model[3], 
                                              model[2], model[1], 
                                              model[0])
                predictions.update({prediction_x : prediction_y})
                prediction_x += prediction_increment
                predictions_df = pnd.DataFrame(predictions, index = [
                    y_data_index]).T
            # Predictive analytics dataframe instantiated/concatenated through
            # the try-except
            try:
                self.predictions = pnd.concat([
                    self.predictions, predictions_df
                    ], axis = 1)
            except:
                self.predictions = predictions_df
    
    
    def upload_excel(self):
        # Create Excel file (With years as the first row)
        with pnd.ExcelWriter('folder/' + self.file_name + '.xlsx') as writer:
            # temporal structure: update to seconds if the temporal structure
            # is initial a date
            if self.temporal_structure == 'Date' or self.temporal_structure == 'MY':
                self.temporal_structure = 'Seconds (from the beginning of the year 2000)'
            self.lottery_df.to_excel(writer, sheet_name='Initial Data', index_label = self.temporal_structure)
            self.avgs_df.to_excel(writer, sheet_name='Averages', index_label = self.temporal_structure)
            self.advs_df.to_excel(writer, sheet_name='Advanced Statistics', index_label = self.temporal_structure)
            if self.name != "Month":
                self.predictions.to_excel(writer, sheet_name='Predictive Analytics', index_label = self.temporal_structure)


# Instantiate each class, run the data creation,
# and run predictive analytics
year = Sheets("Year")
month = Sheets("Month")
month_year = Sheets("Month and Year")
date = Sheets("Date")

# Create a dictionary to iterate values
time_dictionary = {0 : [year, 50, 1, 2], 
                   1 : [month, 1, 1, "NA"], 
                   2 : [month_year, 94608000, 2628000, 3], 
                   3 : [date, 94608000, 86400, 4]}

# Store the Sheets variables
model_types = ["poly", "sinusoidal"]

# Iteration to run various Sheets functions
for number in time_dictionary:
    time_list = time_dictionary[number]
    time_list[0].statistic_creation()
    time_diff = time_list[0].final + time_list[1]
    for item in time_list[0].avgs_df.keys():
        for model_type in model_types:
            time_list[0].predictive_model( 
                time_list[0].final, time_diff,  
                time_list[2], time_list[0].avgs_df[item], 
                item, [model_type, time_list[3]]) 
    time_list[0].upload_excel()

