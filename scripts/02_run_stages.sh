#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${script_dir}/common.sh"

require_command gmx

if [[ $# -ne 1 ]]; then
  echo "Usage: $0 PREPARED_SYSTEM_DIRECTORY" >&2
  exit 2
fi

run_dir="$(cd "$1" && pwd)"
project_root="$(cd "${script_dir}/.." && pwd)"
mdp_dir="${project_root}/configs/gromacs"

require_file "${run_dir}/conf.gro"
require_file "${run_dir}/topol.top"
require_file "${run_dir}/index.ndx"

cd "${run_dir}"

gmx grompp -f "${mdp_dir}/minimization.mdp" -c conf.gro -p topol.top -n index.ndx -o em.tpr
gmx mdrun -deffnm em -v

gmx grompp -f "${mdp_dir}/nvt.mdp" -c em.gro -r em.gro -p topol.top -n index.ndx -o nvt.tpr
gmx mdrun -deffnm nvt -v

gmx grompp -f "${mdp_dir}/npt.mdp" -c nvt.gro -r nvt.gro -t nvt.cpt -p topol.top -n index.ndx -o npt.tpr
gmx mdrun -deffnm npt -v

echo "Equilibration completed. Validate all checkpoints before preparing production."

