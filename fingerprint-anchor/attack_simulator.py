import torch
from tqdm import tqdm


def simulate_clone_attack(original_logits: torch.Tensor, num_attacks: int = 100_000,
                          noise_scale: float = 0.05) -> list:
    """
    Simulates 10^5 pattern-mapping + fine-tuning clone attempts.
    Returns list of cloned distributions.
    """
    clones = []
    for _ in tqdm(range(num_attacks), desc="Simulating clone attacks"):
        # Clone attack: add Gaussian noise (simulates fine-tuning/rebranding)
        noise = torch.randn_like(original_logits) * noise_scale
        clone_logits = original_logits + noise
        clones.append(torch.softmax(clone_logits, dim=-1))
    return clones
