n = int(input())
if n < 10: ans = '000' + str(n)
elif n < 100: ans = '00' + str(n)
elif n < 1000: ans = '0' + str(n)
else: ans = str(n)
print(ans)