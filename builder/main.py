from hamburguesa_builder import HamburguesaBuilder

hamburguesa1 = HamburguesaBuilder().agregar_queso().agregar_lechuga().agregar_tomate().construir()
hamburguesa2 = HamburguesaBuilder().elegir_carne("Carne vegana").agregar_salsa("Mostaza").construir()

print(hamburguesa1)
print(hamburguesa2)