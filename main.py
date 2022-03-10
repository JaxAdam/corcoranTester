import requests as requests

website = input("Введите адрес ресурса для оценки: ")
allN = int(input("Введите общее количество испытании: "))
errors = {}
totalErrorsCount = 0
sumTotals = 0
print("------")
for req in range(allN):
    try:
        response = requests.get('https://' + website, timeout=0.06)
        if response.status_code != 200:
            if response.status_code in errors.keys():
                errors[response.status_code] += 1
            else:
                errors[response.status_code] = 1
            totalErrorsCount += 1
    except:
        if 'timeout' in errors.keys():
            errors['timeout'] += 1
        else:
            errors['timeout'] = 1
        totalErrorsCount += 1

print(errors)

for i in errors:
    a = errors[i]/allN
    N = errors[i]
    wai = 0
    if(N > 0):
        wai = a
    print("Yi = " + str(wai))
    total = (wai * (N - 1)) / allN
    sumTotals += total
    print("------")
    print("Total: " + str(total))
    print("------")
R = totalErrorsCount/allN + sumTotals
print("R = " + str(R))
