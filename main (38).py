while True:
	
	def is_year_leap(x):
		
		if x%4 == 0:
			if x%400 == 0:
				print('Високостный')
			elif x%100 != 0:
				print('Високостный')
			else:
				print('Не Високостный')
		else:
			print('Не Високостный') 
			
	is_year_leap(int(input('Введите год: ')))
