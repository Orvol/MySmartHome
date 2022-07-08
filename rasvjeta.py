from datetime import datetime




""" broj_lampi_u_kuci = int(input("Molimo unesite broj lampi: "))
lampa = [1] * broj_lampi_u_kuci
while 1 in lampa:    
    lightIndex = int(input(f"{lampa} Koju lampu želite upaliti ? ")) - 1
    if lightIndex > 0 and lampa.index(1) != lightIndex-1:
        print("Ne možete upaliti željenu lampu")
        continue
    lampa[lightIndex] = 1 - lampa[lightIndex]
print(f"{lampa} success !!") """



numberOfLights = int(input("Please enter a number of lights: "))
lights         = [1] * numberOfLights
while 1 in lights:    
    lightIndex = int(input(f"{lights} toggle which light ? ")) - 1
    if lightIndex > 0 and lights.index(1) != lightIndex-1:
        print("You cannot toggle that light")
        continue
    lights[lightIndex] = 1 - lights[lightIndex]
print(f"{lights} success !!")