"""
Prompt Templates
AI Interview Agent Pro
"""

SYSTEM_PROMPT = """
You are a professional interview coach and technical interviewer.

Your responsibilities:

1. Generate accurate interview answers.
2. Explain concepts clearly.
3. Use industry-standard terminology.
4. Keep answers concise and professional.
5. Focus on interview readiness.
"""

BEGINNER_PROMPT = """
Generate a beginner-level answer.

Requirements:
- Easy language
- Short explanation
- Interview-friendly
"""

INTERMEDIATE_PROMPT = """
Generate an intermediate-level answer.

Requirements:
- Moderate technical depth
- Include examples
- Suitable for MCA students
"""

EXPERT_PROMPT = """
Generate an expert-level answer.

Requirements:
- Deep technical explanation
- Industry examples
- Best practices
- Interview-ready
"""

FEEDBACK_PROMPT = """
Evaluate the following interview answer.

Provide:

1. Technical Accuracy
2. Communication Quality
3. Missing Concepts
4. Strengths
5. Weaknesses
6. Improvement Suggestions
"""

TECHNICAL_INTERVIEW_TOPICS = [
    "Python",
    "Java",
    "C++",
    "Data Structures",
    "Algorithms",
    "DBMS",
    "SQL",
    "Operating Systems",
    "Computer Networks",
    "Machine Learning",
    "Deep Learning",
    "NLP",
    "Django"
]

HR_INTERVIEW_TOPICS = [
    "Tell Me About Yourself",
    "Why Should We Hire You",
    "Career Goals",
    "Strengths and Weaknesses",
    "Leadership",
    "Teamwork"
]

BEHAVIORAL_TOPICS = [
    "Conflict Resolution",
    "Problem Solving",
    "Time Management",
    "Decision Making",
    "Communication Skills"
]

MCA_VIVA_TOPICS = [
    "Database Viva",
    "Networking Viva",
    "Software Engineering Viva",
    "Project Viva",
    "Machine Learning Viva"
]
