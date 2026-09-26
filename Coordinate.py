import math
while True:
	print('0 - Выход')
	print('1 — Перевод градусов, минут и секунд в десятичные градусы')
	print('2 — Перевод десятичных градусов в минуты и секунды')
	print('3 — Перевод геодезических координат в прямоугольные')
	print('4 — Перевод прямоугольных координат в геодезические')
	print('5 — Объяснение прямоугольных координат')
	print('6 — Поиск сближения меридианов')
	print('7 — Пересчет азимутов и дирекционного угла')
	print('8 — Пересчет магнитного склонения на нужный год')
	print('9 — Прямая геодезическая задача')
	print('10 — Обратная геодезическая задача')
	print('11 — Определение номенклатуры по координатам')
	print('12 — Определение координат углов по номенклатуре')

	mode = input('Выберите режим:')

	if mode == '0':
		break

	if mode not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'):
		print('Такого режима пока нет')
		continue

	if mode == '1':

		degrees = float(input('Введите градусы:'))
		minutes = float(input('Введите минуты:'))
		seconds = float(input('Введите секунды:'))
		sign = input('Если полушарие северное/восточное, введите +, если южное/западное,то -')

		if degrees >= 0 and 0 <= minutes < 60 and 0 <= seconds < 60 and sign in ('+', "-"):
			decimal_degrees = degrees + minutes/60 + seconds/3600
		else:
			print('Ошибка. Проверьте корректность данных.')
			continue

		if sign == '-':
			decimal_degrees = -decimal_degrees

		print(round(decimal_degrees, 6))

	if mode == '2':
		decimal_degrees = float(input('Введите угол в десятичных градусах:'))

		angle = abs(decimal_degrees)
		degrees = int(angle)
		minutes_decimal = (angle - degrees) * 60
		minutes = int(minutes_decimal)
		seconds_decimal = (minutes_decimal - minutes) * 60
		seconds = round(seconds_decimal)

		if seconds == 60:
			seconds = 0
			minutes = minutes + 1

		if minutes == 60:
			minutes = 0
			degrees = degrees + 1

		if decimal_degrees > 0:
			direction = 'северной широты / восточной долготы'
		else:
			direction = 'южной широты / западной долготы'

		print(degrees, '°', minutes, "'", seconds, '"', direction)

	if mode == '3':
		B = float(input('Введите геодезическую широту B в десятичных градусах:'))
		L = float(input('Введите географическую долготу L в десятичных градусах:'))

		if not (-90 < B < 90):
			print('Ошибка: широта должна быть между -90° и 90°, без полюсов.')
			continue

		if not (-180 <= L <= 180):
			print('Ошибка: долгота должна быть от -180° до 180°.')
			continue

		X = round(B * 111000)

		if L < 0:
			L = L + 360

		print('Координата Х приближенно равна ', X, 'м')

		n = int(L / 6) + 1
		L0 = 6 * n - 3

		Y = round(n * 1000000 + 500000 + (L - L0) * 111000 * math.cos(math.radians(B)))

		print('Координата Y приближенно равна', Y, 'м')

	if mode == '4':
		X = float(input('Введите координату Х (в метрах):'))
		Y = float(input('Введите координату Y (в метрах):'))

		B = X / 111000

		if B < 0:
			lat = 'ю.ш.'
		else:
			lat = 'с.ш.'

		print('Широта B приближенно равна', round(abs(B), 6), '°', lat)

		n = int(Y / 1000000)
		L0 = 6 * n - 3
		offset = Y - n * 1000000 - 500000

		L = L0 + offset / (111000 * math.cos(math.radians(B)))

		if L > 180:
			L = L - 360

		if L < 0:
			longi = 'з.д.'
		else:
			longi = 'в.д.'

		print('Долгота L приближенно равна', round(abs(L), 6), '°', longi)

	if mode == '5':
		X = float(input('Введите координату Х (в метрах):'))
		Y = float(input('Введите координату Y (в метрах):'))

		X_km = abs(X / 1000)

		print('Расстояние от экватора составляет', round(X_km, 3), 'км')

		n = int(Y / 1000000)

		print('Номер зоны — ', n)

		Y_zone = Y - n * 1000000

		print('Y внутри зоны —', round(Y_zone / 1000, 3), 'км')

		offset = Y_zone - 500000

		if offset < 0:
			direction = 'западнее осевого меридиана'
		elif offset > 0:
			direction = 'восточнее осевого меридиана'
		else:
			direction = '(на осевом меридиане)'

		distance = abs(offset) / 1000

		print('Расстояние от осевого меридиана — ', round(distance, 3), 'км', direction)

	if mode == '6':
		B = float(input('Введите геодезическую широту B в десятичных градусах:'))
		L = float(input('Введите географическую долготу L в десятичных градусах:'))

		if not (-90 < B < 90):
			print('Ошибка: широта должна быть между -90° и 90°, без полюсов.')
			continue

		if not (-180 <= L <= 180):
			print('Ошибка: долгота должна быть от -180° до 180°.')
			continue

		if L < 0:
			L = L + 360

		n = int(L // 6) + 1
		L0 = 6 * n - 3

		L1 = L0
		if L0 > 180:
			L1 = abs(L0 - 360)
			direction = 'з.д.'

		else:
			L1 = L0
			direction = 'в.д.'

		gamma = (L - L0) * math.sin(math.radians(B))

		if gamma < 0:
			sign = '—'
		else:
			sign = ''

		gamma = abs(gamma)
		degrees = int(gamma)
		minutes_decimal = (gamma - degrees) * 60
		minutes = int(minutes_decimal)
		seconds_decimal = (minutes_decimal - minutes) * 60
		seconds = round(seconds_decimal)
		if seconds == 60:
			seconds = 0
			minutes = minutes + 1

		if minutes == 60:
			minutes = 0
			degrees = degrees + 1

		print('Номер зоны — ', n)
		print('Осевой меридиан — ', L0, '°', '(', L1, '°', direction, ')')
		print('Сближение меридианов 𝛄 —', sign, degrees, '°', minutes, "'", seconds, '"')

	if mode == '7':
		print('Выберите известный угол:')
		print('1 — Известен истинный азимут Aи')
		print('2 — Известен магнитный азимут Ам')
		print('3 — Известен дирекционный угол ⍺')

		angle_type = input('Выберите, что у вас известно:')
		if angle_type not in ('1', '2', '3'):
			print('Такого варианта нет')
			break

		angle = float(input('Введите изветное значение:'))
		gamma_sign = input('Введите знак сближения меридианов γ (+ или -):')
		gamma_degrees = float(input('Введите градус γ (без знака):'))
		gamma_minutes = float(input('Введите минуты γ:'))
		gamma_seconds = float(input('Введите секунды γ:'))

		D_sign = input('Введите знак магнитного склонения (+ или -):')
		D_degrees = float(input('Введите градус D (без знака):'))
		D_minutes = float(input('Введите минуты D:'))
		D_seconds = float(input('Введите секунды D:'))

		gamma = gamma_degrees + gamma_minutes / 60 + gamma_seconds / 3600
		D = D_degrees + D_minutes / 60 + D_seconds / 3600

		if gamma_sign == '-':
			gamma = -gamma

		if D_sign == '-':
			D = -D

		if angle_type == '1':
			A = angle
		if angle_type == '2':
			A = angle + D 
		if angle_type == '3':
			A = angle + gamma

		A = A % 360
		Am = (A - D) % 360
		alpha = (A - gamma) % 360

		for name, value in (
			('Истинный азимут Аи:', A),
			('Магнитный азимут Ам:', Am),
			('Дирекционный угол ⍺:', alpha)
		):
			total_seconds = round(value * 3600) % (360 * 3600)

			degrees = total_seconds // 3600
			minutes = (total_seconds % 3600) // 60
			seconds = total_seconds % 60

			print(f'{name}: {round(value, 6)}° = {degrees}° {minutes}′ {seconds}"')

	if mode == '8':
		map_year = int(input('Введите номер года, для которого указано склонение:'))
		target_year = int(input('Введите, на какой год пересчитать:'))

		D_sign = input('Введите знак исходного склонения ( + - восточное, — - западное):')
		D_degrees = int(input('Введите градусы без знака:'))
		D_minutes = int(input('Введите минуты:'))
		D_seconds = float(input('Введите секунды:'))

		ch_sign = input('Введите знак годового изменения склонения ( + - восточное, — - западное):')
		ch_minutes = int(input('Введите минуты годового изменения склонения без знака:'))
		ch_seconds = float(input('Введите секунды годового изменения склонения:'))

		D = D_degrees + D_minutes / 60 + D_seconds / 3600
		ch = ch_minutes / 60 + ch_seconds / 3600

		if D_sign == '-':
			D = -D

		if ch_sign == '-':
			ch = -ch

		years = target_year - map_year
		D_new = D + years * ch 

		if D_new > 0:
			direction = 'восточное'
			sign = ''

		elif D_new < 0:
			direction = 'западное'
			sign = '—'

		else:
			direction = 'нулевое'
			sign = ''

		total_seconds = round(abs(D_new) * 3600)

		degrees = total_seconds // 3600
		minutes = (total_seconds % 3600) // 60
		seconds = total_seconds % 60

		print(years, 'лет прошло')
		print('Приближенное склонение на ', target_year, 'составляет:')
		print(f'{round(D_new, 6)}° = {sign}{degrees}° {minutes}′ {seconds}", {direction}')

	if mode == '9':
		X = float(input('Введите координату Х точки:'))
		Y = float(input('Введите координату Y точки:'))
		angle = float(input('Введите дирекционный угол:'))
		S = float(input('Введите расстояние между двумя точками:'))
		true_angle = math.radians(angle)

		dX = S * math.cos(true_angle)
		dY = S * math.sin(true_angle)

		X2 = int(X + dX)
		Y2 = int(Y + dY)

		print('Координаты второй точки составляют:', X2, 'м', Y2, 'м')

	if mode == '10':
		X1 = float(input('Введите координату Х первой точки:'))
		Y1 = float(input('Введите координату Y первой точки:'))
		X2 = float(input('Введите координату Х второй точки:'))
		Y2 = float(input('Введите координату Y второй точки:'))

		X = abs(X1 - X2)
		Y = abs(Y1 - Y2)

		S = math.sqrt( X ** 2 + Y ** 2)

		print('Расстояние между точками равно', round(S, 6))

		dX = X2 - X1
		dY = Y2 - Y1

		angle = math.degrees(math.atan2(dY, dX)) % 360

		print('Дирекционный угол составляет', round(angle, 6), '°')

	if mode == '11':
		print('Введите широту B:')
		B_text = input('Введите градусы (южная широта со знаком -): ').strip()
		B_degrees = abs(int(B_text))
		B_minutes = int(input('Введите минуты: '))
		B_seconds = float(input('Введите секунды: ').replace(',', '.'))

		print('Введите долготу L:')
		L_text = input('Введите градусы (западная долгота со знаком -): ').strip()
		L_degrees = abs(int(L_text))
		L_minutes = int(input('Введите минуты: '))
		L_seconds = float(input('Введите секунды: ').replace(',', '.'))

		B = B_degrees + B_minutes / 60 + B_seconds / 3600
		L = L_degrees + L_minutes / 60 + L_seconds / 3600

		if B_text.startswith('-'):
			B = -B

		if L_text.startswith('-'):
			L = -L
		longitude_seconds = (
			round(L * 3600, 6) + 180 * 3600
		) % (360 * 3600)

		latitude_seconds = abs(round(B * 3600, 6))

		if latitude_seconds >= 88 * 3600:
			if B < 0:
				letter = 'z'
			else:
				letter = 'Z'

			print('1:1 000 000 —', letter)
			print('Остальные масштабы: полярная разграфка не реализована.')

		else:
			letters = 'ABCDEFGHIJKLMNOPQRSTUV'

			belt = int(latitude_seconds // 14400)
			letter = letters[belt]

			if B < 0:
				letter = letter.lower()

			latitude_offset = latitude_seconds - belt * 14400

			upper_letters = 'АБВГ'
			lower_letters = 'абвг'

			roman_numbers = (
				'I', 'II', 'III', 'IV', 'V', 'VI',
				'VII', 'VIII', 'IX', 'X', 'XI', 'XII',
				'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII',
				'XIX', 'XX', 'XXI', 'XXII', 'XXIII', 'XXIV',
				'XXV', 'XXVI', 'XXVII', 'XXVIII', 'XXIX', 'XXX',
				'XXXI', 'XXXII', 'XXXIII', 'XXXIV', 'XXXV', 'XXXVI'
			)

			scales = (
				(1000000, 1),
				(500000, 2),
				(200000, 6),
				(100000, 12),
				(50000, 24),
				(25000, 48),
				(10000, 96)
			)

			for scale, parts in scales:
				scale_text = f'{scale:,}'.replace(',', ' ')

				if latitude_seconds >= 84 * 3600 and scale != 1000000:
					print(f'1:{scale_text} — полярная разграфка не реализована')
					continue

				height = 14400 // parts
				width = 21600 // parts

				position = int(latitude_offset // height)

				if B >= 0:
					row = parts - 1 - position
				else:
					row = position

				global_column = int(longitude_seconds // width)

				if latitude_seconds < 60 * 3600:
					group_size = 1
				elif latitude_seconds < 76 * 3600:
					group_size = 2
				elif scale == 200000:
					group_size = 3
				else:
					group_size = 4

				first_column = (
					global_column // group_size
				) * group_size

				names = []

				for current_column in range(
					first_column, first_column + group_size
				):

					column = current_column // parts + 1

					local_column = current_column % parts

					name = f'{letter}-{column}'

					if scale == 500000:
						index = row * 2 + local_column
						name += '-' + upper_letters[index]

					elif scale == 200000:
						index = row * 6 + local_column
						name += '-' + roman_numbers[index]

					elif scale <= 100000:
						factor = parts // 12

						row_100 = row // factor
						column_100 = local_column // factor

						number_100 = row_100 * 12 + column_100 + 1
						name += f'-{number_100}'

						if scale <= 50000:
							step = factor // 2

							row_50 = (row // step) % 2
							column_50 = (local_column // step) % 2

							index = row_50 * 2 + column_50
							name += '-' + upper_letters[index]

						if scale <= 25000:
							step = factor // 4

							row_25 = (row // step) % 2
							column_25 = (local_column // step) % 2

							index = row_25 * 2 + column_25
							name += '-' + lower_letters[index]

						if scale == 10000:
							row_10 = row % 2
							column_10 = local_column % 2

							number_10 = row_10 * 2 + column_10 + 1
							name += f'-{number_10}'

					names.append(name)

				nomenclature = ' + '.join(names)

				if group_size == 1:
					print(f'1:{scale_text} — {nomenclature}')
				else:
					print(
						f'1:{scale_text} — {nomenclature}'
						' (состав объединённого листа)'
					)

	if mode == '12':
		letter = input('Введите букву миллионного листа:').strip()
		column = int(input('Введите номер колонны:'))

		print('1 — 1:1 000 000')
		print('2 — 1:500 000')
		print('3 — 1:200 000')
		print('4 — 1:100 000')
		print('5 — 1:50 000')
		print('6 — 1:25 000')
		print('7 — 1:10 000')

		scale = input('Выберите масштаб: ').strip()

		if scale not in ('1', '2', '3', '4', '5', '6', '7'):
			print('Такого масштаба нет.')
			input('Нажмите Enter, чтобы вернуться в меню')
			continue

		letters = 'ABCDEFGHIJKLMNOPQRSTUV'
		belt = letters.index(letter.upper()) + 1

		dB = 4
		dL = 6

		if letter.islower():
			B_north = -(belt - 1) * dB
		else:
			B_north = belt * dB

		L_west = -180 + (column - 1) * dL

		if scale == '1':
			B_south = B_north - dB
			L_east = L_west + dL

		if scale == '2':
			part = input('Введите букву листа А, Б, В или Г: ').strip().upper()

			dB = 2
			dL = 3

			if part in ('В', 'Г'):
				B_north = B_north - dB

			if part in ('Б', 'Г'):
				L_west = L_west + dL

		if scale == '3':
			roman_numbers = (
				'I', 'II', 'III', 'IV', 'V', 'VI',
				'VII', 'VIII', 'IX', 'X', 'XI', 'XII',
				'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII',
				'XIX', 'XX', 'XXI', 'XXII', 'XXIII', 'XXIV',
				'XXV', 'XXVI', 'XXVII', 'XXVIII', 'XXIX', 'XXX',
				'XXXI', 'XXXII', 'XXXIII', 'XXXIV', 'XXXV', 'XXXVI'
			)

			part = input('Введите римский номер листа, например XVII: ').strip().upper()
			index = roman_numbers.index(part)

			dB = 40 / 60
			dL = 1

			row = index // 6
			col = index % 6

			B_north = B_north - row * dB
			L_west = L_west + col * dL

		if scale in ('4', '5', '6', '7'):
			number = int(input('Введите номер стотысячного листа от 1 до 144: '))

			dB = 20 / 60
			dL = 30 / 60

			index = number - 1

			row = index // 12
			col = index % 12

			B_north = B_north - row * dB
			L_west = L_west + col * dL

		if scale in ('5', '6', '7'):
			part = input('Введите букву пятидесятитысячного листа А, Б, В или Г: ').strip().upper()

			dB = 10 / 60
			dL = 15 / 60

			if part in ('В', 'Г'):
				B_north = B_north - dB

			if part in ('Б', 'Г'):
				L_west = L_west + dL

		if scale in ('6', '7'):
			part = input('Введите букву двадцатипятитысячного листа а, б, в или г: ').strip().lower()

			dB = 5 / 60
			dL = 7 / 60 + 30 / 3600

			if part in ('в', 'г'):
				B_north = B_north - dB

			if part in ('б', 'г'):
				L_west = L_west + dL

		if scale == '7':
			part = input('Введите номер десятитысячного листа от 1 до 4: ').strip()

			dB = 2 / 60 + 30 / 3600
			dL = 3 / 60 + 45 / 3600

			if part in ('3', '4'):
				B_north = B_north - dB

			if part in ('2', '4'):
				L_west = L_west + dL

		B_south = B_north - dB
		L_east = L_west + dL

		for name, B_corner, L_corner in (
			('СЗ', B_north, L_west),
			('СВ', B_north, L_east),
			('ЮЗ', B_south, L_west),
			('ЮВ', B_south, L_east)
		):
			B_total = round(abs(B_corner) * 3600)

			B_degrees = B_total // 3600
			B_minutes = (B_total % 3600) // 60
			B_seconds = B_total % 60

			L_total = round(abs(L_corner) * 3600)

			L_degrees = L_total // 3600
			L_minutes = (L_total % 3600) // 60
			L_seconds = L_total % 60

			if B_corner > 0:
				lat = 'с. ш.'
			elif B_corner < 0:
				lat = 'ю. ш.'
			else:
				lat = ''

			if L_corner > 0:
				lon = 'в. д.'
			elif L_corner < 0:
				lon = 'з. д.'
			else:
				lon = ''

			print(name, 'угол:')
			print(f'B = {B_degrees}° {B_minutes}′ {B_seconds}″ {lat}')
			print(f'L = {L_degrees}° {L_minutes}′ {L_seconds}″ {lon}')
			print()

	input('Нажмите Enter, чтобы вернуться в меню')