import os 

import subprocess

def clear_folder(path):
    if os.path.isdir(path):
            for element in os.listdir(path):

                element = os.path.join(path, element)

                if os.path.isfile(element):
                    os.remove(element)

                else: 
                    clear_folder(element)

            os.rmdir(path)
    
    else:
        raise OSError(path, " not a valid Directory")






if __name__ == "__main__":


    folder = "attempt01/"
    abbrev = "01"

    directory = folder + abbrev
 
    input_file = folder + "input.txt"
    coordinate_file = folder + "coord.txt"

    output_file = directory + "_output"

    energies_output = directory + "_energies"

    radial_distr_output = directory + "_radial_distr"


    print("Hello User, welcome to the MD-Atom Simulation. \nRemember to set the correct files in the main.py file.\nEnjoy!\n")

    if(os.path.isdir(directory)):
        clear_folder(directory)

    os.system(f"mkdir {folder}")
    os.system("cmake ..")
    os.system("make")

    
    os.system(f"./mdatom {input_file} {coordinate_file} > {output_file}")
    
    os.system(f"python energy.py {output_file} > {energies_output}")

    os.system(f"python gr.py {output_file} > {radial_distr_output}")

    os.system(f"python plot.py {radial_distr_output} -r")

    os.system(f"python plot.py {energies_output} -e")

    

    

    
    
    
