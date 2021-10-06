#!/bin/bash

set -o errexit  # Exit the script on any error
set -o nounset  # Treat any unset variables as an error

module --quiet purge  # Reset the modules to the system default
module restore cc

# Arguments: F, Magnetic direction, electric field direction

#Magentic x dir

sbatch --account=nn4654k --mem=1G --time=0:05:00 run_verdet.sh 0.001 x 1
#sbatch --account=nn4654k --mem=1G --time=3:30:00 run_verdet.sh 0.001 x 2
#sbatch --account=nn4654k --mem=1G --time=3:30:00 run_verdet.sh 0.002 x 1
#sbatch --account=nn4654k --mem=1G --time=3:30:00 run_verdet.sh 0.002 x 2
#sbatch --account=nn4654k --mem=1G --time=3:30:00 run_verdet.sh -0.001 x 1
#sbatch --account=nn4654k --mem=1G --time=3:30:00 run_verdet.sh -0.001 x 2
#sbatch --account=nn4654k --mem=1G --time=3:30:00 run_verdet.sh -0.002 x 1
#sbatch --account=nn4654k --mem=1G --time=3:30:00 run_verdet.sh -0.002 x 2

#Magnetic y dir 

#sbatch --account=nn4654k --mem=1G --time=3:30:00 run_verdet.sh 0.001 y 0
#sbatch --account=nn4654k --mem=1G --time=3:30:00 run_verdet.sh 0.001 y 2
#sbatch --account=nn4654k --mem=1G --time=3:30:00 run_verdet.sh 0.002 y 0
#sbatch --account=nn4654k --mem=1G --time=3:30:00 run_verdet.sh 0.002 y 2
#sbatch --account=nn4654k --mem=1G --time=3:30:00 run_verdet.sh -0.001 y 0
#sbatch --account=nn4654k --mem=1G --time=3:30:00 run_verdet.sh -0.001 y 2
#sbatch --account=nn4654k --mem=1G --time=3:30:00 run_verdet.sh -0.002 y 0
#sbatch --account=nn4654k --mem=1G --time=3:30:00 run_verdet.sh -0.002 y 2

#Magnetic z dir

#sbatch --account=nn4654k --mem=1G --time=3:30:00 run_verdet.sh 0.001 z 0
#sbatch --account=nn4654k --mem=1G --time=3:30:00 run_verdet.sh 0.001 z 1
#sbatch --account=nn4654k --mem=1G --time=3:30:00 run_verdet.sh 0.002 z 0
#sbatch --account=nn4654k --mem=1G --time=3:30:00 run_verdet.sh 0.002 z 1
#sbatch --account=nn4654k --mem=1G --time=3:30:00 run_verdet.sh -0.001 z 0
#sbatch --account=nn4654k --mem=1G --time=3:30:00 run_verdet.sh -0.001 z 1
#sbatch --account=nn4654k --mem=1G --time=3:30:00 run_verdet.sh -0.002 z 0
#sbatch --account=nn4654k --mem=1G --time=3:30:00 run_verdet.sh -0.002 z 1
