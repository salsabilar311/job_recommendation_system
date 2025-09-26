from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from collections import Counter

app = Flask(__name__)

# Load model and dataset
# model_file = 'job_recommender.pkl'
data_file = 'filtered_minimum_skill.data'

# Define the function used by the model
def recommend_jobs(user_skills, data_file='filtered_minimum_skill.data'):
    df = pd.read_csv(data_file)
    df['skills'] = df['skills'].fillna('')
    user_skills_str = ' '.join(user_skills)
    vectorizer = CountVectorizer().fit_transform([user_skills_str] + df['skills'].tolist())
    vectors = vectorizer.toarray()
    cosine_sim = cosine_similarity(vectors[0:1], vectors[1:]).flatten()
    df['cosine_similarity'] = cosine_sim
    df['missing_skills'] = df['skills'].apply(lambda skills: list(set(skills.split(', ')) - set(user_skills)))
    df['skills'] = df['skills'].apply(lambda skills: skills.split(', '))
    df = df.sort_values(by='cosine_similarity', ascending=False).reset_index(drop=True)
    filtered_df = df[df['cosine_similarity'] > 0].reset_index(drop=True)
    return filtered_df[['job_title', 'skills', 'missing_skills', 'cosine_similarity']].head(5)

# Route for the home page
@app.route('/')
def index():
    skills = ['api', 'aws', 'azure', 'cloud', 'css', 'docker', 'git', 'go', 'google cloud', 'html', 'java', 'javascript', 'kafka', 'kubernetes', 'laravel', 'microservices', 'mysql', 'node', 'php', 'python', 'react', 'redis', 'ruby', 'scala', 'spark', 'spring boot', 'sql', 'tableau']
    return render_template('home.html', skills=skills)

@app.route('/submit_skills', methods=['GET', 'POST'])
def submit_skills():
    # Load the data
    df = pd.read_csv(data_file)
    
    # Count the occurrences of each skill
    skills_list = df['skills'].str.split(', ').explode()
    skill_counts = Counter(skills_list)
    
    # Prepare data for visualization
    skills, counts = zip(*skill_counts.items())
    
    return render_template('vis.html', skills=skills, counts=counts)

@app.route('/recommend', methods=['POST'])
def home():
    data = request.form.getlist('skills')
    print(data)

    # Memisah tanda koma di inputan user
    # user_skills = [skill.strip() for skill in data]
    user_skills = data  # Data sudah berupa daftar kata
    print(f"User Skills: {user_skills}")
    
    # Memberikan rekomendasi
    recommendations = recommend_jobs(user_skills, data_file=data_file)

    # Print buat di vscode
    print(f"Recommendations: {recommendations.to_dict(orient='records')}")

    # Mengarahkan ke after.html
    return render_template('after.html', recommendations=recommendations.to_dict(orient='records'), user_skills=user_skills)

if __name__ == '__main__':
    app.run(port=3000, debug=True)
