from collections import defaultdict
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from matplotlib import axes


# конвертируем строку в список
def convertStrToList(value):
    return list(map(int, data.split()))


# создаем мапу значений против их количества	
def buildMapOfValueVsAmount(convertedData):
    return {value: convertedData.count(value) for value in convertedData}


# находим уникальные значения из списка	
def findUniqueValues(convertedData):
    return list(set(convertedData))


# строим график
def printStepPlot(x, y):
    ax = plt.gca()
    ax.set_xlim(x[0] - 10, x[-1] + 5)
    pr = x[0] - 10
    for i, v in enumerate(x):
        if i != 0:
            plt.step([pr, v], [y[i], y[i]], where="post", color='b')
            plt.plot([pr], [y[i]], 'bo', alpha=1)
            if (i != len(x) - 1):
                plt.plot([v], [y[i]], 'bo', alpha=1, fillstyle='none')
        pr = v
    plt.step([pr, v + 10], [1, 1], where="post", color='b')
    plt.step([x[0] - 10, x[0]], [0, 0], where='post', color='b')
    plt.plot([x[0]], [0], 'bo', alpha=1, fillstyle='none')


# строим эмпирическую функци. распределения
def plotEmpiricalDistributionFunction(uniqueValues, mapOfValueVsAmount, length):
    temp = 0
    empiricalDistributionFunctionData = []
    for i in uniqueValues:
        temp += mapOfValueVsAmount[i]
        empiricalDistributionFunctionData.append(temp / length)
    plt.figure(0)
    plt.rcParams["figure.figsize"] = (20, 10)
    printStepPlot(uniqueValues, empiricalDistributionFunctionData)


# строим гистограмму	
def plotBarChart(convertedData):
    plt.figure(1)
    plt.rcParams["figure.figsize"] = (20, 10)

    k = -1
    res = []
    m = 11
    for i, v in enumerate(range(min(convertedData), max(convertedData) + 1)):
        if i % m == 0:
            res.append(0)
            k += 1
        if v in convertedData:
            res[k] += convertedData.count(v)
    sz = (max(convertedData) - min(convertedData) + 1) // m
    plt.xticks(range(sz), [f"{min(convertedData) + i * m}-{min(convertedData) + (i + 1) * m - 1}" for i in range(sz)])
    plt.bar(range(sz), res)


# находим среднее значение (сумма всех значений из сета поделить на количество)
def findAndPrintMiddleValue(convertedData):
    mid = sum(convertedData) / len(convertedData)
    print("Среднее значаение:", mid)
    return mid


# находим выборочный момент
def moment(i, uniqueValues, convertedData):
    return sum(map(lambda uniqueValues: (uniqueValues - mid) ** i, convertedData)) / len(convertedData)


# находим выборочную дисперсию ( момент от 2)
def findAndPrintSampleVariance(uniqueValues, convertedData):
    sampleVariance = moment(2, uniqueValues, convertedData)
    print("Выборочная дисперсия:", sampleVariance)
    return sampleVariance


# находим стандартную ошибку (квадрат выб. дисперсии деленный на длину сета)
def findAndPrintStandardError(sampleVariance, convertedData):
    standardError = (sampleVariance / len(convertedData)) ** 0.5
    print("Стандартная ошибка выборки:", standardError)
    return standardError


# находим моду (самое часто попадающееся значение в сете)
def findAndPrintModa(convertedData):
    row = buildMapOfValueVsAmount(convertedData)
    mx = max(row.values())
    moda = 0
    for value, amount in row.items():
        if amount == mx:
            moda = value
            break
    print("Мода:", moda)
    return moda


# средний элемент (медиана)
def findAndPrintMediana(convertedData):
    med = convertedData[len(convertedData) // 2]
    if len(convertedData) % 2 == 0:
        med += convertedData[len(convertedData) // 2 - 1]
        med /= 2
    print("Медиана:", med)
    return med


# квартиль 1 (первый элемент делящий сет на 4 части)
def findAndPrintQuart1(convertedData):
    quart1 = convertedData[len(convertedData) // 4]
    if len(convertedData) % 4 == 0:
        quart1 += convertedData[len(convertedData) // 4 - 1]
        quart1 /= 2
    print("Квартиль 1:", quart1)
    return quart1


# квартиль 2 (первый элемент делящий сет на 4 части)
def findAndPrintQuart2(convertedData):
    quart2 = convertedData[len(convertedData) // 4 * 3]
    if len(convertedData) % 4 == 0:
        quart2 += convertedData[len(convertedData) // 4 * 3 - 1]
        quart2 /= 2
    print("Квартиль 2:", quart2)
    return quart2


# стандартное отклонение (корень из дисперсии)
def findAndPrintSigma(sampleVariance):
    sigma = sampleVariance ** 0.5
    print("Среднее стандартное отклонение:", sigma)
    return sigma


# находим эксцесс (мера остроты пика в распределении случайной величины)
def findAndPrintExcess(uniqueValues, convertedData, sampleVariance):
    excess = moment(4, uniqueValues, convertedData) / (sampleVariance ** 2) - 3
    print("Эксцесс:", excess)
    return excess


# находим ассиметрию (числовое отображение степени отклонения графика распределения показателей от симметричного графика распределения) 
def findAndPrintAsymmetry(uniqueValues, convertedData, sigma):
    asymmetry = moment(3, uniqueValues, convertedData) / (sigma ** 3)
    print("Ассиметричность:", asymmetry)
    return asymmetry


# находим мак и мин
def findAndPrintMaxMin(convertedData):
    print("Минимум:", convertedData[0])
    print("Максимум:", convertedData[-1])
    return convertedData[-1], convertedData[0]


# находим критерий согласия Пирсона
def findAndPrintAcceptanceCriterion(convertedData):
    print("---Критерий Пирсона---")
    print("Объем выборки: ", len(convertedData))


data = '''189 207 213 208 186 210 198 219 231 227 202 211 220 236 227 220 210 183 213
190 197 227 187 226 213 191 209 196 202 235 211 214 220 195 182 228 202 207
192 226 193 203 232 202 215 195 220 233 214 185 234 215 196 220 203 236 225
221 193 215 204 184 217 193 216 205 197 203 229 204 225 216 233 223 208 204
207 182 216 191 210 190 207 205 232 222 198 217 211 201 185 217 225 201 208
211 189 205 207 199'''

convertedData = convertStrToList(data)
convertedData.sort()
length = len(convertedData)
mapOfValueVsAmount = buildMapOfValueVsAmount(convertedData)
uniqueValues = findUniqueValues(convertedData)

plotEmpiricalDistributionFunction(uniqueValues, mapOfValueVsAmount, length)
plotBarChart(convertedData)
plt.show()

mid = findAndPrintMiddleValue(convertedData)
sampleVariance = findAndPrintSampleVariance(uniqueValues, convertedData)
standardError = findAndPrintStandardError(sampleVariance, convertedData)
moda = findAndPrintModa(convertedData)
med = findAndPrintMediana(convertedData)
quart1 = findAndPrintQuart1(convertedData)
quart2 = findAndPrintQuart2(convertedData)
sigma = findAndPrintSigma(sampleVariance)
excess = findAndPrintExcess(uniqueValues, convertedData, sampleVariance)
asymetry = findAndPrintAsymmetry(uniqueValues, convertedData, sigma)
max, min = findAndPrintMaxMin(convertedData)
