"""
Uma pessoa sai de casa ás 6:52
anda 1 km em 8 minutos e 15 segundos
anda 3km em 7 minutos e 12 segundos
anda 1 km em 8 minutos e 15 segundos


que horas ela chega no café da manhã?

"""
km1 = 8 + 15/60
km3 = (7 + 12/60)*3


minutos = km1+km3+km1

hora = minutos/60


print(minutos,"Minutos")
print(hora,"horas")

hora6 = 6*60 + 52

chegada = hora6 + minutos

print(chegada)
