 data-pipeline  poetry run python main.py
Database imdb already exists.
Table imdb already exists.
Table imdb already contains data. Skipping insertion.
Analysis for imdb.csv:
1. Summary of the Data:
    The data contains information on 1000 films. Each entry includes the film's rank, release year, duration, age limit, rating, number of ratings, Metascore, brief description, and name. All films are ranked, with 1 indicating the highest rank. The years in the data cover a broad range of release dates. The Duration is given in a string format with hours and minutes. The age limit, some of which are null, indicates the age appropriateness of the films. Ratings and Metascores, some of which are also null, provide a quality indication. The number of ratings is enclosed in parentheses and presented as a string. Each entry includes a description and the name of the film.

2. Potential Data Quality Issues:
   - There are null values in the 'age_limit' and 'Metascore' columns, which suggests that not all films have these details recorded.
   - The 'duration' is in a string format, which makes performing numerical operations on it challenging.
   - The 'numberof_ratings' column is also in a string format, with numbers enclosed in parentheses.

3. Suggestions for Data Cleaning and Normalization:
   - Handling null values: Depending on the specific requirements, we could either replace null 'age_limit' values with a placeholder string like 'Not Specified' or we could drop these rows from the dataset. The missing Metascores could be replaced with the average of the column, or they could also be dropped depending on the specific use case.
   - The 'duration' of the movies can be converted to a numerical format like duration in minutes. This would involve processing the string to extract the hours and minutes, converting them to integers, and then calculating the total duration in minutes.
   - The 'numberof_ratings' field values are enclosed in brackets and expressed in Millions. We could remove the parentheses and 'M' and convert the column to numeric for easier data computation and analysis.
   - Finally, ensuring consistency across all entries would make the process of analysis smoother and more accurate - this may include unifying the text casing, removing unnecessary leading/trailing whitespaces, etc.

SQL Transformations for imdb.csv:
Certainly. Here are the SQL statements that could be used to address these issues:

Assume the table name is `Movies` and the columns are `rank`, `release_year`, `duration`, `age_limit`, `rating`, `numberof_ratings`, `Metascore`, `description`, `name`.

1. Handling null values:

   a) Replace null values in 'age_limit' with 'Not Specified':
   ```sql
   UPDATE Movies
   SET age_limit = COALESCE(age_limit, 'Not Specified')
   ```

   b) Replace null Metascores with the average Metascore:
   ```sql
   UPDATE Movies
   SET Metascore = COALESCE(Metascore, (SELECT AVG(Metascore) FROM Movies WHERE Metascore IS NOT NULL))
   ```

2. Data type conversions and transformations:

   a) Convert 'duration' to minutes (assuming format 'xh ym'):
   ```sql
   UPDATE Movies
   SET duration = SUBSTRING_INDEX(duration, 'h', 1) * 60 + SUBSTRING_INDEX(SUBSTRING_INDEX(duration, ' ', -2), 'm', 1)
   ```

   b) Convert 'numberof_ratings' to numeric, removing the parentheses and 'M':
   ```sql
   UPDATE Movies
   SET numberof_ratings = REPLACE(REPLACE(REPLACE(numberof_ratings, '(', ''), ')', ''), 'M', '')
   ```

3. Further data cleaning:

   a) Trim leading and trailing whitespace from 'name':
   ```sql
   UPDATE Movies
   SET name = TRIM(name)
   ```

   b) Transform all movie names to lower case for text consistency:
   ```sql
   UPDATE Movies
   SET name = LOWER(name)
   ```

Remember that the actual SQL code may vary depending on your specific SQL dialect and how your data is constructed (especially for the 'duration' and 'numberof_ratings' conversions). These examples are based on MySQL.
