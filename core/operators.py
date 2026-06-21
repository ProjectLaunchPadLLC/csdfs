import torch

def sync_operator(global_state, beta):
    return beta * global_state


def orthogonal_projection(x, global_state):
    g = global_state
    if torch.norm(g) < 1e-8:
        return x
    v = g / torch.norm(g)
    return x - torch.dot(x, v) * v


def individuality_operator(x, global_state, lam):
    return lam * orthogonal_projection(x, global_state)
