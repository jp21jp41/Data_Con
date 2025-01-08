# L_D_Con
Lottery Data Conversion

A basic conversion of Data.Gov data on lottery which takes the data to convert into a set of statistics.

The resulting format: four excel files of various time scales, each with an Initial Data sheet, an Averages sheet, and an Advanced Statistics sheet, all in one folder.
The main statistics throughout: Averages, Sums, Variances, and Standard Deviations, of winning numbers at a given timespan.

Also included: Visual Basic files to automate the spreadsheets.

# Instructions

On line 19 of the Lottery_Data_Conversion.py file, replace the directory (which is, "Lottery_Mega_Millions_Winning_Numbers__Beginning_2002.csv") with
your directory. 
_(Optional at the moment)_ 
Then, you may simply run the file to get all of the data.
To format in excel, there are two very basic Visual files (as of now, they do not have very much utility). They simply automate the process of a specific
format of the data. 
To make the edits:
- Go to "Visual Basic" under "Developer" in Excel.
- Click "This Workbook" under the "Project" window of Visual Basic.
- File -> Import File -> the .bas file (the file with "For_MY_and_Date" is only for the excel files where the temporal structure is a date, i.e., "output_MY" or "output_date"). The other .bas file should be used with "output_year" and "output_month".

The edits are of every sheet, per excel file.

Note that the project only has one developer, so it takes time to make improvements. That also means the limitations are bound to said one developer.
