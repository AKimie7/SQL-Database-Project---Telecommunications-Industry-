from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize the VADER sentiment analyzer
sentimentAnalyzer = SentimentIntensityAnalyzer()

# Sample reviews
reviews = [
    'Sprint mobile plan is excellent!',
    'Not as expected from Sprint, very disappointed.',
    'Sprints data service is average, it does the job.'
    'Superb customer support at Sprint, highly recommended.'
    'Sprints network could be better, but it works.'
    'Best decision I made by choosing Sprint!'
    'Terrible experience with Sprint, complete waste of money.'
    'Sprints services are okay, not too impressed.'
    'Good value for the price with Sprint.'
    'Not recommended, Sprint has poor quality in my area.',
    'Im satisfied with my Sprint plan.',
    'Sprints network works perfectly, no complaints.',
    'Not what I expected from Sprint, but its fine.',
    'Outstanding experience with Sprint, exceeded my expectations.',
    'Decent quality services from Sprint, reasonable price.'
    'I regret choosing Sprint, total waste.',
    'Sprints services are not bad, but not great either.',
    'Impressive mobile plans from Sprint, worth every penny.',
    'I love sprint, great network.',
    'Sprints services met my expectations, works well.',
    'Excellent quality network and performance from Sprint.',
    'The worst experience with Sprint, not what I expected.',
    'Sprints network is not the best, but its okay.',
    'Top-notch customer support at Sprint, highly recommended.',
    'Sprints network could be better, not fully satisfied.',
    'Great value for the price with Sprint, happy with it.',
    'Total disappointment with Sprint, do not buy.',
    'Sprints services are exceptional.',
    'Good purchase with Sprint, serves its purpose.',
    'Avoid Sprints network, its terrible.',
    'Very satisfied with my choice of Sprint.',
    'Sprint network is highly durable and reliable.',
    'Not worth the money with Sprint, disappointed.',
    'Reasonable quality for the price from Sprint.',
    'Sprints services exceeded my expectations, fantastic!'
]

# Perform sentiment analysis and categorize sentiment
sentiments = []
for review in reviews:
    sentiment_scores = sentimentAnalyzer.polarity_scores(review)

    # Categorize sentiment
    if sentiment_scores['compound'] > 0.05:
        sentiment_category = "😀 Positive"
    elif sentiment_scores['compound'] < -0.05:
        sentiment_category = "🙁 Negative"
    else:
        sentiment_category = "😐 Neutral"

    # Print scores using emojis to help visualize data when presenting results
    print(f"""'{review}' \n
    🙁 Negative Sentiment: {sentiment_scores['neg']} \n  
    😐 Neutral Sentiment: {sentiment_scores['neu']} \n
    😀 Positive Sentiment: {sentiment_scores['pos']} \n
    ✨ Compound Sentiment: {sentiment_scores['compound']} \n
    Sentiment Category: {sentiment_category}
    --- \n""")

    sentiments.append(sentiment_category)

# Data with tuples
data = [
    (1, 101, 'Sprint mobile plan is excellent!', '2023-03-01', 5),
    (2, 102, 'Not as expected from Sprint, very disappointed.', '2023-03-02', 1),
    (3, 103, 'Sprints data service is average, it does the job.', '2023-03-03', 3),
    (4, 104, 'Superb customer support at Sprint, highly recommended.', '2023-03-04', 5),
    (5, 105, 'Sprints network could be better, but it works.', '2023-03-05', 2),
    (6, 106, 'Best decision I made by choosing Sprint!', '2023-03-06', 5),
    (7, 107, 'Terrible experience with Sprint, complete waste of money.', '2023-03-07', 1),
    (8, 108, 'Sprints services are okay, not too impressed.', '2023-03-08', 3),
    (9, 109, 'Good value for the price with Sprint.', '2023-03-09', 4),
    (10, 110, 'Not recommended, Sprint has poor quality in my area.', '2023-03-10', 1),
    (11, 111, 'Im satisfied with my Sprint plan.', '2023-03-11', 4),
    (12, 112, 'Sprints network works perfectly, no complaints.', '2023-03-12', 5),
    (13, 113, 'Not what I expected from Sprint, but its fine.', '2023-03-13', 3),
    (14, 114, 'Outstanding experience with Sprint, exceeded my expectations.', '2023-03-14', 5),
    (15, 115, 'Decent quality services from Sprint, reasonable price.', '2023-03-15', 4),
    (16, 116, 'I regret choosing Sprint, total waste.', '2023-03-16', 1),
    (17, 117, 'Sprints services are not bad, but not great either.', '2023-03-17', 3),
    (18, 118, 'Impressive mobile plans from Sprint, worth every penny.', '2023-03-18', 5),
    (19, 119, 'I love sprint, great network.', '2023-03-19', 5),
    (20, 120, 'Sprints services met my expectations, works well.', '2023-03-20', 4),
    (21, 121, 'Excellent quality network and performance from Sprint.', '2023-03-21', 5),
    (22, 122, 'The worst experience with Sprint, not what I expected.', '2023-03-22', 1),
    (23, 123, 'Sprints network is not the best, but its okay.', '2023-03-23', 3),
    (24, 124, 'Top-notch customer support at Sprint, highly recommended.', '2023-03-24', 5),
    (25, 125, 'Sprints network could be better, not fully satisfied.', '2023-03-25', 2),
    (26, 126, 'Great value for the price with Sprint, happy with it.', '2023-03-26', 4),
    (27, 127, 'Total disappointment with Sprint, do not buy.', '2023-03-27', 1),
    (28, 128, 'Sprints services are exceptional.', '2023-03-28', 3),
    (29, 129, 'Good purchase with Sprint, serves its purpose.', '2023-03-29', 4),
    (30, 130, 'Avoid Sprints network, its terrible.', '2023-03-30', 1),
    (31, 131, 'Very satisfied with my choice of Sprint.', '2023-03-31', 5),
    (32, 132, 'Sprint network is highly durable and reliable.', '2023-04-01', 5),
    (33, 133, 'Not worth the money with Sprint, disappointed.', '2023-04-02', 2),
    (34, 134, 'Reasonable quality for the price from Sprint.', '2023-04-03', 3),
    (35, 135, 'Sprints services exceeded my expectations, fantastic!', '2023-04-03', 5)
]

# Extract reviews (the second element in each tuple)
reviews = [item[2] for item in data]

# Print the extracted reviews
for review in reviews:
    print(review)

import plotly.express as px
import pandas as pd

# Example DataFrame with provided data
data = {
    "User_ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
                31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
                41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
    "Country": [
        'France', 'Spain', 'Italy', 'USA', 'Italy', 'Germany', 'Canada', 'Germany', 'Brazil', 'Germany',
        'France', 'Germany', 'Germany', 'South Korea', 'Netherlands', 'Greece', 'Portugal', 'Brazil', 'Brazil', 'Russia',
        'Sweden', 'Switzerland', 'United Arab Emirates', 'Kenya', 'New Zealand', 'Austria', 'Ireland', 'Thailand', 'Turkey', 'Egypt',
        'New Zealand', 'Norway', 'Denmark', 'Finland', 'Norway', 'Denmark', 'Norway', 'Poland', 'Indonesia', 'Malaysia', 'Nigeria',
        'Hong Kong', 'Philippines', 'Czech Republic', 'South Africa', 'Canada', 'Iceland', 'Saudi Arabia', 'Ghana', 'United Arab Emirates'
    ],
    "City": [
        'Paris', 'Barcelona', 'Rome', 'New York', 'Rome', 'Berlin', 'Toronto', 'Berlin', 'Rio de Janeiro', 'Berlin',
        'Marseille', 'Berlin', 'Berlin', 'Seoul', 'Amsterdam', 'Athens', 'Lisbon', 'Brasilia', 'Rio de Janeiro', 'Moscow',
        'Stockholm', 'Zurich', 'Dubai', 'Nairobi', 'Auckland', 'Vienna', 'Dublin', 'Bangkok', 'Istanbul', 'Cairo',
        'Wellington', 'Oslo', 'Copenhagen', 'Helsinki', 'Oslo', 'Copenhagen', 'Oslo', 'Warsaw', 'Jakarta', 'Kuala Lumpur', 'Lagos',
        'Hong Kong', 'Manila', 'Prague', 'Johannesburg', 'Vancouver', 'Reykjavik', 'Riyadh', 'Accra', 'Dubai'
    ],
    "Latitude": [
        48.8566, 41.3851, 41.9028, 40.7128, 35.682839, 52.5200, 43.6532, -33.8651, -22.9068, 51.5074,
        43.2965, 39.9042, 19.4326, 37.5665, 52.3667, 37.9838, 38.7223, -34.6118, -22.9068, 55.7558,
        59.3293, 47.3769, 25.276987, -1.286389, -36.848460, 48.2082, 53.349805, 13.7563, 41.0082, 30.0444,
        -41.2865, 59.9139, 55.6761, 60.1699, -33.4489, -33.9249, 50.8503, 52.2297, -6.2088, 3.1390, 6.5244,
        22.3193, 14.5995, 50.0755, -26.2041, 49.2827, 64.1265, 24.7136, 5.6037, 25.276987
    ],
    "Longitude": [
        2.3522, 2.1734, 12.4964, -74.0060, 139.759455, 13.4050, -79.3832, 151.2095, -43.1729, -0.1278,
        5.3698, 116.4074, -99.1332, 126.9780, 4.8945, 23.7275, -9.1393, -58.4173, 103.8198, 37.6176,
        18.0686, 8.5417, 55.296249, 36.817223, 174.763332, 16.3738, -6.26031, 100.5018, 28.9784, 31.2357,
        174.7762, 10.7522, 12.5683, 24.9384, -70.6693, 18.4241, 4.3517, 21.0122, 106.8456, 101.6869, 3.3792, 114.1694,
        120.9842, 14.4378, 28.0473, -123.1207, -21.8174, 46.6753, -0.186964, 55.296249
    ],
    "Roaming_Start": [
        '2023-03-05 09:00:00', '2023-03-10 10:30:00', '2023-03-15 08:45:00', '2023-03-20 11:15:00', '2023-03-25 07:20:00',
        '2023-03-30 08:30:00', '2023-04-05 12:00:00', '2023-04-10 10:00:00', '2023-04-15 14:30:00', '2023-04-20 11:00:00',
        '2023-04-25 09:45:00', '2023-05-02 10:15:00', '2023-05-07 13:00:00', '2023-05-12 11:30:00', '2023-05-18 09:00:00',
        '2023-05-23 07:45:00', '2023-05-28 08:30:00', '2023-06-02 10:00:00', '2023-06-07 09:30:00', '2023-06-12 10:15:00',
        '2023-06-17 07:45:00', '2023-06-22 13:30:00', '2023-10-25 10:15:00', '2023-11-05 09:30:00', '2023-11-10 10:15:00',
        '2023-06-27 12:15:00', '2023-07-02 11:30:00', '2023-07-07 09:00:00', '2023-07-12 07:45:00', '2023-07-17 14:30:00',
        '2023-07-22 10:15:00', '2023-07-27 11:00:00', '2023-08-01 12:00:00', '2023-08-06 08:45:00', '2023-08-11 09:30:00',
        '2023-08-16 08:15:00', '2023-08-21 10:00:00', '2023-08-26 09:45:00', '2023-08-31 07:30:00', '2023-09-05 12:00:00',
        '2023-09-10 11:30:00', '2023-09-15 10:15:00', '2023-09-20 08:45:00', '2023-09-25 09:30:00', '2023-09-30 08:15:00',
        '2023-10-05 10:00:00', '2023-10-10 07:45:00', '2023-10-15 14:30:00', '2023-10-20 11:30:00', '2023-10-25 10:15:00'
    ],
    "Roaming_End": [
        '2023-03-05 18:00:00', '2023-03-10 20:00:00', '2023-03-15 19:30:00', '2023-03-20 21:30:00', '2023-03-25 17:45:00',
        '2023-03-30 19:15:00', '2023-04-05 22:15:00', '2023-04-10 21:00:00', '2023-04-15 23:00:00', '2023-04-20 21:45:00',
        '2023-04-25 20:30:00', '2023-05-02 22:30:00', '2023-05-07 23:30:00', '2023-05-12 20:15:00', '2023-05-18 18:30:00',
        '2023-05-23 17:00:00', '2023-05-28 19:45:00', '2023-06-02 21:15:00', '2023-06-07 19:45:00', '2023-06-12 21:30:00',
        '2023-06-17 16:30:00', '2023-06-22 23:45:00', '2023-10-25 21:30:00', '2023-11-05 19:45:00', '2023-11-10 21:30:00',
        '2023-06-27 22:30:00', '2023-07-02 20:45:00', '2023-07-07 19:15:00', '2023-07-12 16:30:00', '2023-07-17 23:45:00',
        '2023-07-22 20:30:00', '2023-07-27 21:15:00', '2023-08-01 22:15:00', '2023-08-06 19:00:00', '2023-08-11 20:45:00',
        '2023-08-16 17:30:00', '2023-08-21 21:15:00', '2023-08-26 19:00:00', '2023-08-31 16:45:00', '2023-09-05 22:15:00',
        '2023-09-10 20:45:00', '2023-09-15 21:30:00', '2023-09-20 19:00:00', '2023-09-25 19:45:00', '2023-09-30 17:30:00',
        '2023-10-05 20:15:00', '2023-10-10 16:30:00', '2023-10-15 23:45:00', '2023-10-20 20:45:00', '2023-10-25 21:30:00'
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a map figure using Plotly Express
fig = px.scatter_geo(
    df,
    lat="Latitude",
    lon="Longitude",
    color="Country",
    hover_name="City",
    size_max=30,
    animation_frame="Roaming_Start",
    projection="natural earth"
)

# Update the map layout
fig.update_geos(
    resolution=50,
    showcoastlines=True,
    coastlinecolor="RebeccaPurple",
    showland=True,
    landcolor="black",
    showocean=True,
    oceancolor="LightBlue",
    showrivers=True,
    rivercolor="black"
)

# Update the figure layout
fig.update_layout(
    title="User Roaming Locations",
    geo=dict(
        showframe=False,
        showcoastlines=False,
    ),
)

# Show the map
fig.show()


#attempt 2
import plotly.express as px
import pandas as pd

data = {
    'User_ID': list(range(1, 6)),
    'Data_Usage': [500, 300, 800, 400, 600],
    'Data_Usage_Details': ['Browsing', 'Texting', 'Video Calls', 'Email', 'Social Media']
}

df = pd.DataFrame(data)

fig = px.pie(df, values='Data_Usage', names='Data_Usage_Details',
             title='Data Usage Details Distribution')

fig.show()
