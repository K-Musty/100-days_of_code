# DAY 72 of 100 - Data Visualisation with Matplotlib Programming Languages
---
<img width="1402" height="1620" alt="programminglanguages" src="https://github.com/user-attachments/assets/aaf4a80a-3c92-469f-ac9c-3389c7be23c9" />

### Challenges
- Get raw data and create some charts using Pandas and Matplotlib.
- Analyze the the popularity of different programming languages over the years.


### Notes
- ```.count()``` To count the number of entries in each column, this tells the number of non-NaN values in each column.
- Use ```.groupby()``` to explore the entries per column.
- Use ```to_datetime()``` to convert strings to Datetime objects for easier plotting.
- Use ```.pivot()``` to reshape DataFrame by converting categories to columns.
- Use ```.count()``` and ```isna().values.any()``` to look for NaN values in DataFrame
- Use ```.fillna()``` to replace NaN values.
- Use ```.plot()``` to create (multiple) line charts, can also be used with a for-loop.
- Charts can be styled by changing the size, the labels, and the upper and lower bounds of the axis. Example:
```   
