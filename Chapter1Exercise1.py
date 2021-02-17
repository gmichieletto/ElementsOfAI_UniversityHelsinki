#intermediate

def main():
    portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

    port1 = 0
    for port2 in range(1, 5):
        for port3 in range(1, 5):
            for port4 in range(1, 5):
                for port5 in range(1, 5):
                    route = [port1, port2, port3, port4, port5]
                    if len( set(route)) == 5 :
                    # do not modify the print statement
                        print(' '.join([portnames[i] for i in route]))

main()

print("---------------")

#advance

portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]
def permutations(route, ports):
    if len(ports) < 1:
        print(' '.join([portnames[i] for i in route]))
    else:
        for i in range(len(ports)):
            permutations(route+[ports[i]], ports[:i]+ports[i+1:])
 
permutations([0], list(range(1, len(portnames))))
