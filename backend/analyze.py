from company_parser import extract_company_data
from lead_scoring import score_company
from staffing_detector import is_staffing_company


def analyze_company(company):

    company_data = extract_company_data(
        company
    )

    staffing = is_staffing_company(
        company_data
    )

    score = score_company(
        company_data
    )

    if staffing:
        score -= 40

    return {
        "company_name": company_data["name"],
        "website": company_data["website"],
        "employee_count": company_data["employee_count"],
        "followers": company_data["followers"],
        "staffing_agency": staffing,
        "lead_score": max(score, 0)
    }