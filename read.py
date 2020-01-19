data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))

print('檔案讀取完成，總共有', len(data), "筆資料")

sum_len = 0
for d in data:
    sum_len += len(d) 
print("平均每筆留言有", sum_len / len(data), "個字數")

new = []
for d in data:
    if len(d) <= 150:
        new.append(d)
print('共有', len(new), '筆留言少於150個字')

good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('共有', len(good), '筆留言包含good字眼')

wc = {}
for d in data:
    words = d.split()
    for word in words:
        if word in wc:
            wc[word] +=1 
        else:
            wc[word] = 1

for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])

print(len(wc))

while True:
    word = input('欲查詢內容： ')
    if word == 'q':
        print('感謝使用此搜尋功能')
        break
    if word in wc:
        print(word, '出現過的字數為', wc[word])
    else:
        print('查無', word, '的相關資料')