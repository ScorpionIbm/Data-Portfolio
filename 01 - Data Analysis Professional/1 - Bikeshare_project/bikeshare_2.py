import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    # dictionaries to match with user input
    cities = {'a':'chicago', 'b':'new york city', 'c':'washington'}
    months = {'a':'january', 'b':'february', 'c':'march', 'd':'april', 'e':'may', 'f':'june', 'z':'all', '':'all'}
    days = {'a':'saturday', 'b':'sunday', 'c':'monday', 'd':'tuesday', 'e':'wednesday', 'f':'thursday', 'g':'friday', 'z':'all', '':'all'}
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        message = ''
        for key, item in cities.items():
            message += '\n{}) {}'.format(key, item.title())
        city = input('Select city for analysis:' + message + '\nYour selection: ').lower()
        if city in cities:
            city = cities[city]
            print('Selected city is ' + city.title() + '\n')
            break
        else:
            print('City not in dataset, please select input from the list\n')

    # get user input for month (all, january, february, ... , june)
    while True:
        message = ''
        for key, item in months.items():
            if key == '':
                pass
            else:
                message += '\n{}) {}'.format(key, item.title())
        month = input('Select letter corresponding to month name for analysis: ' + message + '\nYour selection: ').lower()
        if month in months:
            month = months[month]
            print('Selected month is ' + month.title() + '\n')
            break
        else:
            print('Invalid input, please select letter from the list\n')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        message = ''
        for key, item in days.items():
            if key == '':
                pass
            else:
                message += '\n{}) {}'.format(key, item.title())
        day = input('Select letter corresponding to day name for analysis: ' + message + '\nYour selection: ').lower()
        if day in days:
            day = days[day]
            print('Selected day is ' + day.title() + '\n')
            break
        else:
            print('Invalid input, please select letter from the list\n')

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #Read data file and compute required new columns for calculating statistics
    df = pd.read_csv(CITY_DATA[city])
    #add extra columns required for analysis
    df['month'] = pd.DatetimeIndex(df['Start Time']).month_name()
    df['day'] = pd.DatetimeIndex(df['Start Time']).day_name()
    df['hour'] = pd.DatetimeIndex(df['Start Time']).hour

    #apply month and day filters
    if month == 'all':
        pass
    else:
        is_month = df['month']==month.title()
        df = df[is_month]
    if day == 'all':
        pass
    else:
        is_day = df['day']==day.title()
        df = df[is_day]

    #ask if user wants to print 5 lines of the dataset
    ask_print = input('\nDo you want to show the first 5 data points:\nyes or no? ').lower()
    start = 0
    end = 5
    if ask_print in ['yes','y']:
        print(df.iloc[start:end,1:-3].to_string(index=False))
    #ask if user wants to print 5 extra lines
    while ask_print in ['yes','y']:
        ask_print = input('\nShow 5 extra data points:\nyes or no? ').lower()
        if ask_print in ['yes','y']:
            start += 5
            end += 5
            print('\nPrinting 5 more rows:\n')
            print(df.iloc[start:end,1:-3].to_string(index=False))
        else:
            break

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    month = df['month'].mode()[0]
    print('The most frequently occuring month is : ' + month)


    # display the most common day of week
    day = df['day'].mode()[0]
    print('The most frequently occuring day of the week is : ' + day)


    # display the most common start hour
    hour = df['hour'].mode()[0]
    print('The most frequently occuring hour of the day is : ' + str(hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is : ' + start_station)

    # display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is : ' + end_station)

    # display most frequent combination of start station and end station trip
    #create new column to get combination of start and end station
    df['Trip Start:End'] = df['Start Station'] + ' to ' + df['End Station']
    trip_combination = df['Trip Start:End'].mode()[0]
    print('The most commonly used combination of start & end stations is : ' + trip_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def print_time_parts(print_text, seconds):
    """print how many days, hours, minutes and seconds are in seconds input."""
    to_days = 24*60*60
    to_hours = 60*60
    to_minutes = 60
    days = int(seconds//to_days)
    hours = int((seconds-days*to_days)//to_hours)
    minutes = int((seconds-days*to_days-hours*to_hours)//to_minutes)
    seconds = round((seconds-days*to_days-hours*to_hours-minutes*to_minutes),3)
    message = print_text + ' travel time is:'

    if days == 0:
        if hours == 0:
            if minutes == 0:
                message += ' {} seconds.'.format(seconds)
            else:
                message += ' {} minutes,'.format(minutes)
                message += ' {} seconds.'.format(seconds)
        else:
            message += ' {} hours,'.format(hours)
            message += ' {} minutes,'.format(minutes)
            message += ' {} seconds.'.format(seconds)
    else:
        message += ' {} days,'.format(days)
        message += ' {} hours,'.format(hours)
        message += ' {} minutes,'.format(minutes)
        message += ' {} seconds.'.format(seconds)

    return message

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    travel_time = df['Trip Duration'].sum()
    print(print_time_parts('Total',travel_time))

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(print_time_parts('Mean',mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Data summary by user type:')
    user_count=df.groupby(['User Type'])['User Type'].count()
    for index, value in user_count.items():
        print(index + ' : ' + str(value))
    # Display counts of gender
    try:
        print('\nData summary by gender:')
        gender_count = df.groupby(['Gender'])['Gender'].count()
        for index, value in gender_count.items():
            print(index + ' : ' + str(value))
    #exception handler for missing columns in dataset
    except KeyError:
        print('No gender data available for this city')
    # Display earliest, most recent, and most common year of birth
    try:
        earliest = df['Birth Year'].min()
        print('\nThe earliest year of birth is: ' + str(int(earliest)))
        most_recent = df['Birth Year'].max()
        print('The most recent year of birth is: ' + str(int(most_recent)))
        most_common = df['Birth Year'].mode()[0]
        print('The most common year of birth is: ' + str(int(most_common)))
    #exception handler for missing columns in dataset
    except KeyError:
        print('No birthdate data available for this city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() not in ['yes','y']:
            break


if __name__ == "__main__":
    main()



