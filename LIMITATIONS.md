# Limitations (matches paper Section 10)

- Fingerprint evaluation uses synthetic logits and i.i.d. pattern-mapping attacks only.
- No full gradient-based fine-tuning on real 314B-scale models (public Grok-1) yet.
- Adversarial robustness (informed attacker subtracting φ(x)) is untested.
- Metric *d* and Q-tuple coordinate weights are application-dependent and require domain-specific tuning.
- Framework currently lacks production MLOps integration (MLflow, DVC, W&B).
- Hard-invariants decidability is assumed; scaling the C2PA/SLSA lineage graph to millions of checkpoints is an open engineering question.

These limitations are acknowledged to guide responsible future work and deployment.
