import time

from forecast import get_forecast_five_day

for i in get_forecast_five_day():
    print(i)
    time.sleep(2)
