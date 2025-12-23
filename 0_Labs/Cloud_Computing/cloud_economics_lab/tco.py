# ==========================================
# Simulación de Cloud Economics - Cálculo TCO
# ==========================================

# -------- Infraestructura local (On-Premise) --------

# Costo de comprar un servidor físico
costo_adquisicion_local = 5000  # USD

# Costos operativos anuales (electricidad, soporte, mantenimiento)
costos_operativos_local = 3000  # USD por año

# Valor que se recupera al vender el servidor al final de su vida útil
valor_rescate_local = 500  # USD

# Calculamos el Costo Total de Propiedad (TCO) en 5 años
# Fórmula: compra + (operación anual x años) - valor de rescate
tco_local = costo_adquisicion_local + (costos_operativos_local * 5) - valor_rescate_local

# -------- Infraestructura en la nube --------

# Costo mensual del servidor en la nube
costo_nube_mensual = 150  # USD por mes

# Tiempo de uso (5 años)
meses = 60

# Costo total en la nube (solo pago por uso)
tco_nube = costo_nube_mensual * meses

# -------- Mostrar resultados --------

print("=== Resultados de la simulación ===")
print(f"TCO Infraestructura Local (5 años): ${tco_local}")
print(f"TCO Infraestructura en la Nube (5 años): ${tco_nube}")