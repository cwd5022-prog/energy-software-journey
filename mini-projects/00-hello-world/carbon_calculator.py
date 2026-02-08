#간단한 탄소배출 계산기 
EMISSiON_FACTORS = 0.4594 #전력 1kwh당 발생하는 탄소량(kg)

print("=" * 30)
print(" 탄소 배출 계산기 (Energy SW) ")
print("=" * 30)

try: 
    kwh = float(input("사용한 전력량(kWh)을 입력하세요: "))
    co2 = kwh * EMISSiON_FACTORS
    trees = co2/6.6 #소나무 한 그루가 여간 흡수하는 양(약 6.6kg)으로 환산

    print(f"\n 예상 탄소 배출량: {co2:.2f} kg CO2")
    print(f"소나무 {trees:.1f}그루가 1년간 흡수해야하는 양입니다.")
except ValueError:
    print("유효한 숫자를 입력해주세요.")