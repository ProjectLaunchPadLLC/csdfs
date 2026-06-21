import torch

def langevin_step(x, grad_E, eta=0.01, temperature=0.1):
    noise = torch.randn_like(x) * (2 * eta * temperature) ** 0.5
    return x - eta * grad_E + noise
