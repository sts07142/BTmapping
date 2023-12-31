import pandas as pd

# 텍스트 파일 읽기
data = []
with open(r'BTmapping\2023_09_23_09_02_19.txt', 'r') as file:
    for line in file:
        line = line.strip().split(',')
        data.append(line)

# 데이터를 DataFrame으로 변환
df = pd.DataFrame(data, columns=["frameId", "objectId", "bboxX", "bboxY", "bboxW", "bboxH", "score", "currentTime", "-", "-"])

# objectId를 숫자로 변환
df['objectId'] = df['objectId'].astype(int)

# currentTime 열을 datetime 형식으로 변환
df['currentTime'] = pd.to_datetime(df['currentTime'])

# 각 objectId에 대한 가장 처음 currentTime과 가장 마지막 currentTime 출력
first_last_times = df.groupby('objectId')['currentTime'].agg(['first', 'last']).reset_index()

# last - first가 5초 이상인 레코드만 선택
first_last_times['duration'] = (first_last_times['last'] - first_last_times['first']).dt.total_seconds()
first_last_times = first_last_times[first_last_times['duration'] >= 5]

# last가 빠르고 first가 느린 순으로 정렬
first_last_times = first_last_times.sort_values(by=['objectId'], ascending=[True])

# duration 열을 삭제
first_last_times = first_last_times.drop(columns=['duration'])

# 정렬된 데이터를 'first_last_times.csv' 파일에 저장
first_last_times.to_csv('./BTmapping/transMOT.txt', index=False)

print(first_last_times)
