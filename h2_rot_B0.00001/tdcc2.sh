#!/bin/bash

set -o errexit  # Exit the script on any error
set -o nounset  # Treat any unset variables as an error

module --quiet purge
module restore quest2

python /cluster/home/benedico/Programs/QUEST/src/quest.py -me hf_x.inp -mo h2_${1}.mol -ba cc-pvdz.bas -o h2_magnetic_x_${1}.out
python /cluster/home/benedico/Programs/QUEST/src/quest.py -me hf_y.inp -mo h2_${1}.mol -ba cc-pvdz.bas -o h2_magnetic_y_${1}.out
python /cluster/home/benedico/Programs/QUEST/src/quest.py -me hf_z.inp -mo h2_${1}.mol -ba cc-pvdz.bas -o h2_magnetic_z_${1}.out

python use_lonread.py h2_magnetic_x_$1 h2 x
python use_lonread.py h2_magnetic_y_$1 h2 y
python use_lonread.py h2_magnetic_z_$1 h2 z


module --quiet purge  # Reset the modules to the system default
module restore cc

# Arguments, F, Magnetic direction, electric field direction

#Magentic x dir

sbatch --account=nn4654k --mem=1G --time=0:15:00 run_verdet.sh 0.001 x 1 $1
sbatch --account=nn4654k --mem=1G --time=0:15:00 run_verdet.sh 0.001 x 2 $1
sbatch --account=nn4654k --mem=1G --time=0:15:00 run_verdet.sh 0.002 x 1 $1
sbatch --account=nn4654k --mem=1G --time=0:15:00 run_verdet.sh 0.002 x 2 $1
sbatch --account=nn4654k --mem=1G --time=0:15:00 run_verdet.sh -0.001 x 1 $1
sbatch --account=nn4654k --mem=1G --time=0:15:00 run_verdet.sh -0.001 x 2 $1
sbatch --account=nn4654k --mem=1G --time=0:15:00 run_verdet.sh -0.002 x 1 $1 
sbatch --account=nn4654k --mem=1G --time=0:15:00 run_verdet.sh -0.002 x 2 $1

#Magnetic y dir 

sbatch --account=nn4654k --mem=1G --time=0:15:00 run_verdet.sh 0.001 y 0 $1
sbatch --account=nn4654k --mem=1G --time=0:15:00 run_verdet.sh 0.001 y 2 $1
sbatch --account=nn4654k --mem=1G --time=0:15:00 run_verdet.sh 0.002 y 0 $1
sbatch --account=nn4654k --mem=1G --time=0:15:00 run_verdet.sh 0.002 y 2 $1
sbatch --account=nn4654k --mem=1G --time=0:15:00 run_verdet.sh -0.001 y 0 $1
sbatch --account=nn4654k --mem=1G --time=0:15:00 run_verdet.sh -0.001 y 2 $1
sbatch --account=nn4654k --mem=1G --time=0:15:00 run_verdet.sh -0.002 y 0 $1
sbatch --account=nn4654k --mem=1G --time=0:15:00 run_verdet.sh -0.002 y 2 $1  

#Magnetic z dir

sbatch --account=nn4654k --mem=1G --time=0:15:00 run_verdet.sh 0.001 z 0 $1
sbatch --account=nn4654k --mem=1G --time=0:15:00 run_verdet.sh 0.001 z 1 $1
sbatch --account=nn4654k --mem=1G --time=0:15:00 run_verdet.sh 0.002 z 0 $1
sbatch --account=nn4654k --mem=1G --time=0:15:00 run_verdet.sh 0.002 z 1 $1 
sbatch --account=nn4654k --mem=1G --time=0:15:00 run_verdet.sh -0.001 z 0 $1
sbatch --account=nn4654k --mem=1G --time=0:15:00 run_verdet.sh -0.001 z 1 $1
sbatch --account=nn4654k --mem=1G --time=0:15:00 run_verdet.sh -0.002 z 0 $1 
sbatch --account=nn4654k --mem=1G --time=0:15:00 run_verdet.sh -0.002 z 1 $1 
