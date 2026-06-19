from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Course Database
courses = [
    {
        "name": "Python for Beginners",
        "skills": "python programming coding basics",
        "difficulty": "Beginner",
        "duration": "4 Weeks"
    },
    {
        "name": "Machine Learning Fundamentals",
        "skills": "machine learning ai data science",
        "difficulty": "Intermediate",
        "duration": "8 Weeks"
    },
    {
        "name": "Web Development",
        "skills": "html css javascript frontend web design",
        "difficulty": "Beginner",
        "duration": "6 Weeks"
    },
    {
        "name": "Cloud Computing",
        "skills": "cloud aws devops infrastructure",
        "difficulty": "Intermediate",
        "duration": "7 Weeks"
    },
    {
        "name": "Data Science with Python",
        "skills": "python pandas numpy data science",
        "difficulty": "Intermediate",
        "duration": "8 Weeks"
    },
    {
        "name": "Artificial Intelligence",
        "skills": "ai machine learning neural networks python",
        "difficulty": "Advanced",
        "duration": "10 Weeks"
    },
    {
        "name": "Automation with Python",
        "skills": "python automation scripting",
        "difficulty": "Beginner",
        "duration": "5 Weeks"
    }
]

# User Input
user_interests = input("Enter your interests (comma separated): ").lower()
preferred_level = input(
    "Preferred difficulty (Beginner/Intermediate/Advanced): "
).capitalize()

# Filter courses by difficulty
filtered_courses = [
    course for course in courses
    if course["difficulty"] == preferred_level
]

if not filtered_courses:
    print("No courses found for selected difficulty level.")
    exit()

# Prepare documents
course_texts = [course["skills"] for course in filtered_courses]
documents = [user_interests] + course_texts

# TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

# Similarity Calculation
user_vector = tfidf_matrix[0]
course_vectors = tfidf_matrix[1:]

similarities = cosine_similarity(user_vector, course_vectors).flatten()

# Combine results
recommendations = []

for idx, score in enumerate(similarities):
    course = filtered_courses[idx]

    user_words = set(user_interests.replace(",", " ").split())
    course_words = set(course["skills"].split())

    matched_skills = user_words.intersection(course_words)

    recommendations.append({
        "course": course["name"],
        "difficulty": course["difficulty"],
        "duration": course["duration"],
        "score": round(score * 100, 2),
        "matched": matched_skills
    })

# Sort by similarity
recommendations.sort(
    key=lambda x: x["score"],
    reverse=True
)

# Display Results
print("\n" + "="*50)
print("      SMART COURSE RECOMMENDATIONS")
print("="*50)

for i, rec in enumerate(recommendations[:5], start=1):
    print(f"\n{i}. {rec['course']}")
    print(f"   Match Score : {rec['score']}%")
    print(f"   Difficulty  : {rec['difficulty']}")
    print(f"   Duration    : {rec['duration']}")

    if rec["matched"]:
        print(
            f"   Matched Skills : {', '.join(rec['matched'])}"
        )
    else:
        print("   Matched Skills : None")

print("\nRecommendation process completed successfully!")
