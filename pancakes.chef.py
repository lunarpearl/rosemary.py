from kitchen.Rosemary import Rosemary
from kitchen.utensils import Pan, Plate, Bowl
from kitchen.ingredients import Egg, Salt, Flour, Milk, Butter
#whisking 2 eggs i a bowl
bowl=Bowl.use(name='batter')
for i in range(2):
    egg = Egg.take()
    egg.crack()
    bowl.add(egg)
bowl.mix()
#adding salt and flour in the batter, mixing in-between
bowl.add(Salt.take('dash'))
for i in range(5):
    bowl.add(Flour.take(grams=50))
    bowl.mix()
#adding milk in the batter, mixing in-between
for i in range(2):
    bowl.add(Milk.take(ml=250))
    bowl.mix()
#cooking 8 pancakes in a pan and serving it
pan=Pan.use(name='pancakes')
plate=Plate.use()
for i in range(8):
    pan.add(Butter.take(amount='a little'))
    pan.add(bowl.take('1/8'))
    pan.cook(minutes=1)
    pan.flip()
    pan.cook(minutes=1)
    pan.flip()
    pancake=pan.take()
    plate.add(pancake)
Rosemary.serve(plate)
