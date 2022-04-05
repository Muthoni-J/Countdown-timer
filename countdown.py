import time
sec =int(input('how many sec countdown? '))

for x in range(sec):
    print(str(sec - x)+ 'seconds remaining')
    time.sleep(1)
    
