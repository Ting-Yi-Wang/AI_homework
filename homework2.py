#建立一個名為 `scores` 的列表，包含數字 `85, 90, 78, 65`
#印出第一個數字
#將最後一個數字改為 70
#新增一個數字 `88`
#刪除第二個數字
#印出列表長度

scores = [85, 90, 78, 65]
print(scores[0])
scores[-1] = 70
scores.append(88)
scores.pop(1)
print(len(scores))
print(scores)

##建立一個元組 `coordinates = (3, 6, 9)`
##印出第二個元素
##嘗試修改第一個元素，看看 Python 會發生什麼錯誤？
##嘗試新增一個元素 `12`，看看 Python 會發生什麼錯誤？
coordinates = (3, 6, 9)
print(coordinates[1])
#coordinates[0] = 5
#coordinates.append(12)
print(coordinates)

#建立一個集合 `fruits = {"apple", "banana", "cherry"}`
#新增 `"orange"`
#刪除 `"banana"`
#建立 `set2 = {"banana", "grape", "apple"}`
#找出兩個集合的交集
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
fruits.remove("banana")
set2 = {"banana", "grape", "apple"}
print(fruits & set2)

#建立一個字典：
# student = {"name": "John", "age": 18, "score": 85}
#印出 name
#檢查 gender 是否在字典中
#新增 gender: "male"
#刪除 score
student = {"name": "John", "age": 18, "score": 85}
print(student["name"])
print("gender" in student)
student["gender"] = "male"
student.pop("score")
print(student)


