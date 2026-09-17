#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${script_dir}/common.sh"
require_command gmx

tpr="${1:-production.tpr}"
trajectory="${2:-production_fit.xtc}"
output="${3:-results/raw/rmsf.xvg}"
require_file "${tpr}"
require_file "${trajectory}"
mkdir -p "$(dirname "${output}")"

printf 'C-alpha\n' | gmx rmsf -s "${tpr}" -f "${trajectory}" -o "${output}" -res

