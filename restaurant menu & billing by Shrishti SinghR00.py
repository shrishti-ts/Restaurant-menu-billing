print("WELCOME TO BURGER'Z HEADD")
sum1=0
sum2=0
Food_selected = []
Drinks_selected = []
def print_receipt(sum1, sum2, Food_selected, Drinks_selected):
    print(" ")
    print("--------------------------*RECEIPT*----------------------------")
    print(" ")
    print("Your Food order: ")
    print("-------------------------------------------------------------")
    for i in range(len(Food_selected)):
    
    #print(Food_selected[i])
        print(i+1, ")",foods_list[Food_selected[i]], ": Rs", foods[Food_selected[i]])
    print(" ")
    print(" ")
    print("Your Drink order: ")
    print("-------------------------------------------------------------")
    for j in range(len(Drinks_selected)):
    #print(Drinks_selected[j])
        print(j+1, ")",drinks_list[Drinks_selected[j]], ": Rs", drinks[Drinks_selected[j]])
    print(" ")
    print("your total bill is = Rs",sum1+sum2)
    return()

foods={'101':400,'102':350,'103':350,'104':200,'105':250,'106':200}
drinks={'201':150,'202':150,'203':75,'204':80,'205':100,'206':50}
foods_list={'101':"Vegan BBQ Tofu burger",'102':"Peach burger",'103':"Portobello burger",'104':"Baked barocolli burger",'105':"Chicken burger",'106':"Veggi cheese burger"}
drinks_list={'201':"Modern tuscan reds",'202':"A manhattan",'203':"Coke",'204':"Pepsi",'205':"Berry Mojito",'206':"Limca"}
lst1=list(foods.keys())
lst2=list(drinks.keys())
lst3=list(foods_list.keys())
#print(lst1)
while True:
    print("                     **Meals**                  ")
    print("---------------------------------------------------------")
    print("Vegan BBQ Tofu burger                @ 400 rs. {code:101}")
    print("Peach burger                         @ 350 rs. {code:102}")
    print("Portobello burger                    @ 350 rs. {code:103}")
    print("Baked brocolli burger                @ 200 rs. {code:104}")
    print("Chicken burger                       @ 250 rs. {code:105}")
    print("Veggie cheese burger                 @ 200 rs. {code:106}")
    print("press E for exit")
    order=input("Enter your order code from Meals: ")
   
    if order in lst1:
        sum1=sum1 + foods[order]
        
        Food_selected.append(order)
        print(Food_selected)
        print("Your order value from Meals: " ,sum1)
    elif order=='E':
        break
    else:
        print("please enter right item from the menu")
#print(lst2)
while True:
    print("                      **DRINKS**                ")
    print("---------------------------------------------------------")
    print("Modern tuscan reds                   @150 rs.  {code:201}")
    print("A manhattan                          @150 rs.  {code:202}")
    print("Coke                                 @75 rs.   {code:203}")
    print("Pepsi                                @80 rs.   {code:204}")
    print("Berry Mojito                         @100 rs.  {code:205}")
    print("Limca                                @50 rs.   {code:206}")
    print("press E for exit")
    order=input("Enter your order code from Drinks: ")
    if order in lst2:
        sum2=sum2+drinks[order]
        Drinks_selected.append(order)
        print(Drinks_selected)
        print("Your order value from Drinks: ",sum2)
    elif order=='E':
        break
    else:
        print("please enter right item from the menu")
print_receipt(sum1, sum2, Food_selected, Drinks_selected)
        