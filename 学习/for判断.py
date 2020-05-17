name = ['金学庭','潘惠瑜','金灿阳','金菊友','张丽娟']
print('我的家庭表:')
for a in name:
	print(a)
b = 0
for b in range(0,30):
	b = b+1
	print(name[1]+'去了福建,'+name[0]+'思念'+name[1]+'的第{}天.'.format(b))
