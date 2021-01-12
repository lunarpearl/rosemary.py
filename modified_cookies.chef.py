from kitchen.ingredients.Collections import Collection, Mixture, Portion
from kitchen.Rosemary import Rosemary
from kitchen.utensils import BakingTray, Plate, Bowl, Fridge, Oven
from kitchen.ingredients import Egg, Salt, Flour, Butter, Sugar, ChocolateChips, BakingPowder
#making a mixture of ingredients for cookies
batter=Mixture(name='batter to make cookies')
butter=Butter.take(grams=200)
batter._add(item=butter)
for i in range(10):
    sugar=Sugar.take(grams=20)
    batter._add(sugar)
    batter._mix()
for i in range(2):
    egg=Egg.take()
    egg.crack()
    batter._add(egg)
    batter._mix() 
salt=Salt.take('a pinch')
batter._add(salt)
batter._mix()
for i in range(10):
    flour=Flour.take(grams=30)
    batter._add(flour)
    batter._mix()
chocchips=ChocolateChips.take('a 200 g bag')
batter._add(chocchips)
batter._mix()
soda=BakingPowder.take('a teaspoon')
batter._add(soda)
batter._mix()
#making a measurement of ingredients for a single cookie
single_cookie=Portion(ingredient=batter,portion=1/16)
#baking 16 cookies
oven=Oven.use()
oven.preheat(degrees=175)
cookietray=BakingTray.use(name='tray of cookies')
for i in range(16):
    cookietray.add(single_cookie)
oven.add(item=cookietray)
oven.bake(minutes=10)
#cooling the cookies
oven.take()
hotcookies=cookietray.take()
cookiebowl=Bowl.use('cooked cookies')
cookiebowl.add(hotcookies)
fridge=Fridge.use()
fridge.add(item=cookiebowl)
#serving cookies
coolcookies=cookiebowl.take()
plate=Plate.use(name='cooled down cookies')
plate.add(coolcookies)
Rosemary.serve(plate)