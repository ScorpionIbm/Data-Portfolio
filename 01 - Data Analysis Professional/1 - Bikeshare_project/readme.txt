defined dictionaries for easier printing of choices and to match against user input

used multiple pandas and numpy documentation pages

used DatetimeIndex() class from pandas documentation and used its different methods and attributes to extract month names and day names and hour from start time

used boolean filters to filter dataset for months and days

used pandas to_string() method to manipulate the printed parts of the dataframe

used if with in list[] to allow for multiple print input by user

used dataframe slicing techniques with iloc[] and a loop to print parts of the dataset

computed most frequent requirements with the mode() method of pandas Series from documentation and used the first element from the generated mode() series using mode()[0]

combined Start and end station columns using Series operations to get station combination for mode() computation

wrote print_time_parts() to use in printing the Total travel time and mean travel time
also used built-in functions as round() to overcome float representation of milliseconds in time

used groupby() dataframe method and count() Series method to compute the count of user types and gender and iterate over the generated index and values of the series using Series items() method for printing output

used try and except blocks to handle exceptions when dealing with datasets that don't have user types and gender data
