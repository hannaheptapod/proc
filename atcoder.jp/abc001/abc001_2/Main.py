m = int(input())
if m < 100: vv = 0
elif m <= 5000: vv = m*10//1000
elif m <= 30000: vv = m//1000 + 50
elif m <= 70000: vv = (m//1000 - 30)//5 + 80
else: vv = 89
print('{:02}'.format(vv))