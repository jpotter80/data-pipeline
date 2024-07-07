 data-pipeline  poetry run python main.py
2024-07-06 20:43:00,275 - INFO - Database mlb_bat_tracking already exists.
2024-07-06 20:43:00,275 - INFO - Using database: mlb_bat_tracking
2024-07-06 20:43:00,275 - INFO - Processing file: dataset/mlb_bat_tracking.csv
2024-07-06 20:43:00,285 - INFO - Profiling report for mlb_bat_tracking.csv:
Data Profiling Report
=====================

Column: id
  Inferred Type: int64
  Total Count: 214
  Null Count: 0
  Null Percentage: 0.00%
  Unique Values: 214
  Minimum: 453568
  Maximum: 701538
  Mean: 642370.39
  Sample Values: 519317, 665833, 656941, 592450, 666176

Column: name
  Inferred Type: object
  Total Count: 214
  Null Count: 0
  Null Percentage: 0.00%
  Unique Values: 214
  Sample Values: Stanton, Giancarlo, Cruz, Oneil, Schwarber, Kyle, Judge, Aaron, Adell, Jo

Column: swings_competitive
  Inferred Type: int64
  Total Count: 214
  Null Count: 0
  Null Percentage: 0.00%
  Unique Values: 154
  Minimum: 335
  Maximum: 675
  Mean: 462.38
  Sample Values: 424, 418, 468, 538, 473

Column: percent_swings_competitive
  Inferred Type: float64
  Total Count: 214
  Null Count: 0
  Null Percentage: 0.00%
  Unique Values: 199
  Minimum: 0.8981233243967828
  Maximum: 0.9170984455958548
  Mean: 0.90
  Sample Values: 0.9157667386609072, 0.9126637554585152, 0.9017341040462428, 0.9072512647554806, 0.9061302681992336

Column: contact
  Inferred Type: int64
  Total Count: 214
  Null Count: 0
  Null Percentage: 0.00%
  Unique Values: 147
  Minimum: 235
  Maximum: 510
  Mean: 356.83
  Sample Values: 294, 289, 327, 377, 329

Column: avg_bat_speed
  Inferred Type: float64
  Total Count: 214
  Null Count: 0
  Null Percentage: 0.00%
  Unique Values: 214
  Minimum: 62.88440574509802
  Maximum: 80.73858412735842
  Mean: 71.65
  Sample Values: 80.73858412735842, 78.09121547846892, 77.13645959401713, 76.83061236059484, 76.71445790697672

Column: hard_swing_rate
  Inferred Type: float64
  Total Count: 214
  Null Count: 0
  Null Percentage: 0.00%
  Unique Values: 214
  Minimum: 0.0
  Maximum: 0.981132075471698
  Mean: 0.24
  Sample Values: 0.981132075471698, 0.7464114832535885, 0.75, 0.724907063197026, 0.6596194503171247

Column: squared_up_per_bat_contact
  Inferred Type: float64
  Total Count: 214
  Null Count: 0
  Null Percentage: 0.00%
  Unique Values: 212
  Minimum: 0.2133757961783439
  Maximum: 0.4799154334038055
  Mean: 0.33
  Sample Values: 0.2993197278911564, 0.3356401384083045, 0.3394495412844037, 0.3687002652519894, 0.2522796352583586

Column: squared_up_per_swing
  Inferred Type: float64
  Total Count: 214
  Null Count: 0
  Null Percentage: 0.00%
  Unique Values: 210
  Minimum: 0.1506849315068493
  Maximum: 0.4450980392156862
  Mean: 0.26
  Sample Values: 0.2075471698113207, 0.2320574162679425, 0.2371794871794871, 0.258364312267658, 0.175475687103594

Column: blast_per_bat_contact
  Inferred Type: float64
  Total Count: 214
  Null Count: 0
  Null Percentage: 0.00%
  Unique Values: 214
  Minimum: 0.0263157894736842
  Maximum: 0.2811671087533156
  Mean: 0.14
  Sample Values: 0.272108843537415, 0.2352941176470588, 0.2262996941896024, 0.2811671087533156, 0.1519756838905775

Column: blast_per_swing
  Inferred Type: float64
  Total Count: 214
  Null Count: 0
  Null Percentage: 0.00%
  Unique Values: 213
  Minimum: 0.0215633423180593
  Maximum: 0.1987577639751552
  Mean: 0.11
  Sample Values: 0.1886792452830188, 0.1626794258373205, 0.1581196581196581, 0.1970260223048327, 0.1057082452431289

Column: swing_length
  Inferred Type: float64
  Total Count: 214
  Null Count: 0
  Null Percentage: 0.00%
  Unique Values: 214
  Minimum: 5.9343494313725484
  Maximum: 8.399277311320754
  Mean: 7.34
  Sample Values: 8.399277311320754, 7.6323877033492815, 7.820547173447538, 8.185900334572489, 7.663747716701902

Column: swords
  Inferred Type: int64
  Total Count: 214
  Null Count: 0
  Null Percentage: 0.00%
  Unique Values: 23
  Minimum: 0
  Maximum: 25
  Mean: 7.73
  Sample Values: 4, 3, 18, 4, 9

Column: batter_run_value
  Inferred Type: float64
  Total Count: 214
  Null Count: 0
  Null Percentage: 0.00%
  Unique Values: 214
  Minimum: -29.89795032149796
  Maximum: 31.956811281507186
  Mean: -6.72
  Sample Values: 5.401630692218886, -10.679299973258162, -4.1821912476887535, 31.956811281507186, -12.279310068725502

Column: whiffs
  Inferred Type: int64
  Total Count: 214
  Null Count: 0
  Null Percentage: 0.00%
  Unique Values: 108
  Minimum: 37
  Maximum: 216
  Mean: 105.55
  Sample Values: 130, 129, 141, 161, 144

Column: whiff_per_swing
  Inferred Type: float64
  Total Count: 214
  Null Count: 0
  Null Percentage: 0.00%
  Unique Values: 212
  Minimum: 0.0725490196078431
  Maximum: 0.3756218905472637
  Mean: 0.23
  Sample Values: 0.3066037735849056, 0.3086124401913875, 0.3012820512820512, 0.2992565055762082, 0.3044397463002114

Column: batted_ball_events
  Inferred Type: int64
  Total Count: 214
  Null Count: 0
  Null Percentage: 0.00%
  Unique Values: 103
  Minimum: 105
  Maximum: 266
  Mean: 177.60
  Sample Values: 151, 146, 169, 186, 147

Column: batted_ball_event_per_swing
  Inferred Type: float64
  Total Count: 214
  Null Count: 0
  Null Percentage: 0.00%
  Unique Values: 211
  Minimum: 0.2397260273972602
  Maximum: 0.5373134328358209
  Mean: 0.39
  Sample Values: 0.3561320754716981, 0.3492822966507177, 0.3611111111111111, 0.345724907063197, 0.3107822410147992


2024-07-06 20:43:00,286 - INFO - Successfully loaded mlb_bat_tracking.csv
2024-07-06 20:43:00,288 - INFO - Creating table mlb_bat_tracking in database mlb_bat_tracking
2024-07-06 20:43:00,310 - INFO - Table mlb_bat_tracking created successfully in database mlb_bat_tracking.
2024-07-06 20:43:00,332 - INFO - Table mlb_bat_tracking already contains data. Skipping insertion.
2024-07-06 20:43:25,090 - INFO - HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
2024-07-06 20:43:25,096 - INFO - Interaction logged to structure_analysis_1720313005.095377.log
2024-07-06 20:43:25,096 - INFO - Analysis for mlb_bat_tracking.csv:
Thank you for providing this detailed CSV structure. I'll analyze it and provide a summary, potential data quality issues, and suggestions for data cleaning and normalization.

1. Summary of the data:

The dataset appears to be related to baseball batting statistics, containing 214 records with 18 columns. The data includes various metrics such as player ID, name, swing statistics, contact rates, batting speed, and performance indicators.

Key points:
- The dataset contains both categorical (e.g., 'name') and numerical columns.
- Most columns are numerical, with a mix of integer and floating-point values.
- The data seems to focus on individual player performance across various batting metrics.

2. Potential data quality issues:

a) Missing values: The data profile shows no null values, which is good. However, it's worth double-checking if there are any placeholders for missing data (e.g., -1, 999, etc.) that weren't detected as nulls.

b) Outliers: Some columns show a wide range of values, which could indicate potential outliers. For example:
   - 'batter_run_value' ranges from -29.89 to 31.95
   - 'whiffs' ranges from 37 to 216

c) Inconsistent scaling: Different metrics use different scales, which could affect analysis and modeling.

d) Possible duplicate information: Some columns might be providing similar information, such as 'whiffs' and 'whiff_per_swing'.

e) Data type inconsistencies: Some columns that should be percentages (e.g., 'percent_swings_competitive') are stored as floats between 0 and 1, while others (e.g., 'hard_swing_rate') use the same range but represent a different concept.

3. Suggestions for data cleaning and normalization:

a) Handle potential outliers:
   - Investigate extreme values in columns like 'batter_run_value' and 'whiffs' to ensure they are valid data points.
   - Consider using methods like z-score or IQR to identify and handle outliers if necessary.

b) Normalize numerical columns:
   - Apply min-max scaling or standardization to bring all numerical columns to a similar scale.
   - This is particularly important for columns with widely different ranges, like 'avg_bat_speed' and 'batter_run_value'.

c) Convert percentages:
   - For consistency, convert all percentage-based columns to a 0-100 scale instead of 0-1.
   - Affected columns: 'percent_swings_competitive', 'hard_swing_rate', 'whiff_per_swing', etc.

d) Feature engineering:
   - Consider creating new features that might be more informative, such as ratios between existing metrics.
   - Evaluate the necessity of keeping both absolute and per-swing metrics; you might be able to derive one from the other.

e) Data type conversions:
   - Ensure that 'id' is treated as a categorical variable rather than a numerical one, despite being stored as an integer.
   - Convert 'name' to a categorical data type if it's not already.

f) Handling of 'swords' column:
   - The 'swords' column has a relatively small number of unique values. Consider if this should be treated as a categorical variable instead of a continuous one.

g) Correlation analysis:
   - Perform a correlation analysis to identify highly correlated features. This can help in feature selection and avoiding multicollinearity in modeling.

h) Consistency checks:
   - Verify that derived metrics (e.g., 'whiff_per_swing') are consistent with their component parts ('whiffs' and 'swings_competitive').

i) Documentation:
   - Create a data dictionary that explains each column, its units, and how it's calculated. This will be invaluable for anyone working with or interpreting the data.

By addressing these points, you'll have a cleaner, more normalized dataset that's better suited for analysis and modeling. Remember to document all changes made during the cleaning process for transparency and reproducibility.
2024-07-06 20:43:25,096 - INFO - Analysis log saved to: structure_analysis_1720313005.095377.log
2024-07-06 20:43:37,786 - INFO - HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
2024-07-06 20:43:37,790 - INFO - Interaction logged to sql_transformations_1720313017.788786.log
2024-07-06 20:43:37,790 - INFO - SQL Transformations for mlb_bat_tracking.csv:
Certainly! I'll provide SQL statements for data cleaning, normalization, and additional transformations to improve data quality based on the analysis. These statements assume you're using a SQL database that supports window functions and common table expressions (CTEs).

1. SQL statements for data cleaning:

```sql
-- 1. Handle potential outliers using z-score method
WITH stats AS (
  SELECT
    AVG(batter_run_value) AS avg_brv,
    STDDEV(batter_run_value) AS stddev_brv,
    AVG(whiffs) AS avg_whiffs,
    STDDEV(whiffs) AS stddev_whiffs
  FROM baseball_stats
),
z_scores AS (
  SELECT *,
    (batter_run_value - stats.avg_brv) / stats.stddev_brv AS brv_z_score,
    (whiffs - stats.avg_whiffs) / stats.stddev_whiffs AS whiffs_z_score
  FROM baseball_stats, stats
)
UPDATE baseball_stats
SET
  batter_run_value = CASE
    WHEN ABS(z_scores.brv_z_score) > 3 THEN NULL
    ELSE batter_run_value
  END,
  whiffs = CASE
    WHEN ABS(z_scores.whiffs_z_score) > 3 THEN NULL
    ELSE whiffs
  END
FROM z_scores
WHERE baseball_stats.id = z_scores.id;

-- 2. Convert percentages to 0-100 scale
UPDATE baseball_stats
SET
  percent_swings_competitive = percent_swings_competitive * 100,
  hard_swing_rate = hard_swing_rate * 100,
  whiff_per_swing = whiff_per_swing * 100,
  zone_swing_rate = zone_swing_rate * 100,
  chase_rate = chase_rate * 100;

-- 3. Convert 'id' to varchar to treat it as categorical
ALTER TABLE baseball_stats
ALTER COLUMN id TYPE varchar;

-- 4. Convert 'swords' to categorical if it has a small number of unique values
ALTER TABLE baseball_stats
ALTER COLUMN swords TYPE varchar;
```

2. SQL statements for data normalization:

```sql
-- Min-max scaling for numerical columns
WITH min_max AS (
  SELECT
    MIN(avg_bat_speed) AS min_abs, MAX(avg_bat_speed) AS max_abs,
    MIN(batter_run_value) AS min_brv, MAX(batter_run_value) AS max_brv,
    MIN(whiffs) AS min_whiffs, MAX(whiffs) AS max_whiffs,
    MIN(swings_competitive) AS min_sc, MAX(swings_competitive) AS max_sc
  FROM baseball_stats
)
UPDATE baseball_stats
SET
  avg_bat_speed = (avg_bat_speed - min_max.min_abs) / (min_max.max_abs - min_max.min_abs),
  batter_run_value = (batter_run_value - min_max.min_brv) / (min_max.max_brv - min_max.min_brv),
  whiffs = (whiffs - min_max.min_whiffs) / (min_max.max_whiffs - min_max.min_whiffs),
  swings_competitive = (swings_competitive - min_max.min_sc) / (min_max.max_sc - min_max.min_sc)
FROM min_max;
```

3. Additional SQL transformations to improve data quality:

```sql
-- 1. Feature engineering: Create a new ratio metric
ALTER TABLE baseball_stats
ADD COLUMN whiff_to_swing_ratio NUMERIC;

UPDATE baseball_stats
SET whiff_to_swing_ratio = CASE
  WHEN swings_competitive > 0 THEN whiffs::NUMERIC / swings_competitive
  ELSE NULL
END;

-- 2. Consistency check for whiff_per_swing
UPDATE baseball_stats
SET whiff_per_swing = (whiffs::NUMERIC / swings_competitive) * 100
WHERE ABS(whiff_
2024-07-06 20:43:37,791 - INFO - SQL transformations log saved to: sql_transformations_1720313017.788786.log
2024-07-06 20:43:38,207 - INFO - Visualization created for mlb_bat_tracking
2024-07-06 20:43:38,207 - INFO - Visualizations saved to: visualizations/mlb_bat_tracking_correlation_heatmap.png
2024-07-06 20:43:38,207 - INFO - Processed table: mlb_bat_tracking