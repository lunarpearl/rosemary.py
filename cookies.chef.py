from kitchen.ingredients.Collections import BakedCollection
from kitchen.Rosemary import Rosemary
from kitchen.utensils import BakingTray, Plate, Bowl, Fridge, Oven
from kitchen.ingredients import Egg, Salt, Flour, Butter, Sugar, ChocolateChips, BakingPowder
#making a batter for cookies in the bowl:
#creaming butter with sugar
bowl=Bowl.use(name='cookie batter')
bowl.add(Butter.take(grams=200))
for i in range(10):
    bowl.add(Sugar.take(grams=20))
    bowl.mix()
#mix in 2 eggs and some salt into the batter
for i in range(2):
    egg=Egg.take()
    egg.crack()
    bowl.add(egg)
    bowl.mix()
bowl.add(Salt('a pinch'))
bowl.mix()
#slowly incorporate flour into the batter
for i in range(10):
    bowl.add(Flour.take(grams=30))
    bowl.mix()
#mix in chocolate chips into the batter
bowl.add(ChocolateChips('a 200 g bag'))
bowl.mix()
#mix in baking soda/baking powder (not a 1:1 correlation in substitution) into the batter
bowl.add(BakingPowder('a teaspoon'))
bowl.mix()
#lets preheat the oven before putting anything in there
oven=Oven.use()
oven.preheat(degrees=175)
#meanwhile, we should scoop cookies onto the baking tray
cookietray=BakingTray.use(name='tray of cookies')
for i in range(10):
    cookietray.add(bowl.take('1/10'))
#now we can put the tray with cookies in the oven to bake for 10 min
oven.add(item=cookietray)
oven.bake(minutes=10)
#after baking we need to let the cookies cool in the fridge(though that is not really good for the condition of the fridge)
oven.take()
hotcookies=cookietray.take()
cookiebowl=Bowl.use('cooked cookies')
cookiebowl.add(hotcookies)
fridge=Fridge.use()
fridge.add(item=cookiebowl)
#now we can serve the cooled down cookies on the plate
coolcookies=cookiebowl.take()
plate=Plate.use(name='cooled down cookies')
plate.add(coolcookies)
Rosemary.serve(plate)