def main():
    scores = []
    
    while True:
        score = float(input("請輸入學生成績（輸入 -1 表示結束輸入）："))
        
        if score == -1:
            break  # 結束輸入
        
        scores.append(score)
    
    total_students = len(scores)
    pass_count = 0
    
    for s in scores:
        if s >= 60:
            pass_count += 1
        else:
            continue  # 如果不及格，跳過這個迴圈
        
    fail_count = total_students - pass_count
    average_score = sum(scores) / total_students if total_students > 0 else 0
    
    print("全班人數：", total_students)
    print("及格人數：", pass_count)
    print("不及格人數：", fail_count)
    print("全班平均值：", average_score)

if __name__ == "__main__":
    main()

