def detect_buying_signals(company):

    signals = []

    employee_count = company.get(
        "employeeCount", 0
    )

    follower_count = company.get(
        "followerCount", 0
    )

    description = (
        company.get("description", "")
    ).lower()

    if employee_count > 500:
        signals.append(
            "Large organization"
        )

    if employee_count > 5000:
        signals.append(
            "Enterprise scale company"
        )

    if follower_count > 100000:
        signals.append(
            "Strong LinkedIn presence"
        )

    growth_keywords = [
        "ai",
        "artificial intelligence",
        "automation",
        "machine learning",
        "innovation",
        "scale"
    ]

    for keyword in growth_keywords:

        if keyword in description:

            signals.append(
                f"Uses keyword: {keyword}"
            )

    return signals