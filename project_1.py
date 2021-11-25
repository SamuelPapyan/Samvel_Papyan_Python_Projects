from enum import Enum
from datetime import datetime
from re import *

# SalesMethod Enum
class SalesMethod(Enum):
  ByRecipe = 1
  FreeSale = 2

#DrugType Enum
class DrugType(Enum):
  Pill = 1
  Powder = 2
  Salve = 3
  Liquid = 4

#Pharmacy (Դեղատուն) դասը
class Pharmacy:
  instances = 0
  #Կոնստրուկտորը
  def __init__(self,sales_method,name,address,pharmacy_network,drugs):
    # Դեղատան համարը
    self._pharmacy_id = Pharmacy.instances+1
    # Վճարման միջոց
    self._sales_method = sales_method.name
    # Անվանում
    self._name = name
    # Հասցե
    self._address = address
    # Դեղատների ցանց
    self._pharmacy_network = pharmacy_network
    # Դեղերի ցանկ
    self._drugs = drugs
    Pharmacy.instances += 1

  # Դեղատան արտապատկերում
  def show(self):
    print("Pharmacy: {}".format(self._pharmacy_id))
    print("Sales Method: {}".format(self._sales_method))
    print("Name: {}".format(self._name))
    print("Address: {}".format(self._address))
    print("Pharmacy Network Website Link: {}".format(self._pharmacy_network.website_link))
    print("Drugs: ",end="")
    for drug in self.drugs:
      print(drug.title,"|",end=" ")
    print()
    print("-------------------------------------")
  # Ստանալ դեղատան կարգահամարը
  def get_id(self):
    return self._pharmacy_id
  # Ստանալ վճարման միջոցը
  @property
  def sales_method(self):
    return self._sales_method
  # Ստանալ դեղատան անվանումը
  @property
  def name(self):
    return self._name
  # Ստանալ հասցե
  @property
  def address(self):
    return self._address
  # Ստանալ դեղատների ցանցը
  @property
  def pharmacy_network(self):
    return self._pharmacy_network
  # Ստանալ դեղերի ցանկը
  @property
  def drugs(self):
    return self._drugs
  # Փոխել վճարման միջոցը
  @sales_method.setter
  def sales_method(self,sales_method):
    if not isinstance(sales_method, SalesMethod):
      return
    self._sales_method = sales_method.name
  # Փոխել դեղատան անվանումը
  @name.setter
  def name(self,name):
    if not isinstance(name,str) or len(name) == 0:
      return
    self._name = name
  # Փոխել հասցեն
  @address.setter
  def address(self,address):
    if not isinstance(address,str) or len(address) == 0:
      return
    self._address = address
  # Փոխել դեղատների ցանցը
  @pharmacy_network.setter
  def pharmacy_network(self,pharmacy_network):
    if not isinstance(pharmacy_network,PharmacyNetwork):
      return
    self._pharmacy_network = pharmacy_network
  # Ավելացնել դեղը դեղերի ցանկում
  def add_drug(self,drug):
    if not isinstance(drug,Drug):
      return
    self._drugs.append(drug)
  # Հեռացնել դեղը դեղերի ցանկից
  def remove_drug(self,drug):
    index = -1
    if not isinstance(drug, Drug):
      return
    for i in range(0,len(self._drugs)-1):
      if self._drugs[i].get_id() == drug.get_id():
        index = i
    if i != -1:
      self._drugs.pop(i)
  # Փոխել ղեղերի ցանկը
  @drugs.setter
  def drugs(self,drugs):
    if not isinstance(drugs,list):
      return
    for i in drugs:
      if not isinstance(i,Drug):
        return
    self._drugs = drugs


#PharmacyNetwork (Դեղատների ցանց) դասը
class PharmacyNetwork:
  # Ստեղծված դեղատների ցանցերի քանակը
  instances = 0
  # Կոնստրուկտոր
  def __init__(self, website_link):
    # Դեղատների ցանցի համարը
    self._pharmacy_network_id = PharmacyNetwork.instances+1
    # Վեբկայքի հղումը
    self._website_link = website_link
    PharmacyNetwork.instances += 1

  # Արտապատկերել դեղատների ցանցը
  def show(self):
    print("Pharmacy Network: {}".format(self._pharmacy_network_id))
    print("Website Link: {}".format(self._website_link))
    print("-------------------------------------")
  # Ստանալ դեղատների ցանցի համարը
  def get_id(self):
    return self._pharmacy_network_id
  # Ստանալ վեբկայքի հղումը
  @property
  def website_link(self):
    return self._website_link
  # Փոխել վեբկայքի հղումը
  @website_link.setter
  def website_link(self,website_link):
    if not isinstance(website_link, str):
      return
    self._website_link = website_link

# Manufacturer (Արտադրող) դասը
class Manufacturer:
  # Ստեղծված արտադրողների քանակը
  instances = 0
  # Կոնստրուկտորը
  def __init__(self, contact_name, address, phone, country):
    # Արտադրողի համարը
    self._manufacturer_id = Manufacturer.instances+1
    # Անուն Ազգանուն
    self._contact_name = contact_name
    # Հասցե
    self._address = address
    # Հեռախոսահամաը
    self._phone = phone
    # Երկիր-պետություն
    self._country = country
    Manufacturer.instances += 1
  # Արտապատկերել առտադրողի տվյալները
  def show(self):
    print("Manufacturer: {}".format(self._manufacturer_id))
    print("Contact Name: {}".format(self._contact_name))
    print("Address: {}".format(self._address))
    print("Phone: {}".format(self._phone))
    print("Country: {}".format(self._country))
    print("-------------------------------------")
  # Ստանալ արտադրողի համարը
  def get_id(self):
    return self._manufacturer_id
  # Ստանալ անուն ազգանունը
  @property
  def contact_name(self):
    return self._contact_name
  # Ստանալ հասցեն
  @property
  def address(self):
    return self._address
  # Ստանալ հեռախոսահամարը
  @property
  def phone(self):
    return self._phone
  # Ստանալ երկիր-պետությունը
  @property
  def country(self):
    return self._country
  # Փոխել անուն ազգանունը
  @contact_name.setter
  def contact_name(self,contact_name):
    if not isinstance(contact_name, str):
      return
    self._contact_name = contact_name
  # Փոխել հասցեն
  @address.setter
  def address(self,address):
    if not isinstance(address, str):
      return
    self._address = address
  # Փոխել հեռախոսահամարը
  @phone.setter
  def phone(self,phone):
    if not isinstance(phone, str):
      return
    self._phone = phone
  # Փոխել երկիր-պետությունը
  @country.setter
  def country(self,country):
    if not isinstance(country, str):
      return
    self._country = country

# Supplier (Ներմուծող) դասը
class Supplier:
  # Ստեղծված ներմուծողների քանակը
  instances = 0
  # Կոնստրուկտորը
  def __init__(self, contact_name, address, phone, country):
    # Ներմուծողի համար
    self._supplier_id = Supplier.instances+1
    # Անուն ազգանուն
    self._contact_name = contact_name
    # Հասցե
    self._address = address
    # Հեռախոսահամար
    self._phone = phone
    # Երկիր-պետություն
    self._country = country
    Supplier.instances += 1
  # Արտապատկերել ներմուծողի տվյալները
  def show(self):
    print("Supplier: {}".format(self._supplier_id))
    print("Contact Name: {}".format(self._contact_name))
    print("Address: {}".format(self._address))
    print("Phone: {}".format(self._phone))
    print("Country: {}".format(self._country))
    print("-------------------------------------")
  # Ստանալ ներմուծողի համարը
  def get_id(self):
    return self._supplier_id
  # Ստանալ անուն ազգանունը
  @property
  def contact_name(self):
    return self._contact_name
  # Ստանալ հասցեն
  @property
  def address(self):
    return self._address
  # Ստանալ հեռախոսահամարը
  @property
  def phone(self):
    return self._phone
  # Ստանալ երկիր-պետությունը
  @property
  def country(self):
    return self._country
  # Փոխել անուն ազգանունը
  @contact_name.setter
  def contact_name(self,contact_name):
    if not isinstance(contact_name, str):
      return
    self._contact_name = contact_name
  # Փոխել հասցեն
  @address.setter
  def address(self,address):
    if not isinstance(address, str):
      return
    self._address = address
  # Փոխել հեռախոսահամարը
  @phone.setter
  def phone(self,phone):
    if not isinstance(phone, str):
      return
    self._phone = phone
  # Փոխել երկիր-պետությունը
  @country.setter
  def country(self,country):
    if not isinstance(country, str):
      return
    self._country = country

# Drug (Դեղ) դասը
class Drug:
  # Ստեղծված դեղերի քանակը
  instances = 0
  # Կոնստրուկտորը
  def __init__(self,title,sales_method,price,dose,description,contents,manufacturer,supplier,side_effects,drug_type,expiration_date,category):
    # Դեղի համարը
    self._drug_id = Drug.instances+1
    # Դեղի անվանումը
    self._title = title
    # Վճարման միջոցը
    self._sales_method = sales_method.name
    # Գին
    self._price = price
    # Դոզա
    self._dose = dose
    # Նկարագրությունը
    self._description = description
    # Դեղի պարունակության ցուցակը
    self._contents = contents
    # Արտադրող
    self._manufacturer = manufacturer
    # Ներմուծող
    self._supplier = supplier
    # Կողմնակի ազդեցությունների ցանկը
    self._side_effects = side_effects
    # Դեղի տեսակը
    self._drug_type = drug_type.name
    # Դեղի ժամկետը
    self._expiration_date = expiration_date
    # Դասակարգիչ
    self._category = category
    Drug.instances += 1
  # Արտապատկերել դեղի տվյալները
  def show(self):
    print("Drug: {}".format(self._drug_id))
    print("Title: {}".format(self._title))
    print("Sales Method: {}".format(self._sales_method))
    print("Price: {}".format(self._price))
    print("Dose: {}mg".format(self._dose))
    print("Description: {}".format(self._description))
    print("Contents: ",end="")
    for content in self._contents:
      print(content,"|",end=" ")
    print()
    print("Manufacturer: {}".format(self._manufacturer.contact_name))
    print("Supplier: {}".format(self._supplier.contact_name))
    print("Side effects: ",end="")
    for item in self._side_effects:
      print(item,"|",end=" ")
    print()
    print("Drug Type: {}".format(self._drug_type))
    print("Expiration Date: {}".format(self._expiration_date.strftime("%d/%m/%Y")))
    print("Category: {}".format(self._category.category_name))
    print("-------------------------------------")
  # Ստանալ դեղի համարը
  def get_id(self):
    return self._drug_id
  # Ստանալ դեղի անվանումը
  @property
  def title(self):
    return self._title
  # Ստանալ վաճառքի միջոցը
  @property
  def sales_method(self):
    return self._sales_method
  # Ստանալ գինը
  @property
  def price(self):
    return self._price
  # Ստանալ դոզան
  @property
  def dose(self):
    return self._dose
  # Ստանալ նկարագրությունը
  @property
  def description(self):
    return self._description
  # Ստանալ ղեղի պարունակության ցանկը
  @property
  def contents(self):
    return self._contents
  # Ստանալ արտադրողի տվյալները
  @property
  def manufacturer(self):
    return self._manufacturer
  # Ստանալ ներմուծողի տվյալները
  @property
  def supplier(self):
    return self._supplier
  # Ստանալ կողմնային ազդեցությունների ցուցակը
  @property
  def side_effects(self):
    return self._side_effects
  # Ստանալ դեղի տեսակը
  @property
  def drug_type(self):
    return self._drug_type
  # Ստանալ դեղի ժամկետը
  @property
  def expiration_date(self):
    return self._expiration_date
  # Ստանալ դասակարգիչը
  @property
  def category(self):
    return self._category
  # Թոխել դեղի անվանումը
  @title.setter
  def title(self,title):
    if not isinstance(title, str) or len(title) == 0: 
      return
    self._title = title
  # Փոխել վճարռքի միջոցը
  @sales_method.setter
  def sales_method(self, sales_method):
    if not isinstance(sales_method, SalesMethod):
      return
    self._sales_method = sales_method.name
  # Փոխել գինը
  @price.setter
  def price(self,price):
    if not isinstance(price,int):
      return
    self._price = price
  # Փոխել դոզան
  @dose.setter
  def dose(self,dose):
    if not isinstance(dose,float):
      return
    self._dose = dose
  # Փոխել նկարագրությունը
  @description.setter
  def description(self,description):
    if not isinstance(description, str) or len(description) == 0: 
      return
    self._description = description
  # Ավելացնել դեղի պարունակությունը ցուցակում
  def add_content(self,content):
    if not isinstance(title, str) or len(title) == 0: 
      return
    self._contents.append(content)
  # Հեռացնել դեղի պարունակությունը ցեւցակից
  def remove_content(self,content):
    if not isinstance(title, str) or len(title) == 0: 
      return
    self._contents.remove(content)
  # Փոխել դեղի պարունակությունների ցուցակը
  @contents.setter
  def contents(self,contents):
    if not isinstance(contents, list):
      return
    for i in contents:
      if not isinstance(i, str) or len(i) == 0: 
        return
    self._contents = contents
  # Փոխել արտադրողը
  @manufacturer.setter
  def manufacturer(self,manufacturer):
    if not isinstance(manufacturer, Manufacturer):
      return
    self._manufacturer = manufacturer
  # Փոխել ներմուծողը
  @supplier.setter
  def supplier(self,supplier):
    if not isinstance(supplier,Supplier):
      return
    self._supplier = supplier
  # Ավելացնել կողմնակի ազդեցությունը ցուցակում
  def add_side_effect(self,side_effect):
    if not isinstance(side_effect, str):
      return
    self._side_effects.append(side_effect)
  # Հեռացնել կողմնակի ազդցությունը ցուցակից
  def remove_side_effect(self,side_effect):
    if not isinstance(side_effect, str):
      return
    self._side_effects.remove(side_effect)
  # Փոխել կողմնակի ազդեցությեւննեի ցուցակը
  @side_effects.setter
  def side_effects(self,side_effects):
    if not isinstance(side_effects, list):
      return
    for i in side_effect:
      if not isinstance(i,str) or len(i) == 0:
        return
    self._side_effects = side_effects
  # Փոխել դեղի տեսակը
  @drug_type.setter
  def drug_type(self,drug_type):
    if not isinstance(drug_type, DrugType):
      return
    self._drug_type = drug_type.name
  # Փոխել դեղի ժամկետը
  @expiration_date.setter
  def expiration_date(self,expiration_date):
    if not isinstance(expiration_type,datetime):
      return
    self._expiration_date = expiration_date
  # Փոխել դասակարգիչը
  @category.setter
  def category(self, category):
    if not isinstance(category,Category):
      return
    self._category = category
  
# Category (Դասակարգիչ) դասը
class Category:
  # Ստեղծված դասակարգիչների քանակը
  instances = 0
  # Կոնստրուկտոր
  def __init__(self, category_name):
    # Դասակարգիչի համարը
    self._category_id = Category.instances+1
    # Դասակարգիչի անվանումը
    self._category_name = category_name
    Category.instances += 1
  # Արտապատկերել դասակարգիչի տվյալները
  def show(self):
    print("Category: {}".format(self._category_id))
    print("Category Name: {}".format(self._category_name))
    print("-------------------------------------")
  # Ստանալ դասակարգիչի համարը
  def get_id(self):
    return self._category_id
  # Ստանալ դասակարգիչի անվանումը
  @property
  def category_name(self):
    return self._category_name
  # Փոխել դասակարգիչի անվանումը
  @category_name.setter
  def category_name(self,category_name):
    if not isinstance(category_name,str) or len(category_name) == 0:
      return
    self._category_name = category_name


# Դեղատների ցանցեր
pharmacyNetwork1 = PharmacyNetwork("alfapharm.am")
pharmacyNetwork2 = PharmacyNetwork("natali-pharm.am")
pharmacyNetwork3 = PharmacyNetwork("36-6.com")

# Արտադրողներ
manufacturer1 = Manufacturer("Artyom Markosyan","Abovyan str 12","+374 10 765912","Armenia")
manufacturer2 = Manufacturer("Karen Davtyan","Komitas ave 14","+374 12 950123","Armenia")
manufacturer3 = Manufacturer("David Karapetyan","Sayat-Nova ave 12","+374 14 981254","Armenia")

# Ներմուծողներ
supplier1 = Supplier("Daniel Sargsyan","Baghramyan ave 14", "+374 97 921466","Armenia")
supplier2 = Supplier("Rafi Hovhannisyan","Azatutyan ave 29", "+374 91 861234","Armenia")
supplier3 = Supplier("Narek Sargsyan","Tumanyan str 13","+374 97 861423","Armenia")

# Դասակարգիչներ
category1 = Category("Pain Medicine")
category2 = Category("Soar Throat Medicine")
category3 = Category("Heartburn Medicine")

# Դեղեր
drug1 = Drug("Nurofen",SalesMethod.ByRecipe,12000,400,"Pain Medicine",["Ibuprofen"],manufacturer1,supplier1,["Constipation","Dizziness","Nervousness"],DrugType.Pill,datetime(2022,5,22),category1)
drug2 = Drug("Strepsils",SalesMethod.FreeSale,15000,350,"Sore Throat Medicine",["Dichlorobenzyl Alcohol","Amylmetacresol"],manufacturer2,supplier2,["Hiccups","Heartburn"],DrugType.Pill,datetime(2022,6,17),category2)
drug3 = Drug("Geviscon",SalesMethod.ByRecipe,16000,350,"Heartburn Medicine",["Sodium Alginate","Sodium Bicarbonate","Calcium Carbonate"],manufacturer3,supplier3,[],DrugType.Liquid,datetime(2022,7,23),category3)

# Դեղատներ
pharmacy1 = Pharmacy(SalesMethod.ByRecipe,"AlfaPharm","Komitas Ave. 46",pharmacyNetwork1,[drug1,drug2])
pharmacy2 = Pharmacy(SalesMethod.FreeSale,"Natali Pharm","Komitas Ave. 1", pharmacyNetwork2,[drug1,drug2,drug3])
pharmacy3 = Pharmacy(SalesMethod.ByRecipe,"36 6","Abovyan Str. 36", pharmacyNetwork3,[drug2, drug3])

# UI (Օգտռագործողի Տեսարան) դասը
class UI:
  # Տվյալների բազա (կեղծ)
  my_db = {
    "pharmacies":[pharmacy1,pharmacy2,pharmacy3],
    "categories":[category1,category2,category3],
    "manufacturers":[manufacturer1, manufacturer2, manufacturer3],
    "suppliers":[supplier1,supplier2,supplier3],
    "drugs":[drug1,drug2,drug3],
    "pharmacy_networks":[pharmacyNetwork1,pharmacyNetwork2,pharmacyNetwork3]
  }
  # Ինդեքսներ (բանալիներ)
  indexes = {
      1:"pharmacies",
      2:"categories",
      3:"manufacturers",
      4:"suppliers",
      5:"drugs",
      6:"pharmacy_networks"
  }
  # Կոնստրուկտոր
  def __init__(self):
    print("Welcome to Samvel Papyan's Project")
    self.instruction_case_1()
  # Տվյալների ցուցակների ցուցակ
  def instruction_case_1(self):
    print("Press 1 for list of pharmacies")
    print("Press 2 for list of categories")
    print("Press 3 for list of manufacturers")
    print("Press 4 for list of suppliers")
    print("Press 5 for list of drugs")
    print("Press 6 for list of pharmacy networks")
    print("Press 0 for exit")
    try:
      num = int(input())
      self.check_index(num)
    except:
      print("Wrong Input, Try Again")
      self.instruction_case_1()
  # Ինդեքսի ստուգում (ցուցակի որոնում)
  def check_index(self,index):
    if index in [1,2,3,4,5,6]:
      for obj in UI.my_db[UI.indexes[index]]:
        obj.show()
      self.instruction_case_2(index)
    elif index == 0:
      print("Goodbye")
    else:
      self.instruction_case_1()
  
  # Գործողությունների ցուցակ
  def instruction_case_2(self,index):
    print("Press 1 for search an item")
    print("Press 2 for insert an item")
    print("Press 3 for deleting an item")
    print("Press 0 for undo")
    try:
      num = int(input())
      self.check_action(num,index)
    except:
      print("Wrong input, try again")
      self.instruction_case_2(index)

  # Ներմուծված գործողությունի ստուգում
  def check_action(self,index,list_index):
    if index == 1:
      self.search_instruction(list_index)
    elif index == 2:
      self.insert_instruction(list_index)
    elif index == 3:
      self.delete_instruction(list_index)
    elif index == 0:
      self.instruction_case_1()
    else:
      self.instruction_case_2()
  
  # Որոնման գործողություն
  def search_instruction(self,index):
    my_input = input("Type something for search or enter 'exit_search' for undo: ")
    if(my_input != "exit_search"):
      numerical_input = -1
      search_results = 0
      try:
        numerical_input = int(input)
      except:
        numerical_input = -1
      print("---------- Search Results ------------------")
      for obj in UI.my_db[UI.indexes[index]]:
        for i in obj.__dict__:
          if isinstance(obj.__dict__.get(i),int):
            if obj.__dict__.get(i) == numerical_input:
              obj.show()
              search_results += 1
              break
          elif isinstance(obj.__dict__.get(i),str):
            regex = '.*' + my_input + '.*'
            compiler = compile(regex,IGNORECASE)
            if bool(compiler.match(obj.__dict__.get(i))):
              obj.show()
              search_results += 1
              break
      if search_results == 0:
        print("No results")
        print("-----------------------------------------")
    self.check_index(index)
  
  # Հեռացման գործողություն
  def delete_instruction(self,index):
    answer = input("Are you want to delete one of items?[Y/N]")
    if answer in ["y","yes","Y","YES"]:
      my_input = -1
      while(not my_input in [x.get_id() for x in UI.my_db[UI.indexes[index]]]):
        try:
          my_input = int(input("Select id of item for deleting: "))
          if not my_input in [x.get_id() for x in UI.my_db[UI.indexes[index]]]:
            raise Exception("")
        except:
          print("Wrong input, try again.")
      my_id = -1
      for i in range(len(UI.my_db[UI.indexes[index]])):
        if UI.my_db[UI.indexes[index]][i].get_id() == my_input:
          my_id = i
      
      if my_id != -1:
        UI.my_db[UI.indexes[index]].pop(my_id)
        print("-----------------------------------------")
        print("Item successfully deleted.")
        print("-----------------------------------------")
    self.check_index(index)
  # Դեղատան ավելացում
  def add_pharmacy(self):
    my_sales_method = 0
    while my_sales_method == 0:
      try:
        print("1 - By Recipe")
        print("2 - Free Sale")
        my_sales_method = int(input("Sales Method: "))
        if not my_sales_method in [1,2]:
            my_sales_method = 0
            raise Exception("")
      except:
        print("Wrong Input! Try again.")
    my_name = input("Pharmacy Name: ")
    my_address = input("Address: ")
    print("Pharmacy Network")
    my_pharmacy_network_id = 0
    my_pharmacy_network = 0
    while my_pharmacy_network_id == 0:
      try:
        for obj in UI.my_db["pharmacy_networks"]:
          print(obj.get_id(),"-",obj.website_link)
        my_pharmacy_network_id = int(input("Pharmacy Network Id: "))
        if not my_pharmacy_network_id in [x.get_id() for x in UI.my_db["pharmacy_networks"]]:
          my_pharmacy_network_id = 0
          raise Exception("")
        else:
          for i in UI.my_db["pharmacy_networks"]:
            if i.get_id() == my_pharmacy_network_id:
              my_pharmacy_network = i
      except:
        print("Wrong Input! Try again.")
    my_drugs = []
    my_input = -1
    while my_input != 0:
      try:
        print("List of drugs")
        for obj in UI.my_db["drugs"]:
          print(obj.get_id(),"-",obj.title)
        print("----------------")
        print("List of my drugs")
        for i in my_drugs:
          print("-",i.title)
        my_input = int(input("Add drug or enter 0 for exit: "))
        if my_input == 0:
          break
        elif not my_input in [x.get_id() for x in UI.my_db["drugs"]]:
          my_input = -1
          raise Exception("")
        else:
          my_drug = 0
          for i in UI.my_db["drugs"]:
            if i.get_id() == my_input:
              my_drug = i
          my_drugs.append(my_drug)
      except:
        print("Wrong input! Try Again.")
    UI.my_db["pharmacies"].append(Pharmacy(SalesMethod(my_sales_method),my_name,my_address,my_pharmacy_network,my_drugs))
    print("--------------------------------")
    print("Pharmacy successfully added")
    print("--------------------------------")

  # Դեղի ավելացում
  def add_drug(self):
    my_title = input("Drug Title: ")
    my_sales_method = 0
    while my_sales_method == 0:
      try:
        print("1 - By Recipe")
        print("2 - Free Sale")
        my_sales_method = int(input("Sales Method: "))
        if not my_sales_method in [1,2]:
            my_sales_method = 0
            raise Exception("")
      except:
        print("Wrong Input! Try again.")
    my_price = 0
    while my_price == 0:
      try:
        my_price = int(input("Price: "))
      except:
        print("Wrong Input! Try again.")
    my_dose = 0.0
    while my_dose == 0.0:
      try:
        my_dose = float(input("Dose(mg): "))
      except:
        print("Wrong Input! Try again.")
    my_description = input("Description: ")
    my_contents = []
    my_content = ""
    while my_content != "end":
      print("Contents")
      for i in my_contents:
        print("-" + i)
      my_content = input(r"Add content or enter 'end' command for exit: ")
      if my_content != "end":
        my_contents.append(my_content)
    my_manufacturer_id = 0
    my_manufacturer = 0
    while my_manufacturer == 0:
      print("Manufacturer")
      for i in UI.my_db['manufacturers']:
        print(str(i.get_id()) + " - " + i.contact_name)
      try:
        my_manufacturer_id = int(input("Choose Manufacturer Id: "))
        if not my_manufacturer_id in [x.get_id() for x in UI.my_db['manufacturers']]:
          raise Exception("")
        for i in UI.my_db['manufacturers']:
          if i.get_id() == my_manufacturer_id:
            my_manufacturer = i
      except:
        print("Wrong input, try again!")
    my_supplier_id = 0
    my_supplier = 0
    while my_supplier == 0:
      print("Supplier")
      for i in UI.my_db['suppliers']:
        print(str(i.get_id()) + " - " + i.contact_name)
      try:
        my_supplier_id = int(input("Choose Supplier Id: "))
        if not my_supplier_id in [x.get_id() for x in UI.my_db['suppliers']]:
          raise Exception("")
        for i in UI.my_db['suppliers']:
          if i.get_id() == my_supplier_id:
            my_supplier = i
      except:
        print("Wrong input, try again!")
    my_side_effects = []
    my_side_effect = ""
    while my_side_effect != "end":
      print("Side Effects")
      for i in my_side_effects:
        print("- " + i)
      my_side_effect = input(r"Add side effect of enter 'end' for exit: ")
      if my_side_effect != "end":
        my_side_effects.append(my_side_effect)
    my_drug_type = 0
    while(not my_drug_type in [1,2,3,4]):
      print("1 - Pill")
      print("2 - Powder")
      print("3 - Salve")
      print("4 - Liquid")
      try:
        my_drug_type = int(input("Select Drug Type: "))
      except:
        print("Wrong input, try again.")
    my_brand = input("Brand: ")
    print("Expiration Date")
    my_date = 0
    while my_date == 0:
      try:
        my_day = int(input("Day: "))
        my_month = int(input("Month: "))
        my_year = int(input("Year: "))
        if (not my_day in range(1,32)) or (not my_month in range(1,12+1)) or (my_year in range(2021+1)):
          raise Exception("")
        my_date_str = str(my_day) + "/" + str(my_month) + "/" + str(my_year)
        my_date = datetime.strptime(my_date_str,"%d/%m/%Y")
      except:
        print("Wrong input, try again.")
    my_category_id = 0
    my_category = 0
    while my_category == 0:
      print("Category")
      for i in UI.my_db['categories']:
        print(str(i.get_id()) + " - " + i.category_name)
      try:
        my_category_id = int(input("Select Category: "))
        if not my_category_id in [x.get_id() for x in UI.my_db['categories']]:
          raise Exception("")
        for i in UI.my_db['categories']:
          if i.get_id() == my_category_id:
            my_category = i
      except:
        print("Wrong input, try again.")
    UI.my_db['drugs'].append(Drug(my_title,SalesMethod(my_sales_method),my_price,my_dose,my_description,my_contents,my_manufacturer,my_supplier,my_side_effects,DrugType(my_drug_type),my_date,my_category))
    print("--------------------------------")
    print("Drug Successfully Added")
    print("--------------------------------")

  # Դասակարգիչի ավելացում
  def add_category(self):
    my_name = input("Category Name: ")
    UI.my_db["categories"].append(Category(my_name))
    print("--------------------------------")
    print("Category Successfully Added")
    print("--------------------------------")
  # Արտադրողի ավելացում
  def add_manufacturer(self):
    my_contact_name = input("Contact Name: ")
    my_address = input("Address: ")
    my_phone = input("Phone: ")
    my_country = input("Country: ")
    UI.my_db["manufacturers"].append(Manufacturer(my_contact_name, my_address, my_phone, my_country))
    print("--------------------------------")
    print("Manufacturer Successfully Added")
    print("--------------------------------")
  # Ներմուծողի ավելացում
  def add_supplier(self):
    my_contact_name = input("Contact Name: ")
    my_address = input("Address: ")
    my_phone = input("Phone: ")
    my_country = input("Country: ")
    UI.my_db["suppliers"].append(Supplier(my_contact_name, my_address, my_phone, my_country))
    print("--------------------------------")
    print("Supplier Successfully Added")
    print("--------------------------------")
  # Դեղատան ցանցի ավելացում
  def add_pharmacy_network(self):
    my_website_link = input("Website Link: ")
    UI.my_db["pharmacy_networks"].append(PharmacyNetwork(my_website_link))
    print("--------------------------------")
    print("Pharmacy Network Successfully Added")
    print("--------------------------------")

  # Ավելացման նախասկզբման գործողություն
  def insert_instruction(self,index):
    answer = input("Are you want to insert a new item?[Y/N]")
    if answer in ["y","yes","Y","YES"]:
      db_index = UI.indexes[index]
      if db_index == "pharmacies":
        self.add_pharmacy()
      elif db_index == "categories":
        self.add_category()
      elif db_index == "drugs":
        self.add_drug()
      elif db_index == "manufacturers":
        self.add_manufacturer()
      elif db_index == "suppliers":
        self.add_supplier()
      elif db_index == "pharmacy_networks":
        self.add_pharmacy_network()
      else:
        self.instruction_case_2(index)
    self.check_index(index)
    
# UI-ի բացումը
UI()
