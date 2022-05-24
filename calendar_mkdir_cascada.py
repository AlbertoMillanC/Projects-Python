import calendar
from pathlib import Path

month = list(calendar.month_name [1:])
day = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
for i,month in enumerate(month):
    for day_name in day:
    
     Path(f'2022/{i+1}.{month}/{day_name}').mkdir(parents=True, exist_ok=True)








       