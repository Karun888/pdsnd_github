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
    print('Hello! Let\'s explore some US bikeshare data! Please choose from the following cities: Chicago, New_York_City, or Washington')
    # Get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Please select a city : ")
        city = city.strip().lower()
        if city in ['chicago', 'new york city', 'washington'] :
            print('Excellen Choice!')
            print("Please choose one of the following : all, january, february, march, april, may, june")
            break
    else:
        print("Please select a valid ciy")
    # Get user input for month (all, january, february, ... , june)
    while True:
        month = input("Please choose a month : ")
        month = month.strip().lower()
        if month in ['january','february','march','april','may','june','all']:
            print('ok great!')
            print ('Lastly select one of the following days : all, saturday, sunday, monday, tuesday, wednesday, thursday, or, friday')
            break
    else:
        print("please choose a valid month")
    # Get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please choose a day : ")
        day = day.lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            print("OK!! hold your breath")
            break
        else:
            print("Please choose a valid day")
            
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
   
    df = pd.read_csv(CITY_DATA[city])
    
    
    # converting Start_Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    
    # new columns created as per months and days of the week
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
    
        # create new column from month filter
        df = df[df['month'] == month]

        
    # filter by day of week if applicable
    if day != 'all':
                
        df = df[df['day_of_week'] == day.title()]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    
    # Display the most common month
    Common_month = df['month'].mode()[0]
    print('Most Common month:', Common_month)

    
    # Display the most common day of week
    Common_day = df['day_of_week'].mode()[0]
    print('Most Common day:', Common_day)
    
    
    # Display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    Common_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', Common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    
    # Display most commonly used start station
    Common_start_station = df['Start Station'].mode()[0]
    print('Most Common start station:', Common_start_station)
   

    # Display most commonly used end station
    Common_end_station = df['End Station'].mode()[0]
    print('Most Common end Station:', Common_end_station)

    
    # Display most frequent combination of start station and end station trip
    Most_frequent_combination = df['Start Station'] + df['End Station'].mode()[0]
    print('Most frequent combination:', Most_frequent_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    
    # Display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('total travel time:', total_travel_time)

    
    # Display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print('mean travel:', mean_travel)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    
    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    
    # Display counts of gender
    try:
        gender_types = df['Gender'].value_counts()
        print('Gender Types:', gender_types)
    except KeyError:
            print("No data available.") 


    # Display earliest, most recent, and most common year of birth
    try:
      Earliest_Year = df['Birth Year'].min()
      print('Most earliest year:', Earliest_Year)
    except KeyError:
      print("No data available.")

    try:
      Most_Recent_Year = df['Birth Year'].max()
      print('Most Recent Year:', Most_Recent_Year)
    except KeyError:
      print("No data available.")

    try:
      Most_Common_Year = df['Birth Year'].value_counts().idxmax()
      print('Most Common Year:', Most_Common_Year)
    except KeyError:
      print("Sorry, no data available.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    x = 1
    while True:
        raw = input('Do you want to see raw data? yes or no: ')
        if raw.lower() == 'yes':
          print(df[x:x+5])
          x = x+5
        else:
            break

    
 
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to Restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


            
if __name__ == "__main__":
	main()

