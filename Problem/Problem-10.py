tomp = int(input("수온을 입력해주세요: "))
if tomp >= 100:
    print("수온이 100도 이상입니다(물이 기체상태 입니다)")
elif tomp >= 0:
    print("수온이 0도 이상입니다(물이 액체상태 입니다)")
else:
    print("수온이 0도 미만입니다(물이 고체상태 입니다)")