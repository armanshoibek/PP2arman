from datetime import datetime

current_datetime = datetime.now()

current_datetime_without_microseconds = current_datetime.replace(microsecond=0)

print("С микросекундами:", current_datetime)
print("Без микросекунд:", current_datetime_without_microseconds)
