# By: Faisal Algahtani

import time
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import calendar




def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('-'*40)
    print('Hello! Let\'s explore some US bikeshare data!')
    print('-'*40)
    print()
    print("We have following cities:\n1) Chicago\n2) New_York\n3) Washington")
    city = input(str("Pleae Enter City Name: "))
    month = input(str("Pleae Enter Month Name: \nIf you want to Specify Month, please type All: "))
    day = input(str("Pleae Enter Day Name: "))
    return city,month,day



def load_data(city,month,day):
    f = "no"
    city  = city.lower()
    month  = month.lower()
    day  = day.lower()
    if city == 'chicago':
        Chicago = pd.read_csv("chicago.csv")
        if month !='all':
            f = "yes"
            Chicago['Start Time'] = pd.to_datetime(Chicago['Start Time'])
            Chicago['Month'] = Chicago['Start Time'].dt.month_name()
            Chicago['Month'] = Chicago['Month'].str.lower()
            Chicago = Chicago[Chicago['Month']==month]
            Chicago = Chicago.reset_index(drop = True)
            Chicago['Day'] = Chicago['Start Time'].dt.day_name()
            Chicago['Day'] = Chicago['Day'].str.lower()
            Chicago = Chicago[Chicago['Day']==day]
            Chicago = Chicago.reset_index(drop = True)
            df = Chicago
            return df,f
        else:
            df = Chicago
            return df,f
    elif city == 'washington':
        Washington = pd.read_csv("washington.csv")
        if month !='all':
            f = "yes"
            Washington['Start Time'] = pd.to_datetime(Washington['Start Time'])
            Washington['Month'] = Washington['Start Time'].dt.month_name()
            Washington['Month'] = Washington['Month'].str.lower()
            Washington = Washington[Washington['Month']==month]
            Washington = Washington.reset_index(drop = True)
            Washington['Day'] = Washington['Start Time'].dt.day_name()
            Washington['Day'] = Washington['Day'].str.lower()
            Washington = Washington[Washington['Day']==day]
            Washington = Washington.reset_index(drop = True)
            df = Washington
            return df,f
        else:
            df = Washington
            return df,f
    else:
        New_York = pd.read_csv("new_york_city.csv")
        if month !='all':
            f = "yes"
            New_York['Start Time'] = pd.to_datetime(New_York['Start Time'])
            New_York['Month'] = New_York['Start Time'].dt.month_name()
            New_York['Month'] = New_York['Month'].str.lower()
            New_York = New_York[New_York['Month']==month]
            New_York = New_York.reset_index(drop = True)
            New_York['Day'] = New_York['Start Time'].dt.day_name()
            New_York['Day'] = New_York['Day'].str.lower()
            New_York = New_York[New_York['Day']==day]
            New_York = New_York.reset_index(drop = True)
            df = New_York
            return df,f
        else:
            df = New_York
            return df,f



def filtered_data_time_stats(df):
    """Displays statistics on the most frequent times of travel for Filtered Data."""
    print('-'*40)
    print('\nCalculating The Most Frequent Times of Travel for Filtered Data...\n')
    print('-'*40)
    start_time = time.time()
    # display month name
    print("Month is: ",df['Month'].iloc[0])
    print('-'*40)
    # display the most common day of week
    print("Day of week is: ",df['Day'].iloc[0])
    print('-'*40)
    # display the most common start hour
    df['Hour'] = pd.DatetimeIndex(df['Start Time']).hour
    common_hour = pd.DataFrame(df['Hour'].value_counts())
    common_hour = common_hour.reset_index(drop = False)
    cols = common_hour.columns.values
    cols[0] = "Hour"
    cols[1] = "Day_Counts"
    common_hour.column = cols
    common_hour = common_hour.head(1)
    print("Most common Start Hour: ",common_hour.Hour.iloc[0])
    print('-'*40)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def Understanding_the_Data(df):
    df = df[0:40]
    print("Top Five rows of the Dataset are: ")
    print(df.head())
    print()
    print("The Columns in the Dataset are: ")
    df.columns
    print()
    print("The Details about Dataset are: ")
    df.describe()
    print()
    print("The information about the Dataset is: ")
    df.info()
    print()
    cols = df.columns.values
    print("Value count of Top 40 Rows for each column: ")
    i = 0
    while i<len(cols):
        print('-'*40)
        print("Column Name is: ",cols[i])
        print(df[cols[i]].value_counts())
        print('-'*40)
        i = i+1
    i = 0
    print()
    print('-'*40)
    print("Unique values of Top 40 Rows for each column: ")
    while i<len(cols):
        print('-'*40)
        print("Column Name is: ",cols[i])
        print(df[cols[i]].unique())
        print('-'*40)
        i = i+1



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('-'*40)
    print('\nCalculating The Most Frequent Times of Travel...\n')
    print('-'*40)
    start_time = time.time()
    # display the most common month
    print("Most common Month is: ")
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month_name()
    common_month = pd.DataFrame(df['Month'].value_counts())
    common_month = common_month.reset_index(drop = False)
    cols = common_month.columns.values
    cols[0] = "Month"
    cols[1] = "Month_Counts"
    common_month.column = cols
    common_month = common_month.head(1)
    print(common_month.Month.iloc[0])
    print('-'*40)
    # display the most common day of week
    print("Most common Day of week is: ")
    test = df[df.Month == common_month.Month.iloc[0]]
    test = test.reset_index()
    test['Days'] = test['Start Time'].dt.day_name()
    common_day = pd.DataFrame(test['Days'].value_counts())
    common_day = common_day.reset_index(drop = False)
    cols = common_day.columns.values
    cols[0] = "Day"
    cols[1] = "Day_Counts"
    common_day.column = cols
    common_day = common_day.head(1)
    print(common_day.Day.iloc[0])
    print('-'*40)
    # display the most common start hour
    print("Most common Start Hour: ")
    test = test[test.Days == common_day.Day.iloc[0]]
    test = test.reset_index()
    test['Hour'] = pd.DatetimeIndex(test['Start Time']).hour
    common_hour = pd.DataFrame(test['Hour'].value_counts())
    common_hour = common_hour.reset_index(drop = False)
    cols = common_hour.columns.values
    cols[0] = "Hour"
    cols[1] = "Day_Counts"
    common_hour.column = cols
    common_hour = common_hour.head(1)
    print(common_hour.Hour.iloc[0])
    print('-'*40)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    print('-'*50)
    start_time = time.time()
    # display most commonly used start station
    print("Most commonly used start Station is: ")
    common_Start_Station = pd.DataFrame(df['Start Station'].value_counts())
    common_Start_Station = common_Start_Station.reset_index(drop = False)
    cols = common_Start_Station.columns.values
    cols[0] = "Start Station"
    cols[1] = "Station_Counts"
    common_Start_Station.columns = cols
    common_Start_Station = common_Start_Station.head(1)
    print(common_Start_Station['Start Station'].iloc[0])
    print('-'*50)

    # display most commonly used end station
    print("Most commonly used end station is: ")
    common_End_Station = pd.DataFrame(df['End Station'].value_counts())
    common_End_Station = common_End_Station.reset_index(drop = False)
    cols = common_End_Station.columns.values
    cols[0] = "End Station"
    cols[1] = "Station_Counts"
    common_End_Station.columns = cols
    common_End_Station = common_End_Station.head(1)
    print(common_End_Station['End Station'].iloc[0])
    print('-'*50)

    # display most frequent combination of start station and end station trip
    print("Most Frequent combination of Start station and End station Trip is: ")
    df['start_and_end_Station'] = df['Start Station'] + " " + df['End Station']
    common_start_and_end_Station = pd.DataFrame(df['start_and_end_Station'].value_counts())
    common_start_and_end_Station = common_start_and_end_Station.reset_index(drop = False)
    cols = common_start_and_end_Station.columns.values
    cols[0] = "Common Start_and End Station"
    cols[1] = "Station_Counts"
    common_start_and_end_Station.column = cols
    common_start_and_end_Station = common_start_and_end_Station.head(1)
    print(common_start_and_end_Station['Common Start_and End Station'].iloc[0])
    print('-'*50)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    print('-'*50)
    start_time = time.time()

    # display total travel time
    print("Total Travel Time is: ",df['Trip Duration'].sum()/3600," Hours")
    print('-'*40)

    # display mean travel time
    print("Mean Travel Time is: ",df['Trip Duration'].mean()/3600," Hours")
    print('-'*40)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    print('-'*40)
    start_time = time.time()

    # Display counts of user types
    print("Counts of User Types: ")
    User_Types = pd.DataFrame(df['User Type'].value_counts())
    User_Types = User_Types.reset_index(drop = False)
    cols = User_Types.columns.values
    cols[0] = "User Type"
    cols[1] = "Count"
    User_Types.column = cols
    print(User_Types)
    print('-'*40)
    # Display counts of gender
    print("Counts of Gender: ")
    gender = pd.DataFrame(df['Gender'].value_counts())
    gender = gender.reset_index(drop = False)
    cols = gender.columns.values
    cols[0] = "Gender"
    cols[1] = "Count"
    gender.column = cols
    print(gender)
    print('-'*40)

    # Display earliest, most recent, and most common year of birth
    print("Earliest Year of Birth is: ",min(df['Birth Year']))
    print("Recent Year of Birth is: ",max(df['Birth Year']))
    Birth_Year = pd.DataFrame(df['Birth Year'].value_counts())
    Birth_Year = Birth_Year.reset_index(drop = False)
    cols = Birth_Year.columns.values
    cols[0] = "Most Common Year of Birth"
    cols[1] = "Count"
    Birth_Year.column = cols
    Birth_Year = Birth_Year.head(1)
    print('-'*40)
    print("Most common Year of Birth is: ",int(Birth_Year['Most Common Year of Birth'].iloc[0]))
    print('-'*40)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        h = 5
        city,month,day = get_filters()
        print(city,month,day)
        df,f = load_data(city,month,day)
        if city == 'Chicago':
            Understanding_the_Data(df)
        if f == "yes":
            filtered_data_time_stats(df)
        else:
            time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if city == 'Chicago' or city == 'New_York':
            user_stats(df)
        else:
            print("No Data available for City Washington")
        asking_for_data = input('\nDo you want to see the Past Data? yes or no.\n')
        if asking_for_data.lower() == 'yes':
            while True:
                print(df.head(h))
                restart_dip = input('\nWould you like to See more Data? Enter yes or no.\n')
                h = h+5
                if restart_dip.lower() != 'yes':
                    break
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
