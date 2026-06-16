# 최종 보고서

## 1. 프로그램 주제와 목적

내 프로그램의 주제:환자증상기반 질병진단기

이 프로그램을 만든 이유:환자가 겪고 있는 증상을 기반으로 가장 유사한 질환을 예측하고 진단을 내리려고 만들었다 복잡한 진단 과정을  증상 입력받기 질환 비교 및 판독 환자 기록 저장 및 조회 3가지 단계를 거쳐서 실행하도록만들었다


---

## 2. 문제 분해 및 모델링

### 입력 환자의 증상을 입력받는다


### 처리


### 출력


---

## 3. 사용한 2차원 리스트 설명

2차원 리스트 이름:diseases = [

["감기", ["기침", "인후통", "두통"]],

["독감", ["발열", "기침", "두통"]],

["코로나", ["발열", "기침", "호흡곤란"]],

["편도염", ["인후통", "발열"]]

]

한 행의 의미:질병과 그질병의 증상들

각 열의 의미:0번열 질병이름 1번열 해당질병의 주요증상들

| 열 번호 | 의미 | 실제 예시 |
|---:|---|---|
| 0번 열 |  |  |
| 1번 열 |  |  |
| 2번 열 |  |  |
| 3번 열 |  |  |

이 2차원 리스트를 사용한 이유:진간기준이 필요했고 환자의 증상과 질병의 진단의 일치를 판단해서 점수를 매기기위해


---

## 4. 함수 설명

| 함수 이름 | 역할 | 입력값 | 반환값 또는 출력 |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

가장 중요한 함수 하나를 골라 자세히 설명하세요.

함수 이름:def diagnose(symptoms)

설명:최고 점수를 0으로 두고 시작한다
바깥쪽 for문으로 diseases 리스트에서 질환을 하나씩 꺼내고 안쪽 for문으로 환자가 가진 증상이 그 질환의 증상 목록에 있는지 확인하여 일치할 때마다 score를 1점씩 올린다
만약 이번 질환의 점수가 기존 max_score보다 크면 유력한 질환을 교체한다 모든 검사가 끝난 후 점수가 모두 0점이면 예외 처리로 판단 불가를 반환하고 그렇지 않으면 가장 점수가 높은 질환명을 반환한다


---

## 5. 조건문과 반복문 활용

### 조건문 사용 부분

어떤 조건을 검사했는가?
if max_score==0에서 
모든 질환을 다 검사했는데도 최고 점수가 0점인지 일치하는 증상이 단 하나도 없는 예외 상황인지 판단하고 참이라면 판단 불가를 반환한다

### 반복문 사용 부분

무엇을 반복 처리했는가?
for symptom in symptoms에서
리스트에 있는 질환을 하나씩 꺼내어 순서대로 검사하는 과정을 반복했다

### 조건문과 반복문이 함께 작동한 부분
for symptom in symptoms: 
    if symptom in disease[1]:
        score += 1

---

## 6. 실행 결과

대표 실행 결과를 붙여넣으세요.

```text

```1. 환자 등록
2. 기록 조회
3. 종료
선택: 1
환자번호: 1
증상이 있으면 y 입력, 없으면 n 입력
발열: n
기침: y
인후통: n
두통: n
호흡곤란: n

결과 분석:
판독결과
이름:1
예상질환:감기
---

## 7. 테스트와 오류 수정

### 테스트 1: 정상 사례

입력:선택: 1
환자번호: 1
증상이 있으면 y 입력, 없으면 n 입력
발열: n
기침: y
인후통: n
두통: n
호흡곤란: n

예상 결과:환자번호1
예상질환:감기

실제 결과:환자번호1 예상질환:감기


### 테스트 2: 예외 또는 경계 사례

입력:선택: 1
환자번호: 1
증상이 있으면 y 입력, 없으면 n 입력
발열: n
기침: n
인후통: n
두통: n
호흡곤란: n

예상 결과:

실제 결과:


### 발견한 오류와 수정한 방법

모든증상에 n을 입력해서 최종점수가0일때 판단불가를 반환

---

## 8. Gemini 활용 내용 요약

Gemini에게 도움받은 부분:


Gemini가 제안했지만 내가 수정하거나 사용하지 않은 부분:


최종 코드에서 내가 직접 판단하거나 수정한 부분:


---

## 9. 한계와 개선 방안

현재 프로그램의 한계:증상의 중요도 설정을 안해놔서 진단할때 결정적인 핵심증상과 일반증상을 구체적으로 구분할수없음


다시 개선한다면 추가하고 싶은 기능:disease리스트에서 증상옆에 중요도점수를 함께 저장하고 일치할때 이 가중치를 더하는 기능을 넣고싶다


---

## 10. 코드인터뷰 준비

다음 질문에 답할 수 있도록 준비하세요.

1. 내 프로그램의 입력-처리-출력은 무엇인가?
2. 2차원 리스트에서 한 행과 각 열은 무엇을 의미하는가?
3. 가장 중요한 함수는 무엇이고 어떤 역할을 하는가?
4. 조건문과 반복문은 어디에서 사용되었는가?
5. Gemini가 도와준 부분과 내가 직접 수정한 부분은 무엇인가?


diseases = [
    ["감기", ["기침", "인후통", "두통"]],
    ["독감", ["발열", "기침", "두통"]],
    ["코로나", ["발열", "기침", "호흡곤란"]],
    ["편도염", ["인후통", "발열"]]
]

patients = []


def input_symptoms():
    symptoms = []

    print("증상이 있으면 y 입력, 없으면 n 입력")

    answer = input("발열: ")
    if answer == "y" or answer == "Y":
        symptoms.append("발열")

    answer = input("기침: ")
    if answer == "y" or answer == "Y":
        symptoms.append("기침")

    answer = input("인후통: ")
    if answer == "y" or answer == "Y":
        symptoms.append("인후통")

    answer = input("두통: ")
    if answer == "y" or answer == "Y":
        symptoms.append("두통")

    answer = input("호흡곤란: ")
    if answer == "y" or answer == "Y":
        symptoms.append("호흡곤란")

    return symptoms


def diagnose(symptoms):
    best_disease = ""
    max_score = 0

    for disease in diseases:
        score = 0

        for symptom in symptoms:
            if symptom in disease[1]:
                score += 1

        if score > max_score:
            max_score = score
            best_disease = disease[0]

    # 일치하는 증상이 하나도 없는 경우
    if max_score == 0:
        return "판단 불가"

    return best_disease


def add_patient():
    name = input("환자번호: ")

    symptoms = input_symptoms()

    result = diagnose(symptoms)

    patients.append([name, symptoms, result])

    print()
    print("===== 판독 결과 =====")
    print("이름:", name)
    print("예상 질환:", result)


def view_patients():
    print()
    print("===== 환자 기록 =====")

    if len(patients) == 0:
        print("기록이 없습니다.")
        return

    for patient in patients:
        print("이름:", patient[0])

        print("증상:", end=" ")
        for symptom in patient[1]:
            print(symptom, end=" ")
        print()

        print("예상 질환:", patient[2])
        print("------------------")


while True:
    print()
    print("1. 환자 등록")
    print("2. 기록 조회")
    print("3. 종료")

    menu = input("선택: ")

    if menu == "1":
        add_patient()

    elif menu == "2":
        view_patients()

    elif menu == "3":
        print("프로그램 종료")
        break

    else:
        print("잘못 입력했습니다.")