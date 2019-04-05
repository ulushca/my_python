#else 
#input 받기
#A 90이상
#B 80 이상
#C 70 이상
#D 60 이상
#F 60 미만
#i 
flag = 0
while flag == 0:
    score = int(input("your score: "))
    if score >= 90 and score <=100:
        print("your grade: A")

    elif score >= 80 and score < 90:
        print("your grade: B")

    elif score >= 70 and score < 80:
        print("your grade: c")

    elif score >= 60 and score < 70:
        print("your grade: D")

    elif score < 60 and score >= 0:
        print("your grade: F")
    if type !=(int):
        print("Input type Error!")


    else:
        print("Error")
    
    ind = input("Keep going? (y/n): ")
    if ind == "y":
        continue
    elif ind == "n" or ind == "no":
        flag = 1
    else:
        flag = 1

