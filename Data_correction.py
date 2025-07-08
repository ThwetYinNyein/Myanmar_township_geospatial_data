import pandas as pd
df = pd.read_csv("township_summary.csv")

# Define the new row as a DataFrame
new_row = pd.DataFrame([{
    "Township_Name": "Hlaingtharya",
    "Township_Code": "MMR013008",
    "Latitude": 16.8799,
    "Longitude": 96.0546,
    "Area_km2": 67.365591
}])

# Append the new row
df = pd.concat([df, new_row], ignore_index=True)

# Drop rows with specific Township_Code values
df = df[~df['Township_Code'].isin(['MMR013046', 'MMR013047'])]

# Save back to CSV (optional)
df.to_csv("township_summary_updated.csv", index=False)

# Print confirmation
print("✅ Updated DataFrame with new row and removed rows:")
print(df.tail())
