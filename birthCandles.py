def birthdayCakeCandles(candles):
    maxcand=max(candles)
    counter=0
    for i in candles:
        if i==maxcand:
            counter +=1
    return counter