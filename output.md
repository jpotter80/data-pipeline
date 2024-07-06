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

 data-pipeline  poetry run python main.py
Database subscriptions created successfully.
Table subscriptions created successfully.
Data inserted into subscriptions successfully.
Analysis for subscriptions.csv:
1. Summary of Data:
- The data involves information about various YouTube channels. Each channel has three attributes: 'Channel Id', 'Channel Url', 'Channel Title'. All of these attributes are objects or strings.
- The 'Channel Id' attribute represents a unique identifier for each YouTube channel. The 'Channel Url' attribute is the web address that leads to the YouTube channel. The 'Channel Title' attribute represents the name of the YouTube channel.
- The dataset comprises 138 rows and each of these rows represents one unique YouTube channel.
- It appears that there are no null or missing values in this dataset as per the Null Counts for each of the columns.

2. Potential Data Quality Issues:
- One potential issue with this dataset could be inconsistency in the 'Channel Title' attribute. For instance, the same channel might have been entered differently – with misspellings, extra spaces, or different cases.
- Duplicate entries might exist. Even though 'Channel Id' is supposed to be unique, there are chances of duplicate entries in the data.
- Although there seems to be no missing values, there could be cases where a string is empty or a placeholder value is used, which could affect the quality of data.

3. Suggestions for Data Cleaning and Normalization:
- For the 'Channel Title' attribute, we can normalize the values by converting all of them to a similar case, removing any leading and trailing spaces, and correcting misspellings.
- Check for duplicate entries in the dataset. As 'Channel Id' should ideally be unique for each channel, if any duplicates are found, those entries should be removed to maintain data integrity.
- Check for any placeholder values or empty strings, and depending upon the business requirement, choose to either fill these in using appropriate methods (perhaps using manual look-up or any other method) or discard them.
- For cleaner analysis, validation of 'Channel Url' might be necessary to confirm that the URL correctly leads to the respective 'Channel Id'.

SQL Transformations for subscriptions.csv:
In compliance with your request, here are SQL statements that could be used to handle those data cleaning tasks. Please note that these SQL statements assume that your database is named 'youtube_db' and the table is named 'channels':

1. Handling Null Values
Since there are no null values according to your data description, but there could be empty strings or placeholder values, you can replace these with a NULL:

```sql
UPDATE youtube_db.channels
SET Channel_Id = NULLIF(Channel_Id, ''),
    Channel_Url = NULLIF(Channel_Url, ''),
    Channel_Title = NULLIF(Channel_Title, '');
```

2. Data Type Conversions
Since all your columns are of string type (varchar), there's no immediate need for type conversion. But for example if you needed to convert them into a TEXT datatype:

```sql
ALTER TABLE youtube_db.channels
ALTER COLUMN Channel_Id TYPE TEXT,
ALTER COLUMN Channel_Url TYPE TEXT,
ALTER COLUMN Channel_Title TYPE TEXT;
```

Please note that data type conversions very much depend on your specific use case, and you would only typically change the data type if your current data type isn't correctly suited or is inefficient for the data it is holding.

3. Data Transformations

A. Convert 'Channel Title' to similar case and remove trailing/leading white space:

```sql
UPDATE youtube_db.channels
SET Channel_Title = TRIM(LOWER(Channel_Title));
```

B. Remove duplicate entries based on 'Channel Id':

```sql
DELETE FROM youtube_db.channels
WHERE ctid NOT IN (
  SELECT MAX(ctid)
  FROM youtube_db.channels
  GROUP BY Channel_Id);
```

C. Check & Handle placeholder values (Assuming `_unknown_` as the placeholder value):

```sql
UPDATE youtube_db.channels
SET Channel_Id = NULLIF(Channel_Id, '_unknown_'),
    Channel_Url = NULLIF(Channel_Url, '_unknown_'),
    Channel_Title = NULLIF(Channel_Title, '_unknown_');
```

These statements should help you clean your data and make it more consistent and easier to work with. Remember to always backup your data before performing such operations to protect against potential data loss.
