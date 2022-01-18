#learnning programming

height=int(input('height='))
weight=int(input('weight='))

bmi=weight/(height*height)

if bmi<=18.5:
    t='过轻'
elif bmi>18.5 and bmi<=25:
    t='正常'
elif bmi>25 and bmi<=28:
    t='过重'
elif bmi>28:
    t='肥胖'

print('您的BMI是%d,体重情况是%s' %(bmi,t))
