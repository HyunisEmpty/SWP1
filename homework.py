
year = int(input("몇년도인지 입력해주세요 :"))
month = int(input("몇월인지 입력해주세요 :"))
day = int(input("몇일인지 입력해주세요 :"))
print("찾고 있으신 날짜는",year,"년",month,"월",day,"일 입니다.")
day -= 1 # 1년 1월 1일 은 0일지난 시점이다. 그렇기에 1을 빼야 한다.

#sum_day에 1년 부터yaer-1년 까지의 총일수가 저장됨
sum_day = 0
for num_year in range(1,year):
    if (num_year % 400 == 0) or ((num_year % 4 == 0) and (not (num_year % 100 == 0))):
        sum_day += 366
    else:
        sum_day += 365

yun = 0
if (year % 400 == 0) or ((year % 4 == 0) and (not(year % 100 == 0))):
    yun = 1
else:
    yun = 0

i = 1
month_day = 0
while i < month:
    if i == 1:
        month_day +=31
    elif i == 2:
        if yun == 1:
            month_day +=29
        else:
            month_day +=28
    elif i == 3:
        month_day +=31
    elif i == 4:
        month_day +=30
    elif i == 5:
        month_day +=31
    elif i == 6:
        month_day +=30
    elif i == 7:
        month_day +=31
    elif i == 8:
        month_day +=31
    elif i == 9:
        month_day +=30
    elif i == 10:
        month_day +=31
    elif i == 11:
        month_day +=30
    else:
        month_day +=31
    i += 1

all_day = sum_day + month_day + day

if all_day % 7 == 0:
    print("월요일")
elif all_day % 7 == 1:
    print("화요일")
elif all_day % 7 == 2:
    print("수요일")
elif all_day % 7 == 3:
    print("목요일")
elif all_day % 7 == 4:
    print("금요일")
elif all_day % 7 == 5:
    print("토요일")
else :
    print("일요일")

