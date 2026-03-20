from datetime import datetime, timedelta

now = datetime.now()
future = now + timedelta(days=5)
print(future)
