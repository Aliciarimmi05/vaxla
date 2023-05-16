import os
import vaxla

def main () :
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\t-växlare-\n")

    pris = input("\tMata in pris på varan i kr: ")
    exChangenow(int(pris), int(inbet))

    #definerar växlingdunktion som skriver ut växling
    def exChangeNow(priset, inbetalning):
        if priset > inbetalning:
            print("\n\tFattas pengar! ")
        else:
            vaxel_tillbaka_dictonary = vaxla.get_exchange_dict(inbetalning, priset)

            print("\n\t---------------------------------------------------")
            print("\tVäxel tillbaka:n")
            print("\tAntal 500 lappar: " + str(vaxel_tillbaka_dictonary[500]))
            print("\tAntal 100 lappar: " + str(vaxel_tillbaka_dictonary[100]))
            print("\tAntal 50 lappar: " + str(vaxel_tillbaka_dictonary[50]))
            print("\tAntal 20 lappar: " + str(vaxel_tillbaka_dictonary[20]))
            print("\tAntal 10 lappar: " + str(vaxel_tillbaka_dictonary[10]))
            print("\tAntal 5 lappar: " + str(vaxel_tillbaka_dictonary[5]))
            print("\tAntal 1 lappar: " + str(vaxel_tillbaka_dictonary[1]) + "\n\n")

            #print ("test = " + str(vaxel_tillbaka_dictonary))


    main()