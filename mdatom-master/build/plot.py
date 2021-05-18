import matplotlib.pyplot as plt
import pandas as pd
import sys



def plot_radial(file):
    r_distr = pd.read_fwf(file, header=None, widths=[15]*2, names = ["r", "p"])
    plt.figure()
    plt.plot(r_distr['r'].to_list(), r_distr['p'].to_list())
    plt.savefig(file[:file.find(".")] + "_plot.png")


def plot_energy(file):
    energies = pd.read_fwf(file, header=None, widths=[15]*8, names = ["STEP", "TIME", "E-TOTAL", "E-KINETIC", "E-POTENTIAL", "VIRIAL", "PRESSURE", "SCALE-T"]) 
    plt.figure()

    t = energies['TIME'].to_list()
    

    plt.plot(t, energies['E-TOTAL'].to_list(), color='r', label="E-TOTAL")
    plt.plot(t, energies['E-KINETIC'].to_list(), color='g', label="E-KINETIC")
    plt.plot(t, energies['E-POTENTIAL'].to_list(), color='b', label="E-POTENTIAL")
    plt.plot(t, energies['VIRIAL'].to_list(), color='c', label="VIRIAL")
    plt.plot(t, energies['PRESSURE'].to_list(), color='m', label="PRESSURE")
    plt.plot(t, energies['SCALE-T'].to_list(), color='y', label="SCALE-T")

    plt.legend()

    plt.savefig(file[:file.find(".")] + "_plot.png")



def contains_args(list) -> bool:
    return any(element in list for element in sys.argv)



def main():
    '''Can be run with "python plot.py {filename} {optional args}"'''

    filename = sys.argv[1]

    arguments = sys.argv[1:]



    if len(arguments) == 1:
        #default options
        return

    

    if contains_args(["-r", "-radial"]):
        plot_radial(filename)

    if contains_args(["-e", "-energies"]):
        plot_energy(filename)


if __name__ == "__main__":
    main()



    
    

        
    
