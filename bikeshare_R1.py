
# coding: utf-8

# In[1]:


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). 
    # HINT: Use a while loop to handle invalid inputs
    city = input('Would you like to see the data for Chicago, New York, or Washington?\n')
    while True: 
        cities = ['chicago', 'new york', 'washington']
        if city.lower() in cities:
            break
        else:
            city = input('Please enter the name of one of the above three cities:\n')
        
    isfilter = input('Would you like to filter the city\'s data by month, day, both, or not at all? Type "none" for no time filter\n')
    # TO DO: get user input for month (all, january, february, ... , june)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    while True:
        filter_condition = ['month','day','month','both','none']
        if isfilter in filter_condition:
            if isfilter.title() == 'None':
                month = 'all'
                day = 'all'
            elif isfilter.lower() == 'month':    
                month = input('Which month? January, February, March, April, May, or June?\n')
                day = 'all'
            elif isfilter.lower() == 'day':
                month = 'all'
                day = input('Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday?\n')
            else:
                month = input('Which month? January, February, March, April, May, or June?\n')
                day = input('Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday?\n')
            break
        else:
            isfilter = input('Please enter the right filter condition:\n')

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city.lower()])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'], errors = 'ignore')

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
#     df['day_of_week'] = df['Start Time'].dt.dayofweek
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # print(df['month'])
    # print(df['day_of_week'])
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = pd.Series(data=[1,2,3,4,5,6], index = months)[month.lower()]
        # month = months.index(month.lower()) + 1
        
    # print(month)
    
        # filter by month to create the new dataframe
        df = df[df['month']==month]
    # print(df)
    
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day.title()]
        
    #print(day)
#     print(df)

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'], errors = 'ignore')
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].value_counts().index[0]
    count_hour = df['hour'].value_counts().values[0]
    
#     print(df['month'].value_counts().size)
#     print(df['day_of_week'].value_counts().size)

    # TO DO: display the most common month
    # TO DO: display the most common day of week
    # TO DO: display the most common start hour
    
    # 获取'month'和'day_of_week'两列值的个数，通过这个值判断用户输入的过滤条件
    month_size = df['month'].value_counts().size 
    day_size = df['day_of_week'].value_counts().size
    
    if month_size == 1 and day_size == 1:
        print('Filter: both')
        print('Most common hour: {}, Count:{}'.format(common_hour, count_hour))
    elif month_size == 1:
        print('Filter: month')
        common_dayofweek = df['day_of_week'].value_counts().index[0]
        count_dayofweek = df['day_of_week'].value_counts().values[0]
        print('Most common day of week: {}, Count:{}'.format(common_dayofweek, count_dayofweek))
        print('Most common hour: {}, Count:{}'.format(common_hour, count_hour))
    elif day_size == 1:
        print('Filter: day')
        common_month = df['month'].value_counts().index[0]
        count_month = df['month'].value_counts().values[0]
        print('Most common month: {}, Count:{}'.format(common_month, count_month))
        print('Most common hour: {}, Count:{}'.format(common_hour, count_hour))
    else:
        print('Filter: none')
        common_month = df['month'].value_counts().index[0]
        count_month = df['month'].value_counts().values[0]
        print('Most common month: {}, Count:{}'.format(common_month, count_month))
        common_dayofweek = df['day_of_week'].value_counts().index[0]
        count_dayofweek = df['day_of_week'].value_counts().values[0]
        print('Most common day of week: {}, Count:{}'.format(common_dayofweek, count_dayofweek))
        print('Most common hour: {}, Count:{}'.format(common_hour, count_hour))
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].value_counts().index[0]
    count_start_station = df['Start Station'].value_counts().values[0]
    print('Most commonly used start station: {}, Count:{}'.format(common_start_station, count_start_station))
    
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].value_counts().index[0]
    count_end_station = df['End Station'].value_counts().values[0]
    print('Most commonly used end station: {}, Count:{}'.format(common_end_station, count_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    stations_count = df.groupby(['Start Station','End Station']).size() #分组统计station出现的次数
    count_max = stations_count.max() #计算station组合出现最多的次数，作为过滤条件
#     print(count_max)
#     print(stations_count)
    stations = stations_count[stations_count == count_max] #过滤出station组合
    stations = list(stations.index[0])
#     print(stations)
    print('Most frequent combination of start station and end station trip: ({} --> {}), Count:{}'
          .format(stations[0], stations[1], count_max))    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    count = df['Trip Duration'].size
#     print(count)

    # TO DO: display mean travel time
    avg_time = df['Trip Duration'].mean()
    print('Total Duration: {}, Count:{}, Avg Duration: {}'.format(total_time,count,avg_time))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
#     print(df)
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
#     print(user_types)
    print('{}: {}, {}: {}'.format(user_types.index[0],user_types[0],user_types.index[1],user_types[1]))
    
    # TO DO: Display counts of gender
    # TO DO: Display earliest, most recent, and most common year of birth
#     print(df['Gender'])
    try:
        gender = df['Gender'].value_counts()
        earliest_birth = df['Birth Year'].min()
        most_recent_birth = df['Birth Year'].max()
        most_common_birth = df['Birth Year'].value_counts().index[0]
        count_common_birth = df['Birth Year'].value_counts().values[0]
    except KeyError:
        print('This city has no data on gender or date of birth :(')
    else:
        print('{}: {}, {}: {}'.format(gender.index[0],gender[0],gender.index[1],gender[1]))
        print('The earliest year of birth is {}.'
              .format(earliest_birth))
        print('The most recent year of birth is {}.'.format(most_recent_birth))
        print('The most common year of birth is {}, Count:{}'.format(most_common_birth,count_common_birth))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        trip_duration_stats(df)
        station_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()

