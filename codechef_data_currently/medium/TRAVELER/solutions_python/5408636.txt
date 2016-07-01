def main():
    #read no of cities
    n = input()
    #read cities
    city = raw_input().split()
    #read no of routes
    m = input()
    mapp = {}
    #zero out map of routes
    for c in city:
        mapp[c] = [0]*n
    #populate map with available routes by index
    while m:
        m -= 1
        road = raw_input().split()
        elem = mapp[road[0]]
        elem[city.index(road[1])] = int(road[2])
        mapp[road[0]] = elem
    #read no of itineraries
    itins = input()
    #process each itinerary
    while itins:
        itins -= 1
        #read a route
        route = raw_input().split()
        total = 0
        #zero out visited cities
        v = [0]*n
        #if only 1 city in route, print 0
        if route[0] == '1':
            if route[-1] in city:
                print total
            #if city not available, print error
            else:
                print "ERROR"
        else:
            #for each city in itinerary
            for r in range(1, len(route)):
                #if city not available or has been visited, print error
                if (route[r] not in city) or v[city.index(route[r])]:
                    total = "ERROR"
                    break
                #if first city in line, visit and move on, otherwise
                elif r > 1:
                    #check if there is a route from the previous city to the current city in the map
                    if mapp[route[r-1]][city.index(route[r])]:
                        #add to totall
                        total += mapp[route[r-1]][city.index(route[r])]
                    #if no route available, print error
                    else:
                        total = "ERROR"
                        break
                #mark as visited
                v[city.index(route[r])] = 1
            print total
main()