def score_company(company):

    score = 50

    employees = company.get("employee_count", 0)

    if employees > 50:
        score += 10

    if employees > 500:
        score += 15

    if employees > 5000:
        score += 20

    return min(score, 100)