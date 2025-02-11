from auto import Auto
from hacedor import AutoBuilder
from director import Director

# Uso del Builder
builder = AutoBuilder()
director = Director(builder)

director.construir_auto_basico()
auto = builder.get_auto()
print(auto)

builder2 = AutoBuilder()
director2 = Director(builder2)

director2.construir_auto_caro()
auto2 = builder2.get_auto()
print("Es mejor este auto: ",auto2)