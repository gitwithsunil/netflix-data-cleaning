import pandas as pd


# Step 1: Load the CSV File
df = pd.read_csv("netflix_titles.csv")
print("Original Data Shape:", df.shape)

# Step 2: Check for missing values
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# Step 3: Fill or Drop Null Values
df['country'] = df['country'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Not Specified')
df['director'] = df['director'].fillna('Not Specified')
df['rating'] = df['rating'].fillna('Unknown')
df = df.dropna(subset=['date_added'])

# Step 4: Remove Duplicates
df = df.drop_duplicates()

# Step 5: Standardize Text Columns
df['type'] = df['type'].str.lower().str.strip()
df['country'] = df['country'].str.title().str.strip()
df['rating'] = df['rating'].str.upper().str.strip()

# Step 6: Convert 'date_added' to datetime
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# Step 7: Rename Columns
df.columns = df.columns.str.lower().str.replace(" ", "_")

# Step 8: Print Cleaned Info
print("\nData After Cleaning:")
print(df.info())
print("\nSample Data:")
print(df.head())

# Step 9: Save Cleaned Dataset
df.to_csv("cleaned_netflix_titles.csv", index=False)
print("\nCleaned dataset saved as 'cleaned_netflix_titles.csv'")
