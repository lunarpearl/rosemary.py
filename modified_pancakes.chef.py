from kitchen.ingredients.Collections import Collection, Mixture, Portion
from kitchen.Rosemary import Rosemary
from kitchen.utensils import Pan, Plate, Bowl
from kitchen.ingredients import Egg, Salt, Flour, Milk, Butter
#making a batter again but now as a mixture(class)
batter=Mixture(name='batter to make pancakes')
for i in range(2):
    egg=Egg.take()
    egg.crack()
    batter._add(item=egg)
batter._mix()
salt=Salt.take('a dash')
batter._add(item=salt)
batter._mix()
for i in range(5):
    flour=Flour.take(grams=50)
    batter._add(item=flour)
    batter._mix()
for i in range(2):
    milk=Milk.take(ml=500)
    batter._add(item=milk)
    batter._mix()
#making a specific measurement of ingredients to scoop for a single pancake
single_pancake=Portion(ingredient=batter,portion=1/8)
#cooking pancakes in a pan
pan=Pan.use(name='pancakes')
plate=Plate.use()
for i in range(8):
    pan.add(Butter.take(amount='a little'))
    pan.add(single_pancake)
    pan.cook(minutes=1)
    pan.flip()
    pan.cook(minutes=1)
    pan.flip()
    pancake=pan.take()
    plate.add(pancake)
Rosemary.serve(plate)

