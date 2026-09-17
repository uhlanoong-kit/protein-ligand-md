#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${script_dir}/common.sh"

project_root="$(cd "${script_dir}/.." && pwd)"
for structure in 4W52; do
  file="${project_root}/data/raw/${structure}.cif"
  require_file "${file}"
  atom_records=$(grep -c '^ATOM' "${file}" || true)
  het_records=$(grep -c '^HETATM' "${file}" || true)
  echo "${structure}: ATOM=${atom_records}, HETATM=${het_records}, bytes=$(wc -c < "${file}")"
done

echo "Automated presence check passed. Complete the manual audit in docs/validation_checklist.md."
