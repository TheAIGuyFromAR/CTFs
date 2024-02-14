startpin = 4096
count =0
pin = startpin
while(count<5521):
    pin = pin + count
    print(f"pin: {pin}")
    count = count + 1
print(f"final pin: {pin}")