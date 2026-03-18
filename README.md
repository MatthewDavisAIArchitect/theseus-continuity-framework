# theseus-continuity-framework

**v4.0 — arXiv-ready release**

**Paper:** Intent-Aware Continuity in Evolving AI Systems: Typed Adjudication for Provenance-Aware Continuity Judgments

**Author:** Matthew A. Davis (March 2026)

Reproducibility package containing:
- Complete LaTeX source (`main.tex`)
- Observable Configuration State Space simulations
- HonestAGI-style intrinsic fingerprinting test harness (KL < 0.01 under 10⁵ attacks)
- All manuscript figures (TikZ + PDF)
- One-click verification scripts

## Quick Start (60 seconds)

```bash
git clone https://github.com/MatthewDavisAIArchitect/theseus-continuity-framework.git
cd theseus-continuity-framework
cd fingerprint-anchor
pip install -r requirements.txt
bash run_harness.sh          # fingerprint anchor verification
python ../run_all.py         # full Stage-I + figures
```

**Zenodo DOI:** https://doi.org/10.5281/zenodo.19080605

**What's new in v4.0 (arXiv-ready release)**

- New canonical title and abstract (claims now exactly match evidence)
- Typed continuity judgment \(J_{k,c}\) with operational decision procedure + continuity card JSON schema
- Minimal Stage-II case suite table (authorized fine-tune, unauthorized clone, merge, reassembly, etc.)
- Neutral positioning table vs. registries, provenance standards, watermarking, and fingerprinting
- Theorem 1 proof + consequences for measurement layer
- Threats-to-validity and strengthened Limitations sections
- Full alignment with NIST AI RMF / EU AI Act
- Complete reproducibility package (code, test harness, figures)

Full paper source (`main.tex`), figures, and fingerprinting harness are available in the linked GitHub repository **(v4.0 tag)**. This is version 4.0 of the preprint series.

## Repository Structure

* `main.tex` — arXiv-ready paper source
* `fingerprint-anchor/` — anchor injection + 10⁵-attack harness
* `simulation/` — Stage-I drift & repair experiments
* `figures/` — all 6 manuscript figures
* `results/` — generated outputs
* `notebooks/` — exploratory demos
* `run_all.py` — one-command reproduction

## Citation

```bibtex
@misc{davis2026intent,
  author = {Davis, Matthew A.},
  title = {Intent-Aware Continuity in Evolving AI Systems: Typed Adjudication for Provenance-Aware Continuity Judgments},
  year = {2026},
  month = {March},
  version = {4.0},
  note = {arXiv forthcoming},
  doi = {10.5281/zenodo.19080605},
  url = {https://doi.org/10.5281/zenodo.19080605},
  howpublished = {GitHub: https://github.com/MatthewDavisAIArchitect/theseus-continuity-framework/tree/v4.0}
}
```

## License

MIT (see LICENSE)
