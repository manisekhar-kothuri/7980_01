# import pandas, numpy
# Create the required data frames by reading in the files

# Q1 Find least sales amount for each item
# has been solved as an example
def least_sales(df):
    # write code to return pandas dataframe
	ls = df.groupby(["Item"])["Sale_amt"].min().reset_index()
    return ls

# Q2 compute total sales at each year X region
def sales_year_region(df):
    # write code to return pandas dataframe
    df['Order'] = pd.DatetimeIndex(df['OrderDate']).year
    df1=df.groupby(['Order','Region','Item'])
    return df1.sum()

# Q3 append column with no of days difference from present date to each order date
def days_diff(df):
    # write code to return pandas dataframe
    df['days_diff']='2019-12-03'
    df['days_diff']= pd.to_datetime(df['days_diff']) 
    df['days_diff']= df['days_diff']-df['OrderDate']
    return df

# Q4 get dataframe with manager as first column and  salesman under them as lists in rows in second column.
def mgr_slsmn(df):
    # write code to return pandas dataframe
        df1=df.groupby('Manager')['SalesMan'].apply(set).reset_index(name='list_of_salesmen')

    return df1

# Q5 For all regions find number of salesman and number of units
def slsmn_units(df):
    # write code to return pandas dataframe
    df=df1.groupby('Region')['SalesMan'].apply(set).reset_index(name='list_of_salesmen')
    df['salesman_count']=df['list_of_salesmen'].str.len()
    df3=a.groupby('Region')['Sale_amt'].apply(sum).reset_index(name='sum')
    df['total_sales']=df3['sum']
    return df

# Q6 Find total sales as percentage for each manager
def sales_pct(df):
    # write code to return pandas dataframe
    df6=df.groupby('Manager')['Sale_amt'].apply(sum).reset_index(name='percent_sales')
    s=df6['percent_sales'].sum()
    df6['percent_sales']=(df6['percent_sales']/s)*100 
    return df6

# Q7 get imdb rating for fifth movie of dataframe
def fifth_movie(df):
	# write code here
	return df['imdbRating'][4]

# Q8 return titles of movies with shortest and longest run time
def movies(df):
	# write code here
	return (df[df['duration']==df['duration'].min()]['title'],df[df['duration']==df['duration'].max()]['title'])

# Q9 sort by two columns - release_date (earliest) and Imdb rating(highest to lowest)
def sort_df(df):
	# write code here
	df.sort_values(['year', 'imdbRating'], ascending=[True, False])
        return df

# Q10 subset revenue more than 2 million and spent less than 1 million & duration between 30 mintues to 180 minutes
def subset_df(df):
	# write code here
	df[['duration']] = df[['duration']].apply(pd.to_numeric) 
        df1= df[(df['duration'] > 1800) & (df['duration'] < 10800) & (df['gross']>2000000) & (df['gross']<1000000)]
        return df1

# Q11 count the duplicate rows of diamonds DataFrame.
def dupl_rows(df):
	# write code here
	df = (df.fillna('').groupby(df.columns.tolist()).apply(len)/
      .rename('count')/
      .reset_index()/
      .replace('',np.nan)/
      .sort_values(by = ['count'], ascending = False))
	return df

# Q12 droping those rows where any value in a row is missing in carat and cut columns
def drop_row(df):
	# write code here
	df.dropna(subset=['carat','cut'])
	return df

# Q13 subset only numeric columns
def sub_numeric(df):
	# write code here
	df1=df._get_numeric_data()
	return df1

# Q14 compute volume as (x*y*z) when depth > 60 else 8
def volume(df):
	# write code here
	df['volume']=8
	df.loc[df['depth'] > 60, 'volume'] = (df['x']*df['y'])*df['z']
	return df

# Q15 impute missing price values with mean
def impute(df):
	# write code here
	df.fillna(df.mean())
	return df
	
