# AI 활용 자유 주제 파이썬 미니 프로젝트
# 이름 또는 학번:20922 정예동
# 프로젝트 주제:환자증상기반으로 질병진단하기
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