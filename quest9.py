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
brightnessLevels = list(map(int, open('notes9-2.txt').read().split('\n')))

dp = [float('inf')] * (1493 + 1)
dp[0] = 0

def min_beetles_for_brightness(brightness, stamps):
    # Initialize dp array with a large number, representing infinity
    dp = [float('inf')] * (brightness + 1)
    dp[0] = 0  # 0 brightness requires 0 stamps
    
    # Dynamic programming to calculate minimum stamps for each brightness up to the target
    for i in range(1, brightness + 1):
        for stamp in stamps:
            if i - stamp >= 0:
                dp[i] = min(dp[i], dp[i - stamp] + 1)
    
    return dp[brightness]

def total_min_beetles(brightness_list, stamps):
    total_beetles = 0
    for brightness in brightness_list:
        total_beetles += min_beetles_for_brightness(brightness, stamps)
    return total_beetles

# Example usage
brightness_list = list(map(int, open('notes9-2.txt').read().split('\n')))
stamps = [30, 24, 20, 16, 15, 10, 5, 3, 1]
result = total_min_beetles(brightness_list, stamps)
print(result)  # Output the total number of beetles required
