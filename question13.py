# 사용자에게 입력받기
# 출발시간 (시/분), 도착시간 (시/분), 이동 거리

departure_hour = int(input("출발 시 (시간)을 입력하세요: "))
departure_minute = int(input("출발 시 (분)을 입력하세요: "))
arrival_hour = int(input("도착 시 (시간)을 입력하세요: "))
arrival_minute = int(input("도착 시 (분)을 입력하세요: "))
distance = float(input("이동 거리(km)를 입력하세요: "))

# 이동거리, 출발 시간, 도착시간, 평균속도를 계산하여 출력하고

time = (arrival_hour - departure_hour) + (arrival_minute - departure_minute) / 60
speed = distance / time

print(f"이동 거리: {distance:.1f}km")
print(f"출발 시간: {departure_hour}시 {departure_minute}분")
print(f"도착 시간: {arrival_hour}시 {arrival_minute}분")
print(f"평균 속도: {speed:.2f}km/h")

# 속도 상태를 60km/h 미만 "느림", 90km/h 미만 "보통", 이상이면 "빠름" 분류
speed_status = ""

if speed < 60:
    speed_status = "느림"
elif speed < 90: # 이전 조건이 아닌 경우 이미 speed는 60 이상임을 알 수 있으므로, 60 <= speed는 생략
    speed_status = "보통"
else :
    speed_status = "빠름"
print(f"속도 상태: {speed_status}")