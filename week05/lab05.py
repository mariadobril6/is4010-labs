def calculate_average_age(users):
    """Return the average numeric age, or 0.0 when none are valid."""
    ages = []

    for user in users:
        age = user.get("age")

        if isinstance(age, (int, float)) and not isinstance(age, bool):
            ages.append(age)

    if not ages:
        return 0.0

    return sum(ages) / len(ages)


def get_active_user_emails(users):
    """Return email addresses belonging to active users."""
    emails = []

    for user in users:
        if user.get("is_active") and "email" in user:
            emails.append(user["email"])

    return emails
    