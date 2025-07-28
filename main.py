import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load CSV file
df = pd.read_csv("2024-25_placements.csv")


# Define department columns
departments = [
    'CSE', 'IT', 'CSE (AIML)', 'AIML', 'AIDS', 'CSE (IOT, CS&BCT)',
    'ECE', 'EEE', 'MECH', 'CIVIL', 'CHEM', 'Bio- Tech'
]

# Melt the DataFrame
df_long = df.melt(
    id_vars=[
        'Sl.No.', 'Name of the Organization', 'Designation',
        'Internship Stipend (Rs.P.M)', 'CTC\n(Rs.In Lakhs)',
        'Date of Results Announced'
    ],
    value_vars=departments,
    var_name='Department',
    value_name='Placement Count'
)

# Clean and prepare data
df_long['Placement Count'] = pd.to_numeric(df_long['Placement Count'], errors='coerce')
df_long['CTC\n(Rs.In Lakhs)'] = pd.to_numeric(df_long['CTC\n(Rs.In Lakhs)'], errors='coerce')
df_long['Internship Stipend (Rs.P.M)'] = pd.to_numeric(df_long['Internship Stipend (Rs.P.M)'], errors='coerce')

# Extract only the first date in case of multiline date entries
df_long['Date'] = df_long['Date of Results Announced'].str.extract(r'(\d{2}.\d{2}.\d{4})')[0]
df_long['Date'] = pd.to_datetime(df_long['Date'], errors='coerce', dayfirst=True)
df_long['Year'] = df_long['Date'].dt.year

# Drop rows where Placement Count is missing
df_long.dropna(subset=['Placement Count'], inplace=True)

# Create output folder
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Save cleaned data
df_long.to_csv(os.path.join(output_dir, "cleaned_placements.csv"), index=False)
df_long.to_json(os.path.join(output_dir, "cleaned_placements.json"), orient="records", indent=2)

# 1. Total Placements by Department
plt.figure(figsize=(12, 6))
plot_data = df_long.groupby('Department')['Placement Count'].sum().reset_index()
sns.barplot(data=plot_data, x='Department', y='Placement Count', hue='Department', palette='viridis', legend=False)
plt.title("Total Placements by Department")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "placements_by_department.png"))
plt.close()

# 2. Placements Over Years
plt.figure(figsize=(12, 6))
year_data = df_long.groupby('Year')['Placement Count'].sum().reset_index()
sns.lineplot(data=year_data, x='Year', y='Placement Count', marker='o')
plt.title("Total Placements Over Years")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "placements_by_year.png"))
plt.close()

# 3. Average CTC by Department
plt.figure(figsize=(12, 6))
ctc_data = df_long.groupby('Department')['CTC\n(Rs.In Lakhs)'].mean().reset_index()
sns.barplot(data=ctc_data, x='Department', y='CTC\n(Rs.In Lakhs)', hue='Department', palette='coolwarm', legend=False)
plt.title("Average CTC by Department")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "avg_ctc_by_department.png"))
plt.close()

# 4. Average Internship Stipend by Department
plt.figure(figsize=(12, 6))
stipend_data = df_long.groupby('Department')['Internship Stipend (Rs.P.M)'].mean().reset_index()
sns.barplot(data=stipend_data, x='Department', y='Internship Stipend (Rs.P.M)', hue='Department', palette='magma', legend=False)
plt.title("Average Internship Stipend by Department")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "avg_stipend_by_department.png"))
plt.close()

# 5. Top 10 Designations Offered
top_designations = df_long['Designation'].value_counts().head(10).reset_index()
top_designations.columns = ['Designation', 'Count']
plt.figure(figsize=(10, 6))
sns.barplot(data=top_designations, x='Count', y='Designation', hue='Designation', palette='Set2', legend=False)
plt.title("Top 10 Designations Offered")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "top_designations.png"))
plt.close()

print("✅ All processing complete. Check the 'output/' folder for results.")
