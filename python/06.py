with open('python/06.in','r') as f:
    for x in f.readlines():
        datastream = x

for count in [4,14]:
    for i in range(len(datastream)):
        unique_signals = {signal for signal in datastream[i:i+count]}
        if len(unique_signals) == count:
            print(f'{count}: {i + count}')
            break
