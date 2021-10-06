#!/bin/bash

set -o errexit  # Exit the script on any error
set -o nounset  # Treat any unset variables as an error

module --quiet purge  # Reset the modules to the system default
module restore cc

# Arguments, F, Magnetic direction, electric field direction

#Magentic x dir

sbatch --account=nn4654k --mem=1G --time=1:00:00 run_verdet.sh 0.001 0 1
sbatch --account=nn4654k --mem=1G --time=1:00:00 run_verdet.sh 0.001 0 2
sbatch --account=nn4654k --mem=1G --time=1:00:00 run_verdet.sh 0.002 0 1
sbatch --account=nn4654k --mem=1G --time=1:00:00 run_verdet.sh 0.002 0 2
sbatch --account=nn4654k --mem=1G --time=1:00:00 run_verdet.sh -0.001 0 1
sbatch --account=nn4654k --mem=1G --time=1:00:00 run_verdet.sh -0.001 0 2
sbatch --account=nn4654k --mem=1G --time=1:00:00 run_verdet.sh -0.002 0 1
sbatch --account=nn4654k --mem=1G --time=1:00:00 run_verdet.sh -0.002 0 2

#Magnetic y dir 

sbatch --account=nn4654k --mem=1G --time=1:00:00 run_verdet.sh 0.001 1 0
sbatch --account=nn4654k --mem=1G --time=1:00:00 run_verdet.sh 0.001 1 2
sbatch --account=nn4654k --mem=1G --time=1:00:00 run_verdet.sh 0.002 1 0
sbatch --account=nn4654k --mem=1G --time=1:00:00 run_verdet.sh 0.002 1 2
sbatch --account=nn4654k --mem=1G --time=1:00:00 run_verdet.sh -0.001 1 0
sbatch --account=nn4654k --mem=1G --time=1:00:00 run_verdet.sh -0.001 1 2
sbatch --account=nn4654k --mem=1G --time=1:00:00 run_verdet.sh -0.002 1 0
sbatch --account=nn4654k --mem=1G --time=1:00:00 run_verdet.sh -0.002 1 2

#Magnetic z dir

sbatch --account=nn4654k --mem=1G --time=1:00:00 run_verdet.sh 0.001 2 0
sbatch --account=nn4654k --mem=1G --time=1:00:00 run_verdet.sh 0.001 2 1
sbatch --account=nn4654k --mem=1G --time=1:00:00 run_verdet.sh 0.002 2 0
sbatch --account=nn4654k --mem=1G --time=1:00:00 run_verdet.sh 0.002 2 1
sbatch --account=nn4654k --mem=1G --time=1:00:00 run_verdet.sh -0.001 2 0
sbatch --account=nn4654k --mem=1G --time=1:00:00 run_verdet.sh -0.001 2 1
sbatch --account=nn4654k --mem=1G --time=1:00:00 run_verdet.sh -0.002 2 0
sbatch --account=nn4654k --mem=1G --time=1:00:00 run_verdet.sh -0.002 2 1
