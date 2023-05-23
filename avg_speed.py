# If a person traveled up a hill for 18mins at 20mph and then traveled back down the same path at 60mph then their average speed traveled was 30mph.

# Write a function that returns the average speed traveled given an uphill time, uphill rate and a downhill rate. Uphill time is given in minutes. Return the rate as an integer (mph). No rounding is necessary.


def ave_spd(up_time, up_spd, down_spd):
    return (2*((up_time/60)*up_spd))/((up_time/60)+((((up_time/60)*up_spd))/down_spd))

ans =ave_spd(18,20,60)
print(ans)