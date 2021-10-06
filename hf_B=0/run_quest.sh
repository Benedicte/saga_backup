#!/bin/bash
#SBATCH --job-name=tdcc2_0.5_q.py  
#SBATCH --account=nn4654k
#SBATCH --time=00:10:00
#SBATCH --mem-per-cpu=4G
set -o errexit  # Exit the script on any error
set -o nounset  # Treat any unset variables as an error

set +u
. /cluster/software/Anaconda3/2020.11/etc/profile.d/conda.sh
conda activate quest
set -u

module --quiet purge

python /cluster/home/benedico/Programs/QUEST/src/quest.py -me hf_x.inp -mo hf.mol -ba cc-pvdz.bas -o hf_magnetic_x.out
python /cluster/home/benedico/Programs/QUEST/src/quest.py -me hf_y.inp -mo hf.mol -ba cc-pvdz.bas -o hf_magnetic_y.out
python /cluster/home/benedico/Programs/QUEST/src/quest.py -me hf_z.inp -mo hf.mol -ba cc-pvdz.bas -o hf_magnetic_z.out

python use_lonread.py hf_magnetic_x hf x
python use_lonread.py hf_magnetic_y hf y
python use_lonread.py hf_magnetic_z hf z
