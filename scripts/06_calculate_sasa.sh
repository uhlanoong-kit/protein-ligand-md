#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${script_dir}/common.sh"
require_command gmx

tpr="${1:-production.tpr}"
trajectory="${2:-production_fit.xtc}"
total_output="${3:-results/raw/protein_sasa.xvg}"
residue_output="${4:-results/raw/residue_sasa.xvg}"
require_file "${tpr}"
require_file "${trajectory}"
mkdir -p "$(dirname "${total_output}")"

gmx sasa -s "${tpr}" -f "${trajectory}" \
  -surface 'group "Protein"' -output 'group "Protein"' \
  -o "${total_output}" -or "${residue_output}" -tu ns

