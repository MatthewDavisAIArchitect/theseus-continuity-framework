# theseus-continuity-framework

**v1.0 — arXiv-ready release**

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

## What's New in v1.0 (arXiv-ready)

* New canonical title and abstract (claims now exactly match evidence)
* Typed continuity judgment (J_{k,c}) with operational decision procedure + continuity card JSON schema
* Minimal Stage-II case suite table (authorized fine-tune, unauthorized clone, merge, reassembly, etc.)
* Neutral positioning table vs. registries, provenance standards, watermarking, and fingerprinting
* Theorem 1 proof + consequences for measurement layer
* Threats-to-validity and strengthened Limitations sections
* Full alignment with NIST AI RMF / EU AI Act
* Zenodo DOI will be minted from this tag

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
  title={Intent-Aware Continuity in Evolving AI Systems: Typed Adjudication for Provenance-Aware Continuity Judgments},
  author={Matthew A. Davis},
  year={2026},
  howpublished={\url{https://github.com/MatthewDavisAIArchitect/theseus-continuity-framework}},
  note={arXiv forthcoming}
}
```

Zenodo DOI: pending mint from v1.0 tag
arXiv: will be linked after upload

## License

MIT (see LICENSE)
