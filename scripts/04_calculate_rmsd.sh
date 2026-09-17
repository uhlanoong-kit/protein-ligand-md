#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${script_dir}/common.sh"
require_command gmx

tpr="${1:-production.tpr}"
trajectory="${2:-production_fit.xtc}"
output="${3:-results/raw/backbone_rmsd.xvg}"
require_file "${tpr}"
require_file "${trajectory}"
mkdir -p "$(dirname "${output}")"

printf 'Backbone\nBackbone\n' | gmx rms -s "${tpr}" -f "${trajectory}" -o "${output}" -tu ns

