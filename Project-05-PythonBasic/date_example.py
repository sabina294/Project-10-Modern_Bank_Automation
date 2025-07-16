from datetime import datetime

current_date_time = datetime.now()
print(current_date_time) # 2025-07-10 19:51:34.358496

current_date = datetime.today().date()
print(current_date) # 2025-07-10

current_time = datetime.now().time()
print(current_time) #19:51:34.358496

format_date = current_date_time.strftime("%d-%m-%Y")
print(format_date)

format_time = current_time.strftime("%I:%M %p")
print(format_time)