from Neis_API import Region, mealInfo
import warnings

def check_meal(time, date):
    if time == '아침':
        try:
            print()
            print(f'------{date[0:4]}년{date[4:6]}월{date[6:8]}일 아침 급식식단------')
            print()
            print(data[0].dish_name)
        except:
            print()
            print('급식 자료가 존재하지 않습니다.')
    elif time == '점심':
        try:
            print()
            print(f'------{date[0:4]}년{date[4:6]}월{date[6:8]}일 점심 급식식단------')
            print()
            print(data[1].dish_name)
        except:
            print()
            print('급식 자료가 존재하지 않습니다.')
    elif time == '저녁':
        try:
            print()
            print(f'------{date[0:4]}년{date[4:6]}월{date[6:8]}일 저녁 급식식단------')
            print()
            print(data[2].dish_name)
        except:
            print()
            print('급식 자료가 존재하지 않습니다.')
print('---------------Made by busi---------------')
print('목포홍일고등학교 급식식단 알림도우미입니다.')
print('깃허브에서 도움말을 읽고 사용해주시길 바랍니다.')
print()
warnings.filterwarnings(action='ignore')
try:
    print()
    date_= int(input('급식을 확인할 날짜를 입력하세요 EX)20230727 = 2023년07월27일: '))
    data = mealInfo.get_meal_data(region_code=Region.JEONNAM,
                                    school_code="8490087",
                                    date=date_)
except:
    print()
    print('올바르지 않은 값입니다.')
else:
    if len(str(date_)) != 8:
        print()
        print('올바르지 않은 값입니다.')
    else:
        try:
            print()
            time = str(input('확인할 급식을 입력해주세요(아침, 점심, 저녁): '))
        except:
            print()
            print('올바르지 않은 값입니다.')
        else:
            check_meal(time, str(date_))
print()
print('Made by busi')
print('문의하기 - https://litt.ly/busi')
