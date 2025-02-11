from fabrica_abstracta import ComboFactory
from mcfactory import McDonaldsFactory
from burguerfactory import BurgerKingFactory


# 6️⃣ Cliente que usa la fábrica abstracta
def preparar_combo(factory: ComboFactory):
    hamburguesa = factory.crear_hamburguesa()
    bebida = factory.crear_bebida()
    
    return f"{hamburguesa.preparar()} + {bebida.servir()}"

# 7️⃣ Probamos el patrón Abstract Factory
mc_factory = McDonaldsFactory()
bk_factory = BurgerKingFactory()

print(preparar_combo(mc_factory))
print(preparar_combo(bk_factory))