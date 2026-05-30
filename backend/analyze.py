from company_parser import extract_company_data
from lead_scoring import score_company
from staffing_detector import is_staffing_company
from buying_signal import detect_buying_signals
from niche_detector import detect_niche


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

    signals = detect_buying_signals(
        company
    )

    niche_data = detect_niche(
        company
    )

    if staffing:
        score -= 40

    return {
        "company_name": company_data["name"],
        "website": company_data["website"],
        "employee_count": company_data["employee_count"],
        "followers": company_data["followers"],
        "staffing_agency": staffing,
        "lead_score": max(score, 0),

        "industry": niche_data.get(
            "industry"
        ),

        "niche": niche_data.get(
            "niche"
        ),

        "sub_niche": niche_data.get(
            "sub_niche"
        ),

        "buying_signals": signals
    }