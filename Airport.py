

# Loop Code
run_again = "y"
while (run_again == "y"):

    # Introduction
    print("Welcome to Cardiff Airport, we hope you enjoy your flight and you will travel with us again.")
    raw_flight = input("Please enter the details of your flight specification below:" '\n').upper()
     # String Splitting the raw_flight variable and assigning them to other relevant variables for the flight
    flight_dest, bag_total, passenger_age, meal_type, seat_class = raw_flight[:3], int(raw_flight[4]), int(raw_flight[6:8]), raw_flight[-3], raw_flight[-1]

    # Starting The Total Cost
    total_flight_cost = 0


    # Part A: User Input and Flight Destination
     # Defining full desitnation name and costs of both flights
    AMS_flight = "Schiphol, Amsterdam"
    GLA_flight = "Glasgow, Scotland"
    AMS_flight_cost = 150.00
    GLA_flight_cost = 80.00
     # Determining which flight the user chose and giving the relevant destination 
    if flight_dest == "AMS":
        total_flight_cost += AMS_flight_cost
        print("Your destination is " + AMS_flight + ".")
    elif flight_dest == "GLA":
        total_flight_cost += GLA_flight_cost
        print("Your destination is " + GLA_flight + ".")    
    else:
        print("Please check your flight specification again, you might have mistyped the flight destination")


    # Part B: Baggage Costs
     # Defining the total cost of baggage
    total_bag_costs = 0
     # Working out the total number of baggage 
    print("You have " + str(bag_total) + " bag(s) in total.")
    if bag_total == 0 or bag_total == 1:
        print("Good news, you have not incurred any baggage costs")
    elif 1 < bag_total <= 3:
        total_bag_costs = int(bag_total - 1) * 10
        print("You have inccured some baggage fees.")
    else:
        print("You cannot bring this many bags on the flight, lease check your flight specification again, you might have mistyped your bag total")
     # Printing out total baggage cost   
    print("Your total amount for bags is £" + '{0:.2f}'.format(total_bag_costs))


    # Part C: Child Discount
     # Seeing if passenger is eligible for child discount
    child_discount = 0 
    if passenger_age <= 15:
        print("You qualify for the child discount")
        if flight_dest == "AMS":
            child_discount = AMS_flight_cost / 2
        else:
            child_discount = GLA_flight_cost / 2
    elif passenger_age > 15 and passenger_age <= 99:
        print("You qualify for the full adult fare") 
    else:
        print("Please check your flight specification again, you might have mistyped your age")


    # Part E: Seating Class
    seat_total = 0 
    if passenger_age <= 15:
        if seat_class == "F":
            if flight_dest == "AMS":
                seat_total = int(child_discount) * 6
            elif flight_dest == "GLA":
                seat_total = int(child_discount) * 6
        elif seat_class == "E":
            if flight_dest == "AMS":
                seat_total = child_discount
            elif flight_dest == "GLA":
                seat_total = child_discount
    elif passenger_age > 15 and passenger_age <= 99:
        if seat_class == "F":
            if flight_dest == "AMS":
                seat_total = int(AMS_flight_cost) * 6
            elif flight_dest == "GLA":
                seat_total = int(GLA_flight_cost) * 6
        elif seat_class == "E":
            if flight_dest == "AMS":
                seat_total = AMS_flight_cost
            elif flight_dest == "GLA":
                seat_total = GLA_flight_cost
        


    # Part D: Meals
     # Defining costs of meals
    standard_meal = 10.00
    vegetarian_meal = 12.00
    standard_meal_child = 7.50
    vegetarian_meal_child = 9.50
    no_meal = 0
    meal_total = 0 
     # Working out costs of passenger meals and if there is a child discount
    if meal_type == "N":
        meal_total += no_meal
        print("You have chosen to have no meal on the flight")
    elif seat_class == "F":
        if meal_type == "S":
            print("You have chosen a Standard Meal")
        elif meal_type == "V":
            print("You have chosen a Vegeterian Meal")
        meal_total = 0
        print("Since you are flying first class you have the privilege to have free meals")    
    elif meal_type == "S":
        if passenger_age <= 15:
            meal_total += (standard_meal_child)
            print("You have chosen a Standard Meal and you qualify for a child discount")
        elif passenger_age > 15 and passenger_age <= 99:
            meal_total += standard_meal
            print("You have chosen a Standard Meal")
    elif meal_type == "V":
         if passenger_age <= 15:
            meal_total += (vegetarian_meal_child)
            print("You have chosen a Vegeterian Meal and you qualify for a child discount")
         elif passenger_age > 15 and passenger_age <= 99:
            meal_total += vegetarian_meal
            print("You have chosen a Vegeterian Meal")
    else:
        print("Please check your flight specification again, you might have mistyped your meal preference")
    # Printing total meal costs    
    print("Your total amount for meals is £" + '{0:.2f}'.format(meal_total))


    # Part F: Total Cost and Output
    if flight_dest == "AMS":
        total_flight_cost += AMS_flight_cost
    elif flight_dest == "GLA":
        total_flight_cost += GLA_flight_cost

    total_flight_cost = seat_total + total_bag_costs + meal_total
    print("The total amount of money for your flight is £" + '{0:.2f}'.format(total_flight_cost) + " we hope you enjoy your flight and we look forward to have you travel with us in the future.")
    run_again = input("Would you like to retype your flight specification or enter a new flight specification? [y/n]" + '\n').lower()


        
        
        
        





