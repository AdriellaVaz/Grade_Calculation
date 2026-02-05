def calculate_average(marks):
    if len(marks) != 5:
        raise ValueError("Exactly 5 subjects are required")

    for mark in marks:
        if mark < 0 or mark > 100:
            raise ValueError("Marks must be between 0 and 100")

    return sum(marks) / 5


def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 75:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "Fail"