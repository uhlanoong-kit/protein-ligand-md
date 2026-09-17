#!/usr/bin/env bash
set -euo pipefail

project_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
raw_dir="${project_root}/data/raw"
mkdir -p "${raw_dir}"

download_cif() {
  local pdb_id="$1"
  local output="${raw_dir}/${pdb_id}.cif"
  local url="https://files.rcsb.org/download/${pdb_id}.cif"

  if [[ -s "${output}" ]]; then
    echo "Already present: ${output}"
    return
  fi

  echo "Downloading ${pdb_id} from RCSB PDB"
  curl --fail --location --retry 3 --output "${output}" "${url}"
}

download_cif "4W52"

echo "Downloaded coordinate files to ${raw_dir}"
