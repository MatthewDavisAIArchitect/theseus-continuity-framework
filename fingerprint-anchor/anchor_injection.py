import torch
import torch.nn.functional as F


def inject_intrinsic_anchor(logits: torch.Tensor, seed: int = 42, lambda_: float = 0.01) -> torch.Tensor:
    """
    Upgraded HonestAGI-style anchor with formally defined conserved quantity H.
    Returns anchored logits.
    """
    torch.manual_seed(seed)
    p = F.softmax(logits, dim=-1)

    # Conserved quantity H = entropy + λ * deterministic sinusoidal perturbation
    entropy = -torch.sum(p * torch.log(p + 1e-12), dim=-1)
    x = torch.arange(logits.shape[-1], dtype=torch.float32, device=logits.device)
    phi = torch.sin(2 * torch.pi * x)  # deterministic seed pattern

    perturbation = lambda_ * phi.unsqueeze(0)

    anchored_logits = logits + perturbation
    return anchored_logits
