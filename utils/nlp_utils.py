def match_keywords(resume_text: str, keywords: list):
    matched = [kw for kw in keywords if kw.lower() in resume_text]
    missing = [kw for kw in keywords if kw.lower() not in resume_text]
    score = int(100 * len(matched) / len(keywords)) if keywords else 0
    return matched, missing, score
