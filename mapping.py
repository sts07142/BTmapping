# 1 = 인재, 2 = 지우, 3 = 정곤, 4 = 지성, 5 = 태경
# 13 = 지성, 14 = 정곤, 16 = 인재, 19 = 지성, 22, 24, 25 = 지성

## 인재 = 1, 16
## 지우 = 2
## 정곤 = 3, 14
## 지성 = 4, 13, 19, 22, 24, 25
## 태경 = 5
### 16, 2, 14, 25, 5

# 

#초기 가정 : 인원을 알고 있다고 가정
#그냥 transMOT.txt에서 ojectId별로 정렬 후, 그 순서대로 인원만큼 블루투스 와 매핑
## 그러면 초기 5명은 1,2,3,4,5에 매핑될것임.
#그 이후 부터 checkBT.txt에 있는 기록을 기준으로 확인하여 판단
## 판단 기준 : rssi가 나갔으면 그냥 나간거지만, rssi는 안에 있는데 id가 사라지면 특수 상황으로 가정.
## 특수상황에서는 이후에 새 id가 탐지되며 다른 인원들 rssi에 큰 변화가 없는 경우
## 기존의 id와 매핑
## 사실 bbox를 통해 검증을 해야하지만 우선적으로 진행하자.....
## 새 id가 탐지되며 rssi가 변화가 있는 경우는 그대로 매핑