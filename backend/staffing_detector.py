def is_staffing_company(company):

    text = (
        company.get("description", "")
        + " "
        + " ".join(company.get("specialities", []))
    ).lower()

    keywords = [
        "recruitment",
        "staffing",
        "talent acquisition",
        "executive search",
        "headhunting",
        "hiring"
    ]

    for keyword in keywords:
        if keyword in text:
            return True

    return False