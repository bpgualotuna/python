from empleados import EmpleadoTiempoCompleto, EmpleadoMedioTiempo, Empleado

empleado_tc = EmpleadoTiempoCompleto("Juan Perez", 3000)
empleado_mt = EmpleadoMedioTiempo("Ana Gomez", 2000)

empleados = [empleado_tc, empleado_mt]

for empleado in empleados:
    print(f"Empleado: {empleado.nombre}, Salario Total: {empleado.calcular_salario()}")

