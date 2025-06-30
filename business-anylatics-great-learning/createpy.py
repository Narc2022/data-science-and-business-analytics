import pandas as pd

# Create the data for HLOOKUP example
data = {
    "Math": [88, "B+"],
    "Science": [92, "A"],
    "English": [79, "C+"],
    "History": [85, "B"],
}

# Create a DataFrame with 'Marks' and 'Grade' as rows
df = pd.DataFrame(data, index=["Marks", "Grade"])

# Add a 'Category' column to label the rows
df.insert(0, "Category", ["Marks", "Grade"])

# Save the DataFrame to an Excel file
file_path = "/mnt/data/HLOOKUP_Example_Data.xlsx"
df.to_excel(file_path, index=False)

file_path
