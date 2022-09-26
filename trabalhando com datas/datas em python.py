from datetime import datetime, timedelta

# data
hoje = datetime.now()
print(hoje.date())

# variacoes de data
amanha = hoje + timedelta(weeks=1)
print(amanha)

data_contrato = datetime(year=2022, month=9, day=1)
atraso = hoje - data_contrato
print(atraso.days)

# extrair datas em outros formatos
data_contrato = "01/09/2022"
data_contrato = datetime.strptime(data_contrato, "%d/%m/%Y")
print(data_contrato)

# formato brasileiro
print(hoje.strftime("%d/%m/%Y"))
print(hoje.strftime("%A"))

# fuso horario
# hoje = hoje - timedelta(hours=1)
# print(hoje)

import zoneinfo

# print(zoneinfo.available_timezones())
zona = zoneinfo.ZoneInfo('Singapore')
agora_singapore = hoje.astimezone(zona)
print(agora_singapore)
