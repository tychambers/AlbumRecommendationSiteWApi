import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer


def find_recommendations(album):
    df = pd.read_csv('data/Top5000Albums.csv')

    new_rows = []
    for index, row in df.iterrows():
        row['Genres'] = row['Genres'].split(',')
        row['Genres'] = [x.replace(' ', '') for x in row['Genres']]
        row['Genres'] = [x.lower() for x in row['Genres']]
        new_rows.append(row)

    df = pd.DataFrame(new_rows)

    df.dropna(subset=['Descriptors'], inplace=True)

    new_rows = []
    for index, row in df.iterrows():
        row['Descriptors'] = row['Descriptors'].split(',')
        row['Descriptors'] = [x.replace(' ', '') for x in row['Descriptors']]
        row['Descriptors'] = [x.lower() for x in row['Descriptors']]
        new_rows.append(row)

    df = pd.DataFrame(new_rows)

    new_rows = []
    for index, row in df.iterrows():
        row['Artist Name'] = row['Artist Name'].replace(" ", "").lower()
        new_rows.append(row)

    df = pd.DataFrame(new_rows)

    df.drop('Number of Reviews', axis=1, inplace=True)
    df.drop('Number of Ratings', axis=1, inplace=True)
    df.drop('Average Rating', axis=1, inplace=True)
    df.drop('Ranking', axis=1, inplace=True)
    df.drop('Release Date', axis=1, inplace=True)

    df.set_index('Album', inplace=True)

    df['descriptor_words'] = ''
    columns = df.columns
    new_rows = []
    for index, row in df.iterrows():
        words = ''
        for col in columns:
            if col != 'Artist Name':
                words = words + ' ' + ' '.join(row[col])
            else:
                words = words + ' ' + row[col]+ ' '
        row['descriptor_words'] = words
        new_rows.append(row)

    df = pd.DataFrame(new_rows)

    df.drop('Artist Name', axis=1, inplace=True)
    df.drop('Genres', axis=1, inplace=True)
    df.drop('Descriptors', axis=1, inplace=True)

    # instantiating and generating the count matrix
    count = CountVectorizer()
    count_matrix = count.fit_transform(df['descriptor_words'])

    # generating the cosine similarity matrix
    # compares with other entries from the same data
    cosine_sim = cosine_similarity(count_matrix, count_matrix)

    # creating a series for the movie titles so they are associated to an ordered numerical
    # list I will use later to match the indexes
    indices = pd.Series(df.index)

    # function that takes in the album title as input and returns the top 10 recommended albums
    def recommendations(title, cosine_sim1=cosine_sim):
        recommended_albums = []

        # getting the index of the movie that matches the title
        idx = indices[indices == title].index[0]

        # creating a Series with the similarity scores in descending order
        score_series = pd.Series(cosine_sim1[idx]).sort_values(ascending=False)

        # getting the indexes of the 10 most similiar movies
        top_10_indexes = list(score_series.iloc[1:11].index)
        # print(top_10_indexes)

        for i in top_10_indexes:
            recommended_albums.append(list(df.index)[i])

        return recommended_albums

    # input the album name below to get 10 albums that are similar
    albums = recommendations(album)
    return albums