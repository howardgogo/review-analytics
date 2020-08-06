

data = []
count = 0
with open('reviews.txt', 'r')as f:
	for line in f:
		data.append(line)
		count += 1
	if count % 1000 == 0:
		print(len(data))
print('檔案讀完了，共有', len(line), '筆資料')
print(data[0])
	


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



good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('留言裡面有good的留言有', len(good), '筆')
print(good[0])
# len清單中元素數量
#good = [d for d in data if 'good' in d]
#print(good) 第一個d是要被加入清單的元素


wc = {}
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1#字典查找東西用 []
		else:
			wc[word] = 1 #新增新的key進字典

			
for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])


print(len(wc))
print(wc['Allen'])

while True:
	word = input('請輸入想找的字: ')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過', wc[word], '次')
	else:
		print('找不到拉')
print('感謝使用')







