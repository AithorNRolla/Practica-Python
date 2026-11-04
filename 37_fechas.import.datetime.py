import datetime as dt #asignamos el DT a todo. 
print(F"fecha de hoy: {dt.datetime.date.today()}")
print(F"hora actual: {dt.datetime.datetime.now()}") #esto lo he sacado con IA. 
f_posterior=dt.datetime.datetime.now()+datetime.timedelta(days=20,hours=60)

print(f_posterior)

fechahora_actual=datetime.datetime.now()
print(f"La fecha y hora actuales {datetime.datetime.strftime(fechahora_actual,"%d/%m/%Y - %H:%M")}")

fecha1="10/11/2003"
fecha2="25/04/2002"
fecha1=dt.datetime.strptime(fecha1,"%d/%m/%Y")
fecha2=dt.datetime.strptime(fecha2,"%d/%m/%Y")

if fecha1<fecha2:
    print(f"La más antigua es {fecha1}")
else:
    print(f"La más antigua es {fecha2}"