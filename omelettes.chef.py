from kitchen.Rosemary import Rosemary
from kitchen.utensils import Pan, Plate, Bowl
from kitchen.ingredients import Butter, Egg, Salt
#putting 3 eggs in a bowl to mix
bowl=Bowl.use(name='egg mixture')
for i in range(3):
    egg = Egg.take()
    egg.crack()
    bowl.add(egg)
bowl.mix()
#using a pan to make 3 omelettes and serve on 1 plate
pan = Pan.use(name='omelette')
plate = Plate.use()
for i in range(3):
 pan.add(Butter.take('slice'))
 pan.add(bowl.take('1/3'))
 pan.add(Salt.take('dash'))
 pan.cook(minutes=2)
 omelette = pan.take()
 plate.add(omelette)

Rosemary.serve(plate)
