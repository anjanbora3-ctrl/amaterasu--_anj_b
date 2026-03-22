import pandas as pd
import matplotlib.pyplot as plt
import os

def analyze_devsecops_data(file_path):
    print(f"--- DevSecOps Security Analyzer - Starting Analysis ---")
    
    # 1. Load Dataset
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return

    df = pd.read_excel(file_path)
    print(f"Loaded dataset with {len(df)} records.")

    # 2. Define Risk Scoring
    severity_map = {'High': 5, 'Medium': 3, 'Low': 1}
    
    # 3. Calculate Risk Scores
    df['Severity_Score'] = df['Vulnerability_Severity'].map(severity_map).fillna(0)
    df['Exposure_Score'] = df['Public_Exposure'].apply(lambda x: 5 if x == 'Yes' else 0)
    df['Total_Risk_Score'] = df['Severity_Score'] + df['Exposure_Score']

    # 4. Classify Risk Levels
    def classify_risk(score):
        if score >= 8: return 'High'
        elif score >= 4: return 'Medium'
        else: return 'Low'

    df['Risk_Level'] = df['Total_Risk_Score'].apply(classify_risk)

    # 5. Identify Top Risky Repositories (Summing risks if same repo has multiple issues)
    repo_risk = df.groupby('Repository_Name')['Total_Risk_Score'].sum().sort_values(ascending=False).head(10)
    repo_risk_df = repo_risk.reset_index()

    # 6. Detect Anomalies (High risk AND Publicly Exposed)
    anomalies = df[(df['Vulnerability_Severity'] == 'High') & (df['Public_Exposure'] == 'Yes')]
    
    # 7. Generate Output Reports
    print("Generating CSV reports...")
    df.to_csv('risk_analysis_report.csv', index=False)
    repo_risk_df.to_csv('top_risky_repositories.csv', index=False)
    if not anomalies.empty:
        anomalies.to_csv('anomalies_report.csv', index=False)
        print(f"Detected {len(anomalies)} critical anomalies.")

    # 8. Create Visual Charts
    print("Generating visualization charts...")
    
    # Chart 1: Vulnerability Distribution
    plt.figure(figsize=(10, 6))
    df['Vulnerability_Severity'].value_counts().plot(kind='bar', color=['red', 'orange', 'green'])
    plt.title('Distribution of Vulnerability Severity')
    plt.xlabel('Severity')
    plt.ylabel('Count')
    plt.savefig('vulnerability_distribution.png')
    plt.close()

    # Chart 2: Risk Levels
    plt.figure(figsize=(10, 6))
    df['Risk_Level'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['red', 'yellow', 'green'])
    plt.title('Overall Risk Level Distribution')
    plt.ylabel('')
    plt.savefig('risk_level_chart.png')
    plt.close()

    # Chart 3: Top 5 Risky Repositories
    plt.figure(figsize=(10, 6))
    top_5 = repo_risk_df.head(5)
    plt.bar(top_5['Repository_Name'], top_5['Total_Risk_Score'], color='darkred')
    plt.title('Top 5 Risky Repositories')
    plt.xlabel('Repository Name')
    plt.ylabel('Aggregate Risk Score')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('top_risky_repos.png')
    plt.close()

    print("--- Analysis Complete ---")
    print(f"Reports saved: risk_analysis_report.csv, top_risky_repositories.csv")
    print(f"Charts saved: vulnerability_distribution.png, risk_level_chart.png, top_risky_repos.png")

if __name__ == "__main__":
    DATASET_FILE = "devsecops_pipeline_security_dataset (2).xlsx"
    analyze_devsecops_data(DATASET_FILE)
