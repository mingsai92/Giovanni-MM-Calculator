# written by Giovanni on 4/23/2024
# from numpy import log as ln
# import tone
# from tone import Tone
# import winsound

import math
import os
import time

amudictionary = {"H":"1.008","He":"4.003","Li":"6.941","Be":"9.012","B":"10.81","C":"12.011","N":"14.007","O":"15.999","F":"18.998",
                 "Ne":"20.179","Na":"22.990","Mg":"24.305","Al":"26.982","Si":"28.086","P":"30.974","S":"32.067","Cl":"35.453",
                 "Ar":"39.948","K":"39.098","Ca":"40.078","Sc:":"44.956","Ti":"47.88","V":"50.942","Cr":"51.996","Mn":"54.938",
                 "Fe":"55.847","Co":"58.933","Cu":"63.546","Zn":"65.39","Ga":"69.723","Ge":"72.61","As":"74.922","Se":"78.96",
                 "Br":"79.904","Kr":"83.80","Rb":"85.468","Sr":"87.62","Y":"88.906","Zr":"91.224","Nb":"92.906","Mo":"95.94",
                 "Tc":"98","Ru":"101.07","Rh":"102.91","Pd":"106.42","Ag":"107.87","Cd":"112.41","In":"114.82","Sn":"118.71",
                 "Sb":"121.76","Te":"127.60","I":"126.90","Xe":"131.29","Cs":"132.91","Ba:":"137.33","La":"138.91","Ce":"140.12",
                 "Pr":"140.91","Nd":"144.24","Pm":"145","Sm":"150.36","Eu":"151.96","Gd":"157.25","Tb":"158.93","Dy":"162.50",
                 "Ho":"164.93","Er":"167.26","Tm":"168.93","Yb":"173.04","Lu":"174.97","Hf":"178.49","Ta":"180.95","W":"183.85",
                 "Re":"186.21","Os":"190.2","Ir":"192.22","Pt":"195.08","Au":"196.97","Hg":"200.59","Tl":"204.38","Pb":"207.2",
                 "Bi":"208.98","Po":"209","At":"210","Rn":"222"}

clear=lambda:os.system('cls')
clear()
print()
print("\t","\t","Welcome to molar mass calculator")
time.sleep(1.2)
print()
num_diff_atoms =int(input(" How many elements in the molecule or formula unit? "))



if num_diff_atoms==1:
    elem_1 = (input(" What is the first element?: "))
    num_elem1 =int(input(" How many are there? " ))
    print('\t'," There are ",num_elem1," ",elem_1)
    '\n'
    for i in amudictionary.keys():
        if i == elem_1:
            print(elem_1 +" weighs "+ amudictionary.get(i)+" amu.")
            mass=amudictionary.get(i)
            mass=float(mass)
            # print(type(mass))
            '\n'
            print(' The total MM is: ',num_elem1*mass)
            time.sleep(5)
elif num_diff_atoms==2:
    elem_1 =(input(" What is the first element?: "))
    num_elem1 =int(input(" How many are there? " ))
    elem_2 =(input(" What is the second element?: "))
    num_elem2 =int(input(" How many are there? " ))
    print('\t'," There are ",num_elem1," ",elem_1, "and ",num_elem2," ",elem_2)
    '\n'
    for i in amudictionary.keys():
        if i == elem_1:
            print(elem_1 +" weighs "+ amudictionary.get(i)+" amu.")
            mass=amudictionary.get(i)
            mass=float(mass)
            # print(type(mass))
            '\n'                        
            print('The partial molar mass of elem_1 is: ', num_elem1*mass)   
    for i in amudictionary.keys():
        if i == elem_2:
            print(elem_2 +" weighs "+ amudictionary.get(i)+" amu.")
            mass2=amudictionary.get(i)
            mass2=float(mass2)
            # print(type(mass2))
            '\n'
            print('The partial molar mass of elem_2 is: ', num_elem2*mass2)
            '\n'
            print(' The total MM is: ',num_elem1*mass+num_elem2*mass2)
            time.sleep(5)
elif num_diff_atoms==3:
    elem_1 =(input(" What is the first element?: "))
    num_elem1 =int(input(" How many are there? " ))
    elem_2 =(input(" What is the second element?: "))
    num_elem2 =int(input(" How many are there? " ))
    elem_3 =(input(" What is the third element?: "))
    num_elem3 =int(input(" How many are there? " ))    
    print('\t'," There are ",num_elem1," ",elem_1, "and ",num_elem2," ",elem_2,"and ",num_elem3," ",elem_3)
    '\n'
    for i in amudictionary.keys():
            if i == elem_1:
                print(elem_1 +" weighs "+ amudictionary.get(i)+" amu.")
                mass=amudictionary.get(i)
                mass=float(mass)
                # print(type(mass))
                '\n'
                print('The partial molar mass of elem_1 is: ', num_elem1*mass)    
    for i in amudictionary.keys():
            if i == elem_2:
                print(elem_2 +" weighs "+ amudictionary.get(i)+" amu.")
                mass2=amudictionary.get(i)
                mass2=float(mass2)
                # print(type(mass2))
                '\n'
                print('The partial molar mass of elem_2 is: ', num_elem2*mass2)                            
    for i in amudictionary.keys():
            if i == elem_3:
                print(elem_3 +" weighs "+ amudictionary.get(i)+" amu.")
                mass3=amudictionary.get(i)
                mass3=float(mass3)
                # print(type(mass3))
                '\n'
                print('The partial molar mass of elem_3 is: ', num_elem3*mass3)
                '\n'
                print(' The total MM is: ',num_elem1*mass+num_elem2*mass2+num_elem3*mass3)
                time.sleep(5)
elif num_diff_atoms==4:
    elem_1 =(input(" What is the first element?: "))
    num_elem1 =int(input(" How many are there? " ))
    elem_2 =(input(" What is the second element?: "))
    num_elem2 =int(input(" How many are there? " ))
    elem_3 =(input(" What is the third element?: "))
    num_elem3 =int(input(" How many are there? " ))
    elem_4 =(input(" What is the forth element?: "))
    num_elem4 =int(input(" How many are there? " ))
    print('\t'," There are ",num_elem1," ",elem_1, "and ",num_elem2," ",elem_2,"and ",num_elem3," ",elem_3,"and ",num_elem4," ",elem_4)
    '\n'
    for i in amudictionary.keys():
            if i == elem_1:
                print(elem_1 +" weighs "+ amudictionary.get(i)+" amu.")
                mass=amudictionary.get(i)
                mass=float(mass)
                # print(type(mass))
                '\n'
                print('The partial molar mass of elem_1 is: ', num_elem1*mass)    
    for i in amudictionary.keys():
            if i == elem_2:
                print(elem_2 +" weighs "+ amudictionary.get(i)+" amu.")
                mass2=amudictionary.get(i)
                mass2=float(mass2)
                # print(type(mass2))
                '\n'
                print('The partial molar mass of elem_2 is: ', num_elem2*mass2)   
    for i in amudictionary.keys():
            if i == elem_3:
                print(elem_3 +" weighs "+ amudictionary.get(i)+" amu.")
                mass3=amudictionary.get(i)
                mass3=float(mass3)
                # print(type(mass3))
                '\n'
                print('The partial molar mass of elem_3 is: ', num_elem3*mass3)                           
    for i in amudictionary.keys():
            if i == elem_4:
                print(elem_4 +" weighs "+ amudictionary.get(i)+" amu.")
                mass4=amudictionary.get(i)
                mass4=float(mass4)
                # print(type(mass4))
                '\n'
                print('The partial molar mass of elem_4 is: ', num_elem4*mass4)
                '\n'
                print(' The total MM is: ',num_elem1*mass+num_elem2*mass2+num_elem3*mass3+num_elem4*mass4)
                time.sleep(5)
elif num_diff_atoms==5:
    elem_1 =(input(" What is the first element?: "))
    num_elem1 =int(input(" How many are there? " ))
    elem_2 =(input(" What is the second element?: "))
    num_elem2 =int(input(" How many are there? " ))
    elem_3 =(input(" What is the third element?: "))
    num_elem3 =int(input(" How many are there? " ))
    elem_4 =(input(" What is the forth element?: "))
    num_elem4 =int(input(" How many are there? " ))
    elem_5 =(input(" What is the fifth element?: "))
    num_elem5 =int(input(" How many are there? " ))
    print('\t'," There are ",num_elem1," ",elem_1, "and ",num_elem2," ",elem_2,"and ",num_elem3," ",elem_3,"and ",num_elem4," ",elem_4," ",num_elem5," ",elem_5)
    '\n'
    for i in amudictionary.keys():
            if i == elem_1:
                print(elem_1 +" weighs "+ amudictionary.get(i)+" amu.")
                mass=amudictionary.get(i)
                mass=float(mass)
                # print(type(mass))
                '\n'
                print('The partial molar mass of',elem_1,'is: ', num_elem1*mass)    
    for i in amudictionary.keys():
            if i == elem_2:
                print(elem_2 +" weighs "+ amudictionary.get(i)+" amu.")
                mass2=amudictionary.get(i)
                mass2=float(mass2)
                # print(type(mass2))
                '\n'
                print('The partial molar mass of',elem_2,'is: ', num_elem2*mass2)   
    for i in amudictionary.keys():
            if i == elem_3:
                print(elem_3 +" weighs "+ amudictionary.get(i)+" amu.")
                mass3=amudictionary.get(i)
                mass3=float(mass3)
                # print(type(mass3))
                '\n'
                print('The partial molar mass of',elem_3,'is: ', num_elem3*mass3)                           
    for i in amudictionary.keys():
            if i == elem_4:
                print(elem_4 +" weighs "+ amudictionary.get(i)+" amu.")
                mass4=amudictionary.get(i)
                mass4=float(mass4)
                # print(type(mass4))
                '\n'
                print('The partial molar mass of',elem_4,'is: ', num_elem4*mass4)
                '\n'
    for i in amudictionary.keys():
            if i == elem_5:
                print(elem_5 +" weighs "+ amudictionary.get(i)+" amu.")
                mass5=amudictionary.get(i)
                mass5=float(mass5)
                # print(type(mass5))
                '\n'
                print('The partial molar mass of',elem_5,'is: ', num_elem5*mass5)
                '\n'
                print('\t',' The total MM is: ',num_elem1*mass+num_elem2*mass2+num_elem3*mass3+num_elem4*mass4+num_elem5*mass5)
                time.sleep(5)
elif num_diff_atoms==6:
    elem_1 =(input(" What is the first element?: "))
    num_elem1 =int(input(" How many are there? " ))
    elem_2 =(input(" What is the second element?: "))
    num_elem2 =int(input(" How many are there? " ))
    elem_3 =(input(" What is the third element?: "))
    num_elem3 =int(input(" How many are there? " ))
    elem_4 =(input(" What is the forth element?: "))
    num_elem4 =int(input(" How many are there? " ))
    elem_5 =(input(" What is the fifth element?: "))
    num_elem5 =int(input(" How many are there? " ))
    elem_6 =(input(" What is the sixth element?: "))
    num_elem6 =int(input(" How many are there? " ))
    print('\t'," There are ",num_elem1," ",elem_1,"and",num_elem2," ",elem_2,"and",num_elem3," ",elem_3,"and",num_elem4," ",elem_4,"and",num_elem5," ",elem_5," and",num_elem6," ",elem_6)
    '\n'
    for i in amudictionary.keys():
            if i == elem_1:
                print(elem_1 +" weighs "+ amudictionary.get(i)+" amu.")
                mass=amudictionary.get(i)
                mass=float(mass)
                # print(type(mass))
                '\n'
                print('The partial molar mass of',elem_1,'is: ', num_elem1*mass)    
    for i in amudictionary.keys():
            if i == elem_2:
                print(elem_2 +" weighs "+ amudictionary.get(i)+" amu.")
                mass2=amudictionary.get(i)
                mass2=float(mass2)
                # print(type(mass2))
                '\n'
                print('The partial molar mass of',elem_2,'is: ', num_elem2*mass2)   
    for i in amudictionary.keys():
            if i == elem_3:
                print(elem_3 +" weighs "+ amudictionary.get(i)+" amu.")
                mass3=amudictionary.get(i)
                mass3=float(mass3)
                # print(type(mass3))
                '\n'
                print('The partial molar mass of',elem_3,'is: ', num_elem3*mass3)                           
    for i in amudictionary.keys():
            if i == elem_4:
                print(elem_4 +" weighs "+ amudictionary.get(i)+" amu.")
                mass4=amudictionary.get(i)
                mass4=float(mass4)
                # print(type(mass4))
                '\n'
                print('The partial molar mass of',elem_4,'is: ', num_elem4*mass4)
                '\n'
    for i in amudictionary.keys():
            if i == elem_5:
                print(elem_5 +" weighs "+ amudictionary.get(i)+" amu.")
                mass5=amudictionary.get(i)
                mass5=float(mass5)
                # print(type(mass5))
                '\n'
                print('The partial molar mass of',elem_5,'is: ', num_elem5*mass5)
                '\n'
    for i in amudictionary.keys():
            if i == elem_6:
                print(elem_6 +" weighs "+ amudictionary.get(i)+" amu.")
                mass6=amudictionary.get(i)
                mass6=float(mass6)
                # print(type(mass6))
                '\n'
                print('The partial molar mass of',elem_6,'is: ', num_elem6*mass6)
                '\n'
                print('\t',' The total MM is: ',num_elem1*mass+num_elem2*mass2+num_elem3*mass3+num_elem4*mass4+num_elem5*mass5+num_elem6*mass6)
                time.sleep(5)
elif num_diff_atoms>6:
    print('\t',' The number is out of range !')
    time.sleep(5)
     
else:
    clear()
    quit

    #from Tone import Tone
    #Tone.create_tone_from_list([540,607],duration=0.15)    
    #print('\n'," Invalid choice !")
    #print()
    #Tone.create_tone_from_list([880,1200],duration=0.20)
    #Tone.create_tone_from_list([540,607],duration=0.25)
    #Tone.create_tone_from_list([880,1200],duration=0.30)
    #Tone.create_tone_from_list([540,607],duration=0.35)
    #Tone.create_tone_from_list([880,1200],duration=0.40)
    #Tone.create_tone_from_list([540,607],duration=0.45)
   




