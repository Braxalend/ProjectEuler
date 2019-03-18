#Счет букв в числительных
#Если записать числа от 1 до 5 английскими словами (one, two, three, four, five), то используется всего
# 3 + 3 + 5 + 4 + 4 = 19 букв.
#
#Сколько букв понадобится для записи всех чисел от 1 до 1000 (one thousand) включительно?
#
#
#Примечание: Не считайте пробелы и дефисы. Например, число 342 (three hundred and forty-two) состоит из 23 букв,
#число 115 (one hundred and fifteen) - из 20 букв. Использование "and" при записи чисел соответствует правилам
#британского английского.
import inflect

w = inflect.engine()
print (sum([len(w.number_to_words(x).replace(' ','').replace('-','')) for x in range(1,1001)]))

#or

nums={
    1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine',
    10:'ten',
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    15:'fifteen',
    18:'eighteen',
    20:'twenty',
    30:'thirty',
    40:'forty',
    50:'fifty',
    60:'sixty',
    70:'seventy',
    80:'eighty',
    90:'ninety',
    }

def GenNum(n,dic):
    tmp=''
    t=str(n)
    if dic.get(n,False):
        return dic[n]
    elif n<20:
        return dic[int(t[1])]+'teen'
    elif n<100:
        tmp=n-int(t[1])
        return dic[tmp]+dic[int(t[1])]
    elif n<1000:
        if t[1:3]=='00':
            return dic[int(t[0])]+'hundred'
        else:
            return dic[int(t[0])]+'hundredand'+GenNum(int(t[1:3]),nums)
    elif n==1000:
        return 'onethousand'

print(sum([len(GenNum(i,nums)) for i in range(1,1001)]))


