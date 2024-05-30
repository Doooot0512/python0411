def main():
    scores = []
    
    # 輸入學生成績，直到輸入 -1 為止
    while True:
        score = float(input("請輸入學生成績（輸入 -1 表示結束輸入）："))
        if score == -1:
            break
        scores.append(score)
    
    # 計算全班人數
    total_students = len(scores)
    
    # 計算及格人數
    pass_count = sum(1 for s in scores if s >= 60)
    
    # 計算不及格人數
    fail_count = total_students - pass_count
    
    # 計算全班平均值
    average_score = sum(scores) / total_students if total_students > 0 else 0
    
    # 顯示結果
    print("全班人數：", total_students)
    print("及格人數：", pass_count)
    print("不及格人數：", fail_count)
    print("全班平均值：", average_score)

if __name__ == "__main__":
    main()
