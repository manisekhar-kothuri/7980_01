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
	

# Bonus Questions

#Q1  Generate a report that tracks the various Genere combinations for each type year on year. The result data frame should contain type, Genere_combo, year, avg_rating, min_rating, max_rating, total_run_time_mins
def imdb(df):
    df1=df.groupby(['title_year','color','genres'],sort="TRUE")['imdb_score'].agg([min,max,'mean'])
    df2=df.groupby(['title_year','color','genres'],sort="TRUE")['duration'].sum().rename(columns=['total_run_time_mins '])
    df1['total_run_time_mins']=df2[3]
    return df1

#Q2  Is there a realation between the length of a movie title and the ratings ? Generate a report that captures the trend of the number of letters in movies titles over years. We expect a cross tab between the year of the video release and the quantile that length fall under. The results should contain year, min_length, max_length, num_videos_less_than25Percentile, num_videos_25_50Percentile , num_videos_50_75Percentile, num_videos_greaterthan75Precentile
def quan(df,num):
    df['title_length']=df['movie_title'].apply(len)
    df["percentile"]=pd.qcut(df["title_length"],num,labels=False)
    df2=df.pivot_table(index="title_year",columns=['percentile'],values=["title_length"],aggfunc={"title_length":'count'},fill_value=0)
    df2[["min","max"]]=df.groupby("title_year").agg({"title_length":[min,max]})
    return df2

#Q3 In diamonds data set Using the volumne calculated above, create bins that have equal population within them. Generate a report that contains cross tab between bins and cut. Represent the number under each cell as a percentage of total. 
import sys
df1=pd.read_csv('diamonds.csv')
def cross(df1):
    df1['z'].fillna(0,inplace=True)
    for i in range(len(df1)):
        if df1['z'][i]=="None":
            df1['z'][i]=0
    df1['z']=df1['z'].astype(float)
    df1['volume']=8
    df1.loc[df1['depth'] > 60, 'volume'] = (df1['x']*df1['y']*df1['z'])#for calculating volume
    return pd.crosstab(pd.qcut(df1["volume"], 5),df1["cut"],normalize=True)


#Q4  Generate a report that tracks the Avg. imdb rating quarter on quarter, in the last 10 years, for movies that are top performing. You can take the top 10% grossing movies every quarter. Add the number of top performing movies under each genere in the report as well.
def ques4(df,df2):
    import math  
    df['url']=df['movie_imdb_link'].apply(lambda x:x.split('?')[0])
    k=pd.DataFrame()
    hh=df['title_year'].unique()
    for x in hh:
        ll1=df[(df['title_year']==x)]
        lr=ll1.sort_values(by=['gross'], ascending=False)
        g=lr.head(math.ceil(len(ll1)*0.10))
        k=k.append(g)
    q=pd.merge(k,df2,on="url",how="left")
    genres=q.loc[:,'Action':'Western'].columns.tolist()
    m=pd.DataFrame()
    m=q.groupby("title_year")[genres].sum()
    m['Avg_imdb']=q.groupby("title_year")["imdb_score"].mean()
    m['count_imdb']=q.groupby("title_year")["imdb_score"].count()
    return m

df=pd.read_csv("movie_metadata.csv",escapechar="\\")
ques4(df,df2)

#Q5 Bucket the movies into deciles using the duration. Generate the report that tracks various features like nomiations, wins, count, top 3 geners in each decile.
def summ(df2):
    df2=df2.dropna()
    df2["decile"]=pd.qcut(df2["duration"],10,labels=False)
    x=df2.groupby("decile")[["nrOfNominations","nrOfWins"]].sum()
    x["count"]=df2.groupby("decile")["year"].count()
    y=df2.iloc[:,np.r_[8,17:45]]#data
    z=y.groupby("decile")[y.columns.tolist()[1:28]].sum()
    z=z.transpose()
    e=pd.DataFrame(z.apply(lambda x: x.nlargest(3).index,axis=0).transpose(),)
    e.columns=["first","second","third"]
    x["top genres"]=e["first"]+","+e["second"]+","+e["third"]
    return x

#Q16 is in notebook