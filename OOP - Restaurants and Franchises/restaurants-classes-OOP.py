class Menu:
  
  def __init__(self, name, items, start_time,end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  
  def __repr__(self):
    return str(self.name) + " menu available from " + str(self.start_time) + " to " + str(self.end_time)

  def calculate_bill(self, purchased_items):
    total_price = 0
    for item in purchased_items:
      total_price += self.items[item]
    return total_price


brunch = Menu("brunch", {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}, 11, 16)

early_bird = Menu("early_bird", {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}, 7,11)

dinner = Menu("dinner", {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}, 16,22)

kids = Menu("kids", {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}, 11, 21)


brunch_cost = early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)'])

menu_list = [brunch, early_bird, dinner, kids]

class Franchise():
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  def __repr__(self):
    return self.address
  def available_menus(self, time):
    list_menus = []
    for menu in self.menus:
      if(time >= menu.start_time):
        list_menus.append(menu.name)
    return list_menus

flagship_store = Franchise("1232 West End Road", menu_list)

new_installment = Franchise("12 East Mulberry Street", menu_list)

print(flagship_store.available_menus(18))

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises


arepas_menu = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

arepas_place = Franchise("189 Fitzgerald Avenue", arepas_menu)

new_business = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

new_business_arepa = Business("Take a' Arepa", arepas_place)