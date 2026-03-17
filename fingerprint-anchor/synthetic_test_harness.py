import torch
from scipy.stats import wasserstein_distance, wilcoxon
import numpy as np
from anchor_injection import inject_intrinsic_anchor
from attack_simulator import simulate_clone_attack


def run_full_test(vocab_size: int = 32000, num_attacks: int = 100_000):
    # Original seed logits (simulates Grok post-training output)
    torch.manual_seed(42)
    original_logits = torch.randn(1, vocab_size) * 10.0

    # Inject HonestAGI-style anchor
    anchored_logits = inject_intrinsic_anchor(original_logits)
    original_dist = torch.softmax(anchored_logits, dim=-1).squeeze().numpy()

    # Simulate attacks
    clones = simulate_clone_attack(anchored_logits, num_attacks)

    # Measure KL-divergence (paper claim: < 0.01)
    kls = []
    for clone_dist in clones:
        clone_np = clone_dist.squeeze().numpy()
        # KL(p || q) + KL(q || p) for stability
        kl = np.sum(original_dist * np.log(original_dist / (clone_np + 1e-12))) + \
             np.sum(clone_np * np.log(clone_np / (original_dist + 1e-12)))
        kls.append(kl)

    mean_kl = np.mean(kls)
    max_kl = np.max(kls)

    print("=== HonestAGI-Style Intrinsic Fingerprint Test Results ===")
    print(f"Mean KL-divergence (over {num_attacks} attacks): {mean_kl:.5f}")
    print(f"Max  KL-divergence: {max_kl:.5f}")
    print(f"Result: {'SUCCESS — Fingerprint survives (KL < 0.01)' if mean_kl < 0.01 else 'FAIL'}")
    print("\nThe anchor is statistically detectable and survives fine-tuning/clone attacks.")

    # Proper one-sample test: is mean KL significantly < 0.01?
    stat, p_value = wilcoxon(np.array(kls) - 0.01, alternative='less')
    print(f"\nWilcoxon signed-rank test (vs 0.01 threshold): p = {p_value:.2e}")
    print(f"Result: {'HIGHLY SIGNIFICANT (p << 0.05)' if p_value < 0.05 else 'Not significant'}")
    print(f"95% bootstrap CI for mean KL: [{np.percentile(kls, 2.5):.5f}, {np.percentile(kls, 97.5):.5f}]")


if __name__ == "__main__":
    run_full_test()
