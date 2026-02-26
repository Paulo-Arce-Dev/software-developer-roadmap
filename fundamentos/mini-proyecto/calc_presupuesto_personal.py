# calculadora de presupuesto personal

# ingresos
def income_record ():
  registro_ingresos = float(input("Registrar un ingreso: "))
  return registro_ingresos

# gastos
def expense_record ():
  registro_gasto = float(input("Registrar un gasto: "))
  return registro_gasto

# balance
def balance ():
  ingresos = income_record()
  gastos = expense_record()
  balance = ingresos - gastos
  return f"Balance: ${balance:.2f}"

print(balance())