from pymatgen.core import Structure
from pathlib import Path
from pymatgen.symmetry.bandstructure import HighSymmKpath
import subprocess

cif_f = Path("/home/gauravzanjal/Desktop/cif")
cal_f = Path("calculations")
An_to_BH = 1.8897259886

def w_elk(st,output_f):
    with open(output_f,"w") as f:
        f.write("tasks\n")
        f.write("0\n")
        f.write("20\n\n")
        
        f.write("avec\n")
        for v in st.lattice.matrix:
            f.write(f"{v[0]*An_to_BH:15.8f}" 
                    f"{v[1]*An_to_BH:15.8f}" 
                    f"{v[2]*An_to_BH:15.8f}\n")
         
        f.write("\nsppath\n")
        f.write("'/home/gauravzanjal/gaurav/elk/elk-10.8.12/species/'\n\n")

        species = {}
        for i in st:
            element = i.specie.symbol
            if element not in species:
                species[element] = []
            species[element].append(i.frac_coords)
        
        f.write("atoms\n")
        f.write(f"{len(species)}\n")

        
        for element, coords in species.items():
            f.write(f"'{element}.in'\n")
            f.write(f"{len(coords)}\n")
            for c in coords:
                f.write(
                    f"{c[0]:12.8f}"
                    f"{c[1]:12.8f}"
                    f"{c[2]:12.8f}\n"
                )
                
        f.write("plot1d\n")
        kpath = HighSymmKpath(st)
        path = kpath.kpath["path"][0]
        points = kpath.kpath["kpoints"]
        f.write(f"{len(path)}\n")
        f.write("200\n")
        
        for l in path:
            p = points[l]
            f.write(
                f"{p[0]:10.6f}"
                f"{p[1]:10.6f}"
                f"{p[2]:10.6f}"
                f"  !{l}\n")

        f.write("\n\nngridk")
        f.write("\n10  10  10")
        
for cif_f in cif_f.glob("*.cif"):
    st = Structure.from_file(cif_f)
    material = cif_f.stem
    
    material_d = cal_f / material
    material_d.mkdir(parents=True,exist_ok=True)  
    
    output_f = material_d /"elk.in"
    w_elk(st, output_f)
print("Finished")

def SCf(cal_f):
    for f in cal_f.iterdir():
        if f.is_dir():
            if (f/ "BAND.OUT").exists():
                print(f"{f.name} completed")
                continue
            print(f"Running {f.name}")
            
            try:
                subprocess.run(
                    ["/home/gauravzanjal/gaurav/elk/elk-10.8.12/src/elk"],
                    cwd=f,
                    check=True
                    )
                print(f"{f.name}: Success")
            
            except subprocess.CalledProcessError:
                print(f"{f.name}: Failed")
        
        
SCf(cal_f)
