# Координата (Coordinate)

Учебный консольный калькулятор по топографии на Python.
Проект студента географического факультета МГУ.

An educational Python command-line calculator for topography,
developed by a geography student at Moscow State University.
The program interface is in Russian.

## Режимы / Features

| № | Режим | Feature |
|---|---|---|
| 1 | Градусы, минуты, секунды → десятичные градусы | DMS → decimal degrees |
| 2 | Десятичные градусы → градусы, минуты, секунды | Decimal degrees → DMS |
| 3 | Широта и долгота → приближённые X, Y | Latitude/longitude → approximate X, Y |
| 4 | X, Y → приближённые широта и долгота | X, Y → approximate latitude/longitude |
| 5 | Расшифровка прямоугольных координат: зона и смещение от осевого меридиана | Coordinate interpretation: zone and central meridian offset |
| 6 | Приближённое сближение меридианов | Approximate meridian convergence |
| 7 | Пересчёт истинного и магнитного азимутов и дирекционного угла | True, magnetic and grid azimuth conversion |
| 8 | Пересчёт магнитного склонения на заданный год | Magnetic declination adjustment for a target year |
| 9 | Прямая геодезическая задача на плоскости | Forward plane surveying problem |
| 10 | Обратная геодезическая задача на плоскости | Inverse plane surveying problem |
| 11 | Номенклатура по координатам: от 1:1 000 000 до 1:10 000 | Map sheet designation from coordinates |
| 12 | Координаты четырёх углов одинарного листа по номенклатуре | Coordinates of all four corners of a single map sheet |

Режим 0 завершает программу.
Mode 0 exits the program.

## Запуск / Running

Требуется Python 3.6 или новее. Сторонние библиотеки не нужны.
Requires Python 3.6 or later. No third-party packages are needed.

Скачайте проект через Code → Download ZIP и распакуйте архив.
Откройте терминал в папке проекта и выполните:

Download the project via Code → Download ZIP and extract it.
Open a terminal in the project folder and run:

```bash
python3 Coordinate.py
```

В Windows можно использовать / On Windows, you can use:

```bash
py Coordinate.py
```

## Ввод данных / Input

- Для дробных чисел используйте точку: `55.75`.
- Координаты X и Y и расстояния вводятся в метрах.
- В режимах 4 и 5 вводите полный Y с номером зоны.
- Следуйте подсказкам о знаках и единицах измерения.
- В режиме 12 буква пояса — латинская, буквы подразделений АБВГ — русские.
- Маленькая буква пояса обозначает южное полушарие по принятой в проекте convention.

Use a decimal point, enter distances and X/Y coordinates in metres,
and follow the prompts for signs and units.
Modes 4 and 5 require the full Y coordinate including the zone number.
In mode 12, use a Latin latitude-band letter and Cyrillic subdivision
letters. A lowercase band letter denotes the Southern Hemisphere
in this project.

## Ограничения / Limitations

- Режимы 3 и 4 используют учебное приближение через 111 км на градус
  и косинус широты, а не точное преобразование Гаусса — Крюгера.
- Режим 6 использует приближённую формулу сближения меридианов.
- Режим 8 предполагает постоянное годовое изменение склонения,
  введённое пользователем; геомагнитная модель не используется.
- В режиме 11 начиная с 84° по модулю реализован только миллионный масштаб.
- Режим 12 рассчитывает одинарные листы и не учитывает объединение
  листов на высоких широтах; полярные листы Z/z не поддерживаются.
- Обработка ошибочного ввода пока неполная.

Modes 3, 4 and 6 use educational approximations.
Mode 8 applies a user-provided constant annual declination change.
Mode 11 supports only the million-scale sheet at absolute latitudes
of 84° and above. Mode 12 handles single sheets without high-latitude
grouping and does not support polar sheets Z/z.
Input validation is incomplete.
