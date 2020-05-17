a = input('你认识那个女的吗?')
if a == '认识' or '是':
	b = input('那她是不是单身啊?')
	if b == '是':
		print('你可以追求她')
	else:
		print('放弃')
else:
	pass
###########################
a = input('你认识那个女的吗？')
b = input('她单身吗?')
if a == '认识' and b == '单身':
	print('那你可追求她')
else:
	print('那算了')
