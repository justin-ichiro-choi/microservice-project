

def main_menu(stations, routes):

    print("Transit Route")
    print("")
    print("Statistics")
    print("Number of Stations: " + str(len(stations)))
    print("Number of Routes: " + str(len(routes)))
    print("Tickets Sold: 0")
    print(" ")
    print("Please note that information from this page is not importable. Please feel free to enter then numbers provided to navigate the menu!")
    print("1. Routes Page")
    print("2. Stations Page")
    print("3. Quick Add Station")
    print("4. Quick Add Route")

    print("5. Exit")
    print("")
    choice = input("Enter your choice: ")

    if choice == '1':
        route_submenu(stations, routes)
    elif choice == '2':
        station_submenu(stations)
    elif choice == '3':
        add_station(stations)
    elif choice == '4':
        print("Test")
    elif choice == '5':
        exit()
    else:
        print("Invalid choice")
        main_menu(stations, routes)

def station_submenu(stations_list):
    print("")
    print("--------------------------------------------------------")
    print("Here is the page to add, remove, or edit stations.")
    print("1. Add New Station. ")
    print("2. Edit Existing Station.")
    print("3. Remove Existing Station.")
    print("4. View All Stations.")
    print("5. Back to Main Menu")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_station(stations_list)
    elif choice == '2':
        edit_station(stations_list)
    elif choice == '3':
        remove_station(stations_list)
    elif choice == '4':
        view_stations(stations_list, True)
    elif choice == '5':
        main_menu(stations, routes)
    else:
        print("Invalid choice")
        station_submenu(stations_list)

def add_station(station_list):
    station_name = input("Enter the name of the station that you wish to enter into the system: ")
    station_description = input("Please enter a short description of the station: ")
    station_routes = []

    station_list.append([station_name, station_description, station_routes])

    station_submenu(station_list)

def view_stations(station_list, redirect):

    print("")
    print("Here is a list of all stations")
    
    for station in station_list:
        print("")
        print("Name: " + station[0])
        print("Description: " + station[1])

        if not station[2]:
            print("Station is not assigned to any route")
        else:
            print("Station is part of: " + ",".join(station[2]))
    
    if redirect:
        station_submenu(station_list)

def remove_station(station_list):
    station_name = input("Enter the name of the station that you wish to remove from the system: ")
    for station in station_list:
        if station_name in station:
            station_list.remove(station)
            print("Station Removed!")
    

    station_submenu(station_list)
    
def edit_station(station_list):
    station_name = input("Enter the name of the station that you wish to edit: ")
    new_description = input("Enter a new description: ")

    for station in station_list:
        if station[0] == station_name:
            station[1] = new_description
            print(station_name + "Station Edited!")
    
    
    station_submenu(station_list)

def route_submenu(stations_list, routes_list):
    print("")
    print("--------------------------------------------------------")
    print("Here is the page to add, remove, or edit routes.")
    print("1. Add New Route. ")
    print("2. Edit Existing Route.")
    print("3. Remove Existing Route.")
    print("4. View All Routes.")
    print("5. Back to Main Menu")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_route(stations_list, routes_list)
    elif choice == '2':
        edit_route(stations_list, routes_list)
    elif choice == '3':
        remove_route(stations_list, routes_list)
    elif choice == '4':
        view_routes(stations_list, routes_list)
    elif choice == '5':
        main_menu(stations, routes)
    else:
        print("Invalid choice")
        route_submenu(stations_list, routes_list)

def add_route(stations_list, routes_list):
    
    new_route = []

    name = input("Enter the name of the route: ")
    new_route.append(name)
    
    print("")
    print("Here are the stations added in our database")

    view_stations(stations_list, False)

    while True:

        station = input("Enter the name of a station one by one to create a route. (type 'quit' to exit): ")

        if station == "quit":
            break
        elif check_station_names(stations_list, station) == False:
            print("Station not found")
        else:
            new_route.append(station)
            print(station + " added!" )
        
        print("")
    
    routes_list.append(new_route)
    route_submenu(stations_list, routes_list)

def view_routes(stations_list, routes_list):
    for route in routes_list:
        print(" ")
        print("Route:  " + " -- ".join(route))
    
    route_submenu(stations_list, routes_list)

def check_station_names(list_of_lists, name):
    for station in list_of_lists:
        if name in station:
            return True
    return False

if __name__ == "__main__":
    
    stations = [["Downtown", "Middle of Town", []], ["Redrum", "Middle of Nowhere", []]]
    routes = []

    main_menu(stations, routes)
