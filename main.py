##########################################################################
################### Autor: Rubén Gámez Torrijos ##########################
########################### GATORU ACADEMY® ##############################
############################### 2023 #####################################

# Paso 1: Obtener el consumo mensual promedio en kilovatios por hora (kWh)
consumo_mensual = float(input("Ingrese el consumo mensual promedio en kWh: "))

# Paso 2: Obtener la cantidad de horas de luz solar promedio al día
horas_sol = float(input("Ingrese la cantidad de horas de luz solar promedio al día: "))

# Paso 3: Obtener la eficiencia promedio de los paneles solares
eficiencia = float(input("Ingrese la eficiencia promedio de los paneles solares (en %): ")) / 100

# Paso 4: Obtener la potencia de los paneles solares disponibles en el mercado
potencia_panel = float(input("Ingrese la potencia de los paneles solares disponibles en el mercado (en Watts): "))

# Paso 5: Obtener la potencia de la batería en kW (si se selecciona "Si" con baterías)
desea_baterias = input("¿Desea instalar baterías para almacenar energía durante la noche? (si/no): ")

if desea_baterias.lower() == "si":
    potencia_bateria = float(input("Ingrese la potencia de la batería para el horario de noche (en kW): "))
else:
    potencia_bateria = 0.0

# Paso 6: Calcular la potencia necesaria del kit de energía solar considerando la batería
potencia_necesaria = ((consumo_mensual * 1000) / (eficiencia * horas_sol * 30))

# Paso 7: Calcular la cantidad de paneles solares necesarios en el kit
paneles_necesarios = potencia_necesaria / potencia_panel 

# Paso 8: Calcular la cantidad de baterías necesarias para el horario de noche
horas_noche = 24 - horas_sol
consumo_diario = consumo_mensual / 30
potencia_noche = consumo_diario * horas_noche
potencia_noche_conseguida = potencia_noche * (1 - eficiencia)
capacidad_bateria = potencia_bateria * 0.8  # Consideramos que se puede usar el 80% de la capacidad de la batería
baterias_noche = int(potencia_noche_conseguida / capacidad_bateria) # Agregamos 1 batería adicional para tener un margen

# Paso 9: Imprimir el resultado
print("Para un consumo mensual de {:.2f} kWh, se necesita un kit de energía solar con una potencia de al menos {:.2f} kW.".format(consumo_mensual, potencia_necesaria / 1000))
print("Se recomienda adquirir {:.0f} paneles solares de {} Watts para el kit.".format(paneles_necesarios, potencia_panel))
if potencia_bateria > 0:
    print("Se necesitarán {} baterías de {} kW para el horario de noche.".format((baterias_noche), potencia_bateria))
else:
    print("No se requieren baterías para el horario de noche.")
