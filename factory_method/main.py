from creador_concreto import PizzeriaPepperoni, PizzeriaQueso, PizzeriaVegetariana


# 5️⃣ Uso del Factory Method
pizzeria = PizzeriaQueso()
print(pizzeria.ordenar_pizza())

pizzeria = PizzeriaPepperoni()
print(pizzeria.ordenar_pizza())

pizzeria = PizzeriaVegetariana()
print(pizzeria.ordenar_pizza())