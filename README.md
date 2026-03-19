# theseus-continuity-framework

**v4.1 — arXiv-ready release**

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

**What's new in v4.1**

- Strengthened Ship of Theseus framing in the Introduction (now the central metaphor is fully developed)
- Restored all 6 measurement-layer figures in the Appendix (no more placeholder note)
- Minor cleanups for arXiv submission

This is version 4.1 of the preprint series. GitHub tag: v4.1

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
  version = {4.1},
  note = {arXiv forthcoming},
  doi = {10.5281/zenodo.19080605},
  url = {https://doi.org/10.5281/zenodo.19080605},
  howpublished = {GitHub: https://github.com/MatthewDavisAIArchitect/theseus-continuity-framework/tree/v4.1}
}
```

## License

MIT (see LICENSE)
