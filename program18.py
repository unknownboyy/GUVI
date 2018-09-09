import time
while True:
    _seconds=int(time.time())+5*3600+30*60
    seconds=_seconds%86400
    hour=seconds//3600
    seconds=seconds%3600
    minute=seconds//60
    seconds=seconds%60
    print(hour,'H ',minute,'M ',seconds,'S ')
    time.sleep(1)