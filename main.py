from re import *
from datetime import datetime
import os
import json
import mysql.connector as mysqli
from enum import Enum

# SalesMethod Enum
class SalesMethod(Enum):
  ByRecipe = 1
  FreeSale = 2

# DrugType Enum
class DrugType(Enum):
  Pill = 1
  Powder = 2
  Salve = 3
  Liquid = 4

# Տվյալների բազայի հետ կապը
mydb = mysqli.connect(
  host="localhost",
  user="root",
  password="",
  database="pharmacy_db"
)
# Տվյալների բազայի հետ աշխատելու գործիքը (Կուրսոր)
mycursor = mydb.cursor()


# UI (Օգտռագործողի Տեսարան) դասը
class UI:
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
  
  def print_data_set(self,index):
    if index == 1:
      mycursor.execute('select * from pharmacies')
      data = mycursor.fetchall()
      for x in data:
        Printer.print_pharmacy(x)
        print("=======================")
    elif index == 2:
      mycursor.execute('select * from categories')
      data = mycursor.fetchall()
      for x in data:
        Printer.print_category(x)
        print("=======================")
    elif index == 3:
      mycursor.execute('select * from manufacturers')
      data = mycursor.fetchall()
      for x in data:
        Printer.print_manufacturer(x)
        print("=======================")
    elif index == 4:
      mycursor.execute('select * from suppliers')
      data = mycursor.fetchall()
      for x in data:
        Printer.print_supplier(x)
        print("=======================")
    elif index == 5:
      mycursor.execute('select * from drugs')
      data = mycursor.fetchall()
      for x in data:
        Printer.print_drug(x)
        print("=======================")
    elif index == 6:
      mycursor.execute('select * from pharmacy_networks')
      data = mycursor.fetchall()
      for x in data:
        Printer.print_pharmacy_network(x)
        print("=======================")
  # Ինդեքսի ստուգում (ցուցակի որոնում)      
  def check_index(self,index):
    if index in [1,2,3,4,5,6]:
      self.print_data_set(index)
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
      search_results = MySearchEngine.search(my_input, index)
      if len(search_results) == 0:
        print("No results")
      else:
        for item in search_results:
          Printer.print(item, index)
          print("=================================")
      print("-----------------------------------------")
      input("Press enter to continue")
    self.check_index(index)
  
  # Հեռացման գործողություն
  def delete_instruction(self,index):
    answer = input("Are you want to delete one of items?[Y/N]")
    try:
      if answer in ["y","yes","Y","YES"]:
        Delete.delete(index)
        print("-----------------------------------------")
        print("Item successfully deleted.")
        print("-----------------------------------------")
    except Exception as e:
      print(e)
    self.check_index(index)
  # Ավելացնել դեղատուն
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
    mycursor.execute("select pharmacy_network_id, website_link from pharmacy_networks")
    mydata = mycursor.fetchall()
    my_pharmacy_network = -1
    while my_pharmacy_network == -1:
      try:
        for obj in mydata:
          print(obj[0],"-",obj[1])
        my_pharmacy_network_id = int(input("Pharmacy Network Id: "))
        if not my_pharmacy_network_id in [x[0] for x in mydata]:
          raise Exception("")
        else:
          my_pharmacy_network = int(my_pharmacy_network_id)
      except:
        print("Wrong Input! Try again.")
    mycursor.execute("select drug_id, title from drugs")
    mydata = mycursor.fetchall()
    my_drugs = []
    my_input = -1
    while my_input != 0:
      try:
        print("List of drugs")
        for obj in mydata:
          print(obj[0],"-",obj[1])
        print("----------------")
        print("List of my drugs")
        for i in my_drugs:
          print("-",i["title"])
        my_input = int(input("Add drug or enter 0 for exit: "))
        if my_input == 0:
          break
        elif not my_input in [x[0] for x in mydata]:
          my_input = -1
          raise Exception("")
        else:
          drug_title = ""
          for i in mydata:
            if(i[0] == int(my_input)):
              drug_title = i[1]
          my_drug = {"drug_id":int(my_input),"title":drug_title}
          my_drugs.append(my_drug)
      except:
        print("Wrong input! Try Again.")
    
    input_query = "insert into pharmacies (sales_method, name, address, pharmacy_network_id) values (%s,%s,%s,%s)"
    query_val = (SalesMethod(my_sales_method).name,my_name,my_address,str(my_pharmacy_network))
    mycursor.execute(input_query,query_val)
    mydb.commit()

    input_query = "insert into drug_in_pharmacy (drug_id, pharmacy_id) values (%s, %s)"
    query_val = [(x["drug_id"], str(mycursor.lastrowid)) for x in my_drugs]
    mycursor.executemany(input_query,query_val)
    mydb.commit()
    print("--------------------------------")
    print("Pharmacy successfully added")
    print("--------------------------------")

  # Ավելացնել դեղ
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
    mycursor.execute("select manufacturer_id, contact_name from manufacturers")
    mydata = mycursor.fetchall()
    my_manufacturer_id = 0
    my_manufacturer = -1
    while my_manufacturer == -1:
      print("Manufacturer")
      for i in mydata:
        print(str(i[0]) + " - " + i[1])
      try:
        my_manufacturer_id = int(input("Choose Manufacturer Id: "))
        if not my_manufacturer_id in [x[0] for x in mydata]:
          raise Exception("")
        my_manufacturer = int(my_manufacturer_id)
      except:
        print("Wrong input, try again!")
    mycursor.execute("select supplier_id, contact_name from suppliers")
    mydata = mycursor.fetchall()
    my_supplier_id = 0
    my_supplier = -1
    while my_supplier == -1:
      print("Supplier")
      for i in mydata:
        print(str(i[0]) + " - " + i[1])
      try:
        my_supplier_id = int(input("Choose Supplier Id: "))
        if not my_supplier_id in [x[0] for x in mydata]:
          raise Exception("")
        my_supplier = int(my_supplier_id)
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
    my_date = ""
    while my_date == "":
      try:
        my_day = int(input("Day: "))
        my_month = int(input("Month: "))
        my_year = int(input("Year: "))
        if (not my_day in range(1,32)) or (not my_month in range(1,12+1)) or (my_year in range(2021+1)):
          raise Exception("")
        my_day = str(my_day)
        my_month = str(my_month)
        my_year = str(my_year)
        if int(my_day) < 10:
          my_day = "0" + my_day
        if int(my_month) < 10:
          my_month = "0" + my_month
        my_date = my_year + my_month + my_day
      except:
        print("Wrong input, try again.")
    mycursor.execute("select category_id, category_name from categories")
    mydata = mycursor.fetchall()
    my_category_id = 0
    my_category = -1
    while my_category == -1:
      print("Category")
      for i in mydata:
        print(str(i[0]) + " - " + i[1])
      try:
        my_category_id = int(input("Select Category: "))
        if not my_category_id in [x[0] for x in mydata]:
          raise Exception("")
        my_category = my_category_id
      except:
        print("Wrong input, try again.")
    try:
      input_query = "insert into drugs (title, sales_method, price, dose, description, manufacturer_id, supplier_id, drug_type, expiration_date,brand,category_id) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
      query_val = (my_title,SalesMethod(my_sales_method).name,str(my_price),str(my_dose),my_description,str(my_manufacturer),str(my_supplier),DrugType(my_drug_type).name,my_date,my_brand,my_category)
      mycursor.execute(input_query, query_val)
      mydb.commit()
      
      lastrowid = mycursor.lastrowid

      input_query = "insert into drug_contents(drug_id, content_item) values (%s, %s)"
      query_val = [(str(lastrowid), x) for x in my_contents]
      mycursor.executemany(input_query, query_val)
      mydb.commit()

      input_query = "insert into drug_side_effects(drug_id, side_effect_name) values (%s, %s)"
      query_val = [(str(lastrowid), x) for x in my_side_effects]
      mycursor.executemany(input_query, query_val)
      mydb.commit()
      print("--------------------------------")
      print("Drug Successfully Added")
      print("--------------------------------")
    
    except Exception as e:
      print(e)

  # Ավելացնել դասակարգիչ
  def add_category(self):
    my_name = input("Category Name: ")
    input_query = "insert into categories (category_name) values (%s)"
    query_val = (my_name,)
    mycursor.execute(input_query,query_val)
    mydb.commit()
    print("--------------------------------")
    print("Category Successfully Added")
    print("--------------------------------")
  
  # Ավելացնել արտադրողը
  def add_manufacturer(self):
    my_contact_name = input("Contact Name: ")
    my_address = input("Address: ")
    my_phone = input("Phone: ")
    my_country = input("Country: ")
    input_query = "insert into manufacturers (contact_name, address, phone, country) values (%s, %s, %s, %s)"
    query_val = (my_contact_name, my_address, my_phone, my_country)
    mycursor.execute(input_query,query_val)
    mydb.commit()
    print("--------------------------------")
    print("Manufacturer Successfully Added")
    print("--------------------------------")

  # Ավելացնել ներմուծողը
  def add_supplier(self):
    my_contact_name = input("Contact Name: ")
    my_address = input("Address: ")
    my_phone = input("Phone: ")
    my_country = input("Country: ")
    input_query = "insert into suppliers (contact_name, address, phone, country) values (%s, %s, %s, %s)"
    query_val = (my_contact_name, my_address, my_phone, my_country)
    mycursor.execute(input_query,query_val)
    mydb.commit()
    print("--------------------------------")
    print("Supplier Successfully Added")
    print("--------------------------------")

  # Ավելացնել դեղատան ցանցը
  def add_pharmacy_network(self):
    my_website_link = input("Website Link: ")
    input_query = "insert into pharmacy_networks (website_link) values (%s)"
    query_val = (my_website_link,)
    mycursor.execute(input_query,query_val)
    mydb.commit()
    print("--------------------------------")
    print("Pharmacy Network Successfully Added")
    print("--------------------------------")
  
  # Ավելացման գործողություն
  def insert_instruction(self,index):
    answer = input("Are you want to insert a new item?[Y/N]")
    if answer in ["y","yes","Y","YES"]:
      if index == 1:
        self.add_pharmacy()
      elif index == 2:
        self.add_category()
      elif index == 5:
        self.add_drug()
      elif index == 3:
        self.add_manufacturer()
      elif index == 4:
        self.add_supplier()
      elif index == 6:
        self.add_pharmacy_network()
      else:
        self.instruction_case_2(index)
    self.check_index(index)

# Printer (Տպիչ) գործողություն
class Printer:
  # Արտածել ըստ ինդեքսի (փնտրել որ աղյուսակից պիտի արտածվի)
  def print(data, index):
    if index == 1:
      Printer.print_pharmacy(data)
    elif index == 2:
      Printer.print_category(data)
    elif index == 3:
      Printer.print_manufacturer(data)
    elif index == 4:
      Printer.print_supplier(data)
    elif index == 5:
      Printer.print_drug(data)
    elif index == 6:
      Printer.print_pharmacy_network(data)
  # Արտածել դեղատան տվյալները
  def print_pharmacy(data):
    mycursor.execute("select website_link from pharmacy_networks where pharmacy_network_id = %s",(str(data[4]),))
    mydata = mycursor.fetchall()
    website_link = mydata[0][0] if (len(mydata) > 0) else "---"
    mycursor.execute("select C1.title, C2.pharmacy_id from drugs C1 inner join drug_in_pharmacy C2 on C1.drug_id = C2.drug_id where C2.pharmacy_id = %s",(str(data[0]),))
    mydata = mycursor.fetchall()
    drugs = [x[0] for x in mydata]
    print("Pharmacy:", data[0])
    print("Name:", data[1])
    print("Sales Method:", data[3])
    print("Address:",data[2])
    print("Pharmacy Network Website:", website_link)
    print("Drugs:",end="")
    print(" | ".join(drugs))
  # Արտածել արտադրողի տվյալները
  def print_manufacturer(data):
    print("Manufacturer:",data[0])
    Printer.print_person(data)
  # Արտածել ներմուծողի տվյալները
  def print_supplier(data):
    print("Supplier:",data[0])
    Printer.print_person(data)
  # Արտածել մարդու տվյալները (արտադրողի և ներմուծողի ընդհանուր կոդի հատվածը)
  def print_person(data):
    print("Contact Name:", data[1])
    print("Address:", data[2])
    print("Phone:", data[3])
    print("Country:",data[4])
  # Արտածել դասակարգչի տվյալները
  def print_category(data):
    print("Category:",data[0])
    print("Category Name:",data[1])
  # Արտածել դեղատան ցանցի տվյալները
  def print_pharmacy_network(data):
    print("Pharmacy Network:", data[0])
    print("Website Link:", data[1])
  # Արտածել դեղի տվյալները
  def print_drug(data):
    mycursor.execute("select contact_name from manufacturers where manufacturer_id = %s",(str(data[6]),))
    mydata = mycursor.fetchall()
    manufacturer_name = mydata[0][0] if (len(mydata) > 0) else "---"

    mycursor.execute("select contact_name from suppliers where supplier_id = %s",(str(data[7]),))
    mydata = mycursor.fetchall()
    supplier_name = mydata[0][0] if (len(mydata) > 0) else "---"

    mycursor.execute("select category_name from categories where category_id = %s",(str(data[11]),))
    mydata = mycursor.fetchall()
    category_name = mydata[0][0] if (len(mydata) > 0) else "---"

    mycursor.execute("select content_item from drug_contents where drug_id = %s",(str(data[0]),))
    mydata = mycursor.fetchall()
    contents = [x[0] for x in mydata]

    mycursor.execute("select side_effect_name from drug_side_effects where drug_id = %s",(str(data[0]),))
    mydata = mycursor.fetchall()
    side_effects = [x[0] for x in mydata]

    print("Drug:",data[0])
    print("Title:", data[2])
    print("Sales Method:", data[1])
    print("Price:", data[3])
    print("Dose:", data[4])
    print("Description:", data[5])
    print("Manufacturer:", manufacturer_name)
    print("Supplier:",supplier_name)
    print("Contents: "," | ".join(contents))
    print("Side Effects: "," | ".join(side_effects))
    print("Drug Type:", data[8])
    print("Brand:",data[9])
    print("Expiration_date: ",data[10])
    print("Category:",category_name)

# MySearchEngine (Իմ որոնման շարժիչ) դասը
class MySearchEngine:
  # Որոնել ըստ ինդեքսի (փնտրել որ աղյուսակից պիտի որոնի)
  def search(item, index):
    if index == 1:
      return MySearchEngine.search_pharmacies(item)
    elif index == 2:
      return MySearchEngine.search_categories(item)
    elif index == 3:
      return MySearchEngine.search_manufacturers(item)
    elif index == 4:
      return MySearchEngine.search_suppliers(item)
    elif index == 5:
      return MySearchEngine.search_drugs(item)
    elif index == 6:
      return MySearchEngine.search_pharmacy_networks(item)
  # Որոնել դեղատտները
  def search_pharmacies(item):
    fake_regex = '%' + item + '%'
    sql = "select * from pharmacies where pharmacy_id = %s or sales_method like %s or name like %s or address like %s or sales_method = %s"
    val = (item, fake_regex, fake_regex, fake_regex, item)
    mycursor.execute(sql,val)
    return mycursor.fetchall()
  # Որոնել դասակարգիչները
  def search_categories(item):
    fake_regex = '%' + item + '%'
    sql = "select * from categories where category_id = %s or category_name like %s"
    val = (item, fake_regex)
    mycursor.execute(sql,val)
    return mycursor.fetchall()
  # Որոնել արտադրողները
  def search_manufacturers(item):
    fake_regex = '%' + item + '%'
    sql = "select * from categories where manufacturer_id = %s or contact_name like %s or address like %s or phone like %s or country like %s"
    val = (item, fake_regex, fake_regex, fake_regex, fake_regex)
    mycursor.execute(sql,val)
    return mycursor.fetchall()
  # Որոնել ներմուծողները
  def search_suppliers(item):
    fake_regex = '%' + item + '%'
    sql = "select * from categories where supplier_id = %s or contact_name like %s or address like %s or phone like %s or country like %s"
    val = (item, fake_regex, fake_regex, fake_regex, fake_regex)
    mycursor.execute(sql,val)
    return mycursor.fetchall()
  # Որոնել դեղատան ցանցերը
  def search_pharmacy_networks(item):
    fake_regex = '%' + item + '%'
    sql = "select * from pharmacy_networks where pharmacy_network_id = %s or website_link like %s"
    val = (item, fake_regex)
    mycursor.execute(sql,val)
    return mycursor.fetchall()
  # Որոնել դեղերը
  def search_drugs(item):
    fake_regex = '%' + item + '%'
    sql = "select * from drugs where drug_id = %s or sales_method = %s or title like %s or price = %s or dose = %s or description like %s or drug_type = %s or brand like %s"
    val = (item, item, fake_regex, item, item, fake_regex, item,fake_regex)
    mycursor.execute(sql,val)
    return mycursor.fetchall()

# Delete (ջնջել) դասը
class Delete:
  # Ջնջել ըստ ինդեքսի (փնտրել որ աղյուսակից պիտի ջնջել)
  def delete(index):
    if index == 1:
      Delete.delete_pharmacy()
    elif index == 2:
      Delete.delete_category()
    elif index == 3:
      Delete.delete_manufacturer()
    elif index == 4:
      Delete.delete_supplier()
    elif index == 5:
      Delete.delete_drug()
    elif index == 6:
      Delete.delete_pharmacy_network()
  # Ջնջել դեղատունը
  def delete_pharmacy():
    mycursor.execute("select pharmacy_id from pharmacies")
    mydata = mycursor.fetchall()
    my_id = -1
    while not my_id in [x[0] for x in mydata]:
      try:
        my_id = int(input("Select id of item for deleting: "))
        if not my_id in [x[0] for x in mydata]:
          raise Exception("")
      except:
        print("Wrong input, try again.")
    try:
      mycursor.execute("delete from pharmacies where pharmacy_id = %s",(str(my_id),))
      mydb.commit()
      mycursor.execute("delete from drug_in_pharmacy where pharmacy_id = %s",(str(my_id),))
      mydb.commit()
    except Exception as e:
      print(e)

  # Ջնջել դասակարգիչը
  def delete_category():
    mycursor.execute("select category_id from categories")
    mydata = mycursor.fetchall()
    my_id = -1
    while not my_id in [x[0] for x in mydata]:
      try:
        my_id = int(input("Select id of item for deleting: "))
        if not my_id in [x[0] for x in mydata]:
          raise Exception("")
      except:
        print("Wrong input, try again.")
    mycursor.execute("delete from categories where category_id = %s",(str(my_id),))
    mydb.commit()

  # Ջնջել արտադրողը
  def delete_manufacturer():
    mycursor.execute("select manufacturer_id from manufacturers")
    mydata = mycursor.fetchall()
    my_id = -1
    while not my_id in [x[0] for x in mydata]:
      try:
        my_id = int(input("Select id of item for deleting: "))
        if not my_id in [x[0] for x in mydata]:
          raise Exception("")
      except:
        print("Wrong input, try again.")
    mycursor.execute("delete from manufacturers where manufacturer_id = %s",(str(my_id),))
    mydb.commit()

  # Ջնջել ներմուծողը
  def delete_supplier():
    mycursor.execute("select supplier_id from suppliers")
    mydata = mycursor.fetchall()
    my_id = -1
    while not my_id in [x[0] for x in mydata]:
      try:
        my_id = int(input("Select id of item for deleting: "))
        if not my_id in [x[0] for x in mydata]:
          raise Exception("")
      except:
        print("Wrong input, try again.")
    mycursor.execute("delete from suppliers where supplier_id = %s",(str(my_id),))
    mydb.commit()

  # Ջնջել դեղը
  def delete_drug():
    try:
      mycursor.execute("select drug_id from drugs")
      mydata = mycursor.fetchall()
      my_id = -1
      while not my_id in [x[0] for x in mydata]:
        try:
          my_id = int(input("Select id of item for deleting: "))
          if not my_id in [x[0] for x in mydata]:
            raise Exception("")
        except:
          print("Wrong input, try again.")
      mycursor.execute("delete from drugs where drug_id = %s",(str(my_id),))
      mydb.commit()
      mycursor.execute("delete from drug_contents where drug_id = %s",(str(my_id),))
      mydb.commit()
      mycursor.execute("delete from drug_side_effects where drug_id = %s",(str(my_id),))
      mydb.commit()
      mycursor.execute("delete from drug_in_pharmacy where drug_id = %s",(str(my_id),))
      mydb.commit()
    except Exception as e:
      print(e)
    
  # Ջնջել դեղատան ցանցը
  def delete_pharmacy_network():
    mycursor.execute("select pharmacy_network_id from pharmacy_networks")
    mydata = mycursor.fetchall()
    my_id = -1
    while not my_id in [x[0] for x in mydata]:
      try:
        my_id = int(input("Select id of item for deleting: "))
        if not my_id in [x[0] for x in mydata]:
          raise Exception("")
      except:
        print("Wrong input, try again.")
    mycursor.execute("delete from pharmacy_networks where pharmacy_network_id = %s",(str(my_id),))
    mydb.commit()

UI()