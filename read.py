data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
			# 每一千筆才印一次留言
print('檔案讀取完成，總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d)
	# print(sum_len)
print('每筆留言的平均長度是', sum_len / len(data))

new = [d for d in data if len(d) < 100]
print('一共有', len(new) , '筆留言長度小於100')

good = [d for d in data if 'good' in d]
print('一共有', len(good) , '筆留言提到good')

bad = ['good' in d for d in data]
print(bad)