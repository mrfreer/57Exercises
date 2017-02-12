#Expert system car maintenance
carsilent = input("Is your car silent when you turn the key? Y for yes")
if carsilent == 'Y':
    batteries = input("Are the battery terminals corroded?")
    if batteries == 'Y':
        print("Clean terminals and try again.")
    else:
        print("Replace cables and try again.")
else:
    clickingnoise = input("Does the car make a clicking noise?")
    if clickingnoise == 'Y':
        print("Replace the battery.")
    else:
        crankup = input("Does the car crank up but fail to start?")
        if crankup == 'Y':
            print("Check spark plug connections.")
        else:
            engineidle = input("Does the engine start and then die?")
            if engineidle == 'Y':
                fuelinjection = input('Does your car have fuel injection?')
                if fuelinjection == 'Y':
                    print('Get it in for service.')
                else:
                    print('Check to ensure the choke is opening and closing.')