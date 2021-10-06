#!/bin/bash
#SBATCH --job-name=tdcc2_0.5_q.py  
#SBATCH --account=nn4654k
#SBATCH --time=00:10:00
#SBATCH --mem-per-cpu=4G
set -o errexit  # Exit the script on any error
set -o nounset  # Treat any unset variables as an error
module --quiet purge
#module restore quest2

set +u
. /cluster/software/Anaconda3/2020.11/etc/profile.d/conda.sh
conda activate quest
set -u

python /cluster/home/benedico/Programs/QUEST/src/quest.py -me hf_x.inp -mo h2.mol -ba cc-pvdz.bas -o h2_magnetic_x.out
python /cluster/home/benedico/Programs/QUEST/src/quest.py -me hf_y.inp -mo h2.mol -ba cc-pvdz.bas -o h2_magnetic_y.out
python /cluster/home/benedico/Programs/QUEST/src/quest.py -me hf_z.inp -mo h2.mol -ba cc-pvdz.bas -o h2_magnetic_z.out

python use_lonread.py h2_magnetic_x h2 x
python use_lonread.py h2_magnetic_y h2 y
python use_lonread.py h2_magnetic_z h2 z
