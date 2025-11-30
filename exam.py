def check_exam_status(score):
    if score >= 50:
        print("Result: Passed! :)")
    else:
        print("Result: Failed :(")

exam_score = float(input("Enter your exam score: "))

check_exam_status(exam_score)