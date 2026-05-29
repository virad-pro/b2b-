def extract_company_data(company):

    return {
        "name": company.get("name"),
        "description": company.get("description"),
        "website": company.get("website"),
        "employee_count": company.get("employeeCount"),
        "followers": company.get("followerCount"),
        "specialities": company.get("specialities", [])
    }