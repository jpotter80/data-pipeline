
# IMDB Movie Data Analysis

## Initial Data Exploration

### Dataset Overview
- The dataset contains information about 1000 movies from IMDB.
- Key features include: rank, year, duration, age_limit, rating, number_of_ratings, Metascore, description, and name.

### Data Quality
- The Metascore column has 158 null values, which may require attention in future analyses.
- Other columns appear to be complete with no missing values.

## Visualizations and Insights

### Distribution of Movie Ratings
![Distribution of Movie Ratings](rating_distribution.png)

- Ratings range from approximately 7.5 to 9.3.
- The distribution is left-skewed, with most movies rated between 7.75 and 8.25.
- There's a peak around 7.75-8.00, suggesting this is the most common rating range.
- Very few movies have ratings above 9.0, indicating that extremely high ratings are rare.

### Movie Ratings by Year
![Movie Ratings by Year](ratings_by_year.png)

- The dataset includes movies from around 1920 to 2023.
- There's a general increase in the number of rated movies over time.
- Ratings seem to be more spread out in recent years, ranging from about 7.5 to 9.3.
- No strong correlation between year and rating is immediately apparent.
- The highest-rated movies (above 9.0) appear across various years.

## Next Steps

1. Investigate the relationship between movie duration and rating.
2. Analyze the distribution of genres and their impact on ratings.
3. Examine the correlation between the number of ratings and the overall rating.
4. Look into patterns in the Metascore and how it relates to the IMDB rating.
5. Perform statistical tests to confirm or refute observed trends.
6. Create a predictive model for movie ratings based on available features.

## Questions for Further Investigation

1. Is there a significant difference in ratings between movies of different age limits?
2. How has the average movie duration changed over the years, and does it correlate with ratings?
3. Are there any notable differences in ratings or other features for movies with and without Metascores?
4. Can we identify any patterns in the movie descriptions that correlate with higher ratings?

This analysis summary will be updated as we progress through our investigation.
