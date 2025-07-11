import pandas as pd

# Load original job dataset
df = pd.read_csv("Dataset.csv", encoding='latin1')

# Split Skills and Certifications into list
df['Skills'] = df['Skills'].apply(lambda x: [i.strip() for i in str(x).split(',')])
df['Certifications'] = df['Certifications'].apply(lambda x: [i.strip() for i in str(x).split(',')])

# Explode skills and certifications into rows
skills_df = df[['Job Title', 'Skills']].explode('Skills')
skills_df = skills_df.rename(columns={'Skills': 'Skill'})

cert_df = df[['Job Title', 'Certifications']].explode('Certifications')
cert_df = cert_df.rename(columns={'Certifications': 'Certification'})

# Export to CSV for Power BI
skills_df.to_csv("job_skills.csv", index=False)
cert_df.to_csv("job_certs.csv", index=False)
df.to_csv("job_main.csv", index=False)
