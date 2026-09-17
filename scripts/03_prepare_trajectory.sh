#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${script_dir}/common.sh"

require_command gmx

tpr="${1:-production.tpr}"
trajectory="${2:-production.xtc}"
output="${3:-production_fit.xtc}"

require_file "${tpr}"
require_file "${trajectory}"

tmp_whole="${output%.xtc}_whole.xtc"
tmp_centered="${output%.xtc}_centered.xtc"
printf 'System\n' | gmx trjconv -s "${tpr}" -f "${trajectory}" -o "${tmp_whole}" -pbc whole
printf 'Protein\nSystem\n' | gmx trjconv -s "${tpr}" -f "${tmp_whole}" -o "${tmp_centered}" -center -pbc mol -ur compact
printf 'Backbone\nSystem\n' | gmx trjconv -s "${tpr}" -f "${tmp_centered}" -o "${output}" -fit rot+trans
rm -f "${tmp_whole}" "${tmp_centered}"

echo "Prepared trajectory: ${output}"

