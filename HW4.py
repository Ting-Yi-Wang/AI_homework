#題目一
numbers = [51, 30, 78, 20, 96, 40, 62]
# 印出第 1 個數字、第 3 個數字與最後一個數字
print("題目一答案如下:")
print(numbers[0])  # 第 1 個數字
print(numbers[2])  # 第 3 個數字
print(numbers[-1]) # 最後一個數字
#印出 list 中的最大值與最小值。
print(max(numbers))
print(min(numbers))
#將 list 中的數字由小到大排序後印出。
numbers.sort()
print(numbers)
#計算並印出總和與平均值（平均值保留到小數點第 2 位）
total = sum(numbers)  # 計算總和
average = total / len(numbers)  # 計算平均值
print(f"總和: {total}")
print(f"平均值: {average:.2f}")  # 平均值保留到小數點第 2 位
filtered_numbers = [num for num in numbers if num >= 50]  # 篩選出大於等於 50 的數字
print(filtered_numbers)
#換行
print("\n")
print("題目二答案如下:")
asian_countries = {
    'Taiwan': 'Taipei',
    'Japan': 'Tokyo',
    'South Korea': 'Seoul',
    'Myanmar': 'Yangon',
    'Germany': 'Berlin'
    }
#印出asian_countries
print('舊字典:', asian_countries)
asian_countries['Myanmar'] = 'Naypyidaw'  # 更正 Myanmar 的首都
asian_countries.pop('Germany')  # 移除 Germany
asian_countries['Thailand'] = 'Bangkok'  # 新增 Thailand 及其首都
print('新字典:', asian_countries)
# 將國家按照字母排序，並將排序後的結果指派給變數 sorted_asian_countries
sorted_asian_countries = dict(sorted(asian_countries.items()))
print('排序後新字典:', sorted_asian_countries)

print("\n")
print("題目三答案如下:")
#班上有 4 位學生，他們分別有 3 科的考試成績，資料如下：
scores = {
    "Linda": [85, 90, 78],
    "Richard": [72, 88, 91],
    "Una": [90, 85, 87],
    "Brian": [60, 75, 70]
}
#計算每位學生的平均分數。
average_scores = {name: sum(scores) / len(scores) for name, scores in scores.items()}
print(average_scores)
comments = {}
for name, avg_score in average_scores.items():
    if avg_score >= 85:
        comments[name] = "優秀"
    elif avg_score >= 70:
        comments[name] = "及格"
    else:
        comments[name] = "需加強"

#請印出每位學生的「平均分數」與「評語」
for name, avg_score in average_scores.items():
    print(f"{name} 平均分數: {avg_score:.2f}，評語: {comments[name]}")
# 計算全班的「總平均分數」
class_average = sum(average_scores.values()) / len(average_scores)
print(f"全班總平均分數: {class_average:.2f}")

# 找出「平均分數最高的學生」
highest_student = max(average_scores, key=average_scores.get)
highest_score = average_scores[highest_student]
print(f"平均分數最高的學生: {highest_student}，平均分數: {highest_score:.2f}")
print("\n")
print("題目四答案如下:")
def check_password(password):
    # 檢查長度是否大於 5
    if len(password) <= 5:
        return "INVALID"
    # 檢查是否包含大寫字母、小寫字母、數字，且不包含空白
    if (any(char.isupper() for char in password) and
        any(char.islower() for char in password) and
        any(char.isdigit() for char in password) and
        not any(char.isspace() for char in password)):
        return "Valid Password"
    return "INVALID"
#請使用你的函數印出以下結果
print(check_password("GenAI4Humanities"))
print(check_password("genai4humanities"))
print(check_password("GENAI4HUMANITIES"))
print(check_password("GenAIGenAI"))
print(check_password("GenAI 2025"))
print(check_password("GenAI"))