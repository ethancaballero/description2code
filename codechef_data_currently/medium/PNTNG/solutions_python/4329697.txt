def main():
    dimensions = raw_input()
    n,m,h = [int(i) for i in dimensions.split(' ')]
    layers = []
    for i in range(1,h+1):
        t_c = raw_input()
        t,c = [int(i) for i in t_c.split(' ')]
        layers.append([t,c])

    layers = sorted(layers, key=lambda layer: layer[1])
    total = n*m 
    cost = 0
    painted = 0
    flag = False
    for layer in layers:
        max_cost = layer[0]*layer[1]
        if total-painted < layer[0]:
            cost += (total-painted)*layer[1]
        else:
            cost += max_cost
        painted += layer[0]
        if (painted >= total):
            flag = True
            break
    if flag:
        print cost
    else:
        print "Impossible"
    
    

if __name__ == '__main__':
    main()
