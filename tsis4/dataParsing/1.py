def subtract_five_days(date_str):
    year, month, day = map(int, date_str.split('-'))
    day -= 5
    if day < 1:
        month -= 1
        if month == 0:
            year -= 1
            month = 12
        day += 30
    return f"{year:04d}-{month:02d}-{day:02d}"

date_input = input("Введите дату в формате 'ГГГГ-ММ-ДД': ")
new_date = subtract_five_days(date_input)
print("Результат после вычета пяти дней:", new_date)
