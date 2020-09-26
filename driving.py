country = input('請問是那個國家:')
age = int(input('請輸入年齡:'))
if country == '台灣':
	if age >= 18 :
		print ('你可以考駕照')
	else :
		print ('你不可以考駕照')
elif country == '美國' :
	if age >= 16 :
		print ('你可以考駕照')
	else :
		print ('你不可以考駕照')
else :
	print ('只能輸入台灣/美國')