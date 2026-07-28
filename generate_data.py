import pandas as pd
import numpy as np

np.random.seed(42)

schools = [
    "School of Medicine",
    "School of Dentistry",
    "School of Pharmacy",
    "School of Health Care Sciences",
    "School of Science and Technology"
]

programmes = {
    "School of Medicine": ["MBChB"],
    "School of Dentistry": ["BDS"],
    "School of Pharmacy": ["BPharm"],
    "School of Health Care Sciences": [
        "BNursing",
        "Radiography",
        "Physiotherapy"
    ],
    "School of Science and Technology": [
        "BSc Life Sciences",
        "BSc Biochemistry",
        "BSc Mathematics"
    ]
}

provinces = [
    "Gauteng",
    "Limpopo",
    "North West",
    "Mpumalanga",
    "Free State",
    "Eastern Cape",
    "KwaZulu-Natal"
]

comments = [
    "Excellent teaching.",
    "Need faster assessment feedback.",
    "Tutors are supportive.",
    "LMS performance needs improvement.",
    "Clinical placements are valuable.",
    "Need more practical sessions.",
    "Library resources are excellent.",
    "Assessment workload is high.",
    "Lecturers explain concepts well.",
    "Communication can be improved."
]

records = []

for i in range(1, 5001):

    school = np.random.choice(schools)

    attendance = np.random.randint(45, 100)

    lms = np.random.randint(20, 180)

    library = np.random.randint(0, 30)

    tutors = np.random.randint(0, 10)

    assessment = int(
        attendance * 0.45 +
        lms * 0.18 +
        np.random.normal(10, 8)
    )

    assessment = max(30, min(95, assessment))

    if assessment >= 65:
        risk = "Low"
    elif assessment >= 50:
        risk = "Medium"
    else:
        risk = "High"

    epistemic = int(
        attendance * 0.6 +
        tutors * 2 +
        np.random.randint(-8, 8)
    )

    epistemic = max(40, min(100, epistemic))

    satisfaction = np.random.randint(2, 6)

    feedback = np.random.randint(5, 30)

    records.append({

        "StudentID": f"SMU{i:05d}",

        "School": school,

        "Programme": np.random.choice(programmes[school]),

        "YearLevel": np.random.randint(1, 5),

        "Gender": np.random.choice(["Male", "Female"]),

        "Age": np.random.randint(18, 30),

        "Province": np.random.choice(provinces),

        "Funding": np.random.choice(
            ["NSFAS", "Bursary", "Self-funded"]
        ),

        "Attendance": attendance,

        "LMSLogins": lms,

        "LibraryVisits": library,

        "TutorSessions": tutors,

        "AssessmentAverage": assessment,

        "FeedbackDays": feedback,

        "Satisfaction": satisfaction,

        "RiskLevel": risk,

        "EpistemicAccess": epistemic,

        "Comment": np.random.choice(comments)

    })

df = pd.DataFrame(records)

df.to_csv("data/students.csv", index=False)

print("students.csv created successfully.")
