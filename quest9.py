brightnessLevels = [14498, 10099 ,17618 ,13490 ,17647, 14071, 10107, 10059, 16218, 10000]
test = [2,4,7,16]
t = 0

for sparkball in brightnessLevels:
    t +=  (sparkball//10)
    sparkball = sparkball%10

    t +=  (sparkball//5)
    sparkball = sparkball%5

    t +=  (sparkball//3)
    sparkball = sparkball%3

    t +=  (sparkball//1)
    sparkball = sparkball%1
   
print(t)



# Part 2 
# minimum number of beetles for a certain brightness
def minBeetles(brightness):
    dp = [float('inf')] * (brightness + 1)
    dp[0] = 0

    for i in range(1, brightness + 1):
        for stamp in stamps:
            if i - stamp >= 0:
                dp[i] = min(dp[i], dp[i - stamp] + 1)

    return dp[brightness]

stamps = [30, 25, 24, 20, 16, 15, 10, 5, 3, 1]
brightnessLevels = list(map(int, open('notes9-2.txt').read().split('\n')))
t = 0

for brightness in brightnessLevels:
    t += minBeetles(brightness)
print(t)
