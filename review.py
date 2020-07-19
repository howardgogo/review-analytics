data = []
count = 0
with open('reviews.txt', 'r')as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
		    print(len(data))
print('檔案讀完了，共有', len(line), '筆資料')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)

print('留言平均長度為', sum_len / len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)

print('字數小於100的留言共有', len(new), '筆')
print(new[3])


