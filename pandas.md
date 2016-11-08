
# Pandas

How to creates a dates ranges in Pandas?

How to creates a dates DataFrame in Pandas?

    # dates
    dates = pd.date_range('2010-04-21', '2015-04-21')

    # create a data frame of dates as index column
    df = pd.DataFrame(index=dates)



How to read a CSV File?

How to read CSV file with specific index columns?

How to parse dates in a CSV File?

How to read only required columns from CSV File?

How to specific the NULL values notation in CSV File?


    # read csv file
    df_spy = pd.read_csv(
            'data/%s.csv' %s 'SPY',
            index_col='Dates', # specific index
            parse_dates=True, # identify Date columns as DateTime values
            usecols=['Date', 'Adj Close'], # cols we need
            na_values=['nan'] # csv has NAN as NULL values, so tell CSV ahead.
                )


How to join two data frames?

    # join data frames - default LEFT join
    df = df1.join(df_spy)


How to rename a data frame column?

    df.rename(columns={'Adj Close':'SPY'})


How to drop na values in a data frame?

    df.dropna()


How to do a inner join of data frames?

    df.join(df_)




How to plot a DataFrame?

How to set plot fontsize?

How to set plot label?

How to set x label and y label?

    ax = df.plot(title='Stock Prices', fontsize=2)
    ax.set_xlabel('Date')
    ax.set_ylabel('Prices')
    plt.show()


How take a slice of data?

    df_new = df.ix[start_index:end_index]

## Hungry
Hungry for more? [link](https://inlovewithcode.wordpress.com/pandas/)
