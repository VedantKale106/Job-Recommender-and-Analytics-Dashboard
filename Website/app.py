from flask import Flask, render_template, request, jsonify
import pandas as pd
import re

app = Flask(__name__)

# Load and preprocess data
try:
    df = pd.read_csv("Dataset.csv", encoding='latin1')
    # Clean 'Skills' column
    df['Skills'] = df['Skills'].apply(lambda x: [i.strip().lower() for i in str(x).split(',')] if pd.notna(x) else [])
    
    # Create a set of all unique skills for suggestions
    all_skills = set()
    for skills_list in df['Skills']:
        all_skills.update(skills_list)
    all_skills = sorted(list(all_skills))
    
except Exception as e:
    print(f"Error loading dataset: {e}")
    df = pd.DataFrame()
    all_skills = []

# Enhanced skill matching function
def recommend_jobs(student_skills, top_n=5):
    student_skills = [s.strip().lower() for s in student_skills if s.strip()]
    recommendations = []

    for _, row in df.iterrows():
        job_skills = row['Skills']
        if not job_skills:
            continue
            
        matched = list(set(student_skills) & set(job_skills))
        missing = list(set(job_skills) - set(student_skills))
        match_score = len(matched) / len(job_skills) if job_skills else 0

        recommendations.append({
            'Job Title': row['Job Title'],
            'Match %': round(match_score * 100, 2),
            'Matched Skills': matched,
            'Missing Skills': missing,
            'Total Skills Required': len(job_skills),
            'Skills Matched': len(matched)
        })

    recommendations = sorted(recommendations, key=lambda x: (x['Match %'], x['Skills Matched']), reverse=True)
    return recommendations[:top_n]

# Get skill suggestions based on partial input
def get_skill_suggestions(query, limit=10):
    query = query.lower().strip()
    if not query:
        return []
    
    suggestions = [skill for skill in all_skills if query in skill.lower()]
    return suggestions[:limit]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        skills_input = request.form["skills"]
        student_skills = [s.strip() for s in skills_input.split(',') if s.strip()]
        top_n = int(request.form.get("top_n", 5))
        
        results = recommend_jobs(student_skills, top_n)
        
        # Calculate some statistics
        total_jobs = len(df)
        jobs_with_matches = len([r for r in results if r['Match %'] > 0])
        
        stats = {
            'total_jobs': total_jobs,
            'jobs_with_matches': jobs_with_matches,
            'avg_match': round(sum(r['Match %'] for r in results) / len(results), 2) if results else 0
        }
        
        return render_template("result.html", 
                             skills=student_skills, 
                             results=results, 
                             stats=stats,
                             top_n=top_n)
    
    return render_template("index.html", popular_skills=all_skills[:20])

@app.route("/api/skills")
def api_skills():
    query = request.args.get('q', '')
    suggestions = get_skill_suggestions(query)
    return jsonify(suggestions)

if __name__ == "__main__":
    app.run(debug=True)