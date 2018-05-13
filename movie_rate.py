
# coding: utf-8

# In[9]:


###             MOVIE RATING              ####


import pandas as pd
m_rate=pd.read_csv('data.tsv',delimiter='\t')
#considering only first 5000 movies in the dataset
m_rate=m_rate.iloc[0:5000,:]
#finding any null value present in the dataset or not
m_rate.info() #It showed dataset does not have any  null value
#calculating average rating of all movies from m_rate dataset
c=m_rate['averageRating'].mean()
#calculating number votes required for a movie to include in the chart 
m=m_rate['numVotes'].quantile(0.9)
print(m)
# copies those movies whose number votes >=m
# copy() method to ensure that the new q_movies DataFrame created is independent of your original metadata DataFrame. In other words, any changes made to the q_movies DataFrame does not affect the metadata.
q_movies = m_rate.copy().loc[m_rate['numVotes'] >= m]

# define  weight rating function to calculate weight rate
def weight_movie(x=q_movies,m=m,C=c):
    # Number of votes for particular movie
    v=x['numVotes']
    # Average ratings of that movie
    R=x['averageRating']
    return ((v/m+v)*R+(m/m+v)*C)

#Apply weighted function for each movie to calculate weighted score
q_movies['score']=q_movies.apply(weight_movie,axis=1)
q_movies = q_movies.sort_values('score', ascending=False)
q_movies.to_csv("movie_score.csv",sep=",")
q_movies.head(50)



 


# In[20]:




