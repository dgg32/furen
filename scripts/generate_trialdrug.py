#!/usr/bin/env python3
"""Generate a trial-drug linkage CSV.

Reads `data/drug.csv` and `data/trials.csv` and writes `data/trialdrug.csv`.
Output columns: PostingID,drug_cui

Usage: python scripts/generate_trialdrug.py
"""
import csv
import re
from pathlib import Path


DATA_DIR = Path(__file__).resolve().parents[1] / "data"
DRUGS_CSV = DATA_DIR / "drug.csv"
TRIALS_CSV = DATA_DIR / "trials.csv"
OUT_CSV = DATA_DIR / "trialdrug.csv"


def load_drug_cuis(path):
    cuis = set()
    with path.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        key = None
        # find the drug_cui column name (expect 'drug_cui')
        for k in reader.fieldnames:
            if k and k.lower() == "drug_cui":
                key = k
                break
        if key is None:
            raise ValueError("drug_cui column not found in drug.csv")
        for row in reader:
            val = row.get(key, "")
            val = val.strip()
            if not val:
                continue
            cuis.add(val)
    return cuis


def extract_cuis_from_field(s):
    if not s:
        return []
    # find patterns like C123456 or C12345
    return re.findall(r"C\d+", s)


def generate_linkage(drug_cuis_set, trials_path, out_path):
    pairs = set()
    with trials_path.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        # choose PostingID (as seen in the file); fall back to first column
        id_col = None
        for k in reader.fieldnames:
            if k and k.lower() == "postingid":
                id_col = k
                break
        if id_col is None:
            id_col = reader.fieldnames[0]

        # find drug_cui column
        drug_col = None
        for k in reader.fieldnames:
            if k and k.lower() == "drug_cui":
                drug_col = k
                break
        if drug_col is None:
            raise ValueError("drug_cui column not found in trials.csv")

        for row in reader:
            trial_id = row.get(id_col, "").strip()
            raw = row.get(drug_col, "")
            cuis = extract_cuis_from_field(raw)
            for cui in cuis:
                if cui in drug_cuis_set:
                    pairs.add((trial_id, cui))

    # write out
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["PostingID", "drug_cui"])
        for trial_id, cui in sorted(pairs):
            writer.writerow([trial_id, cui])


def main():
    drug_cuis = load_drug_cuis(DRUGS_CSV)
    generate_linkage(drug_cuis, TRIALS_CSV, OUT_CSV)
    print(f"Wrote {OUT_CSV} with links for {len(drug_cuis)} known drug_cuis.")


if __name__ == "__main__":
    main()
