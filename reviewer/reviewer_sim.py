import random

class ReviewerSim:

    def score(self, paper_metrics):

        novelty = paper_metrics.get("novelty", 0.7)
        clarity = paper_metrics.get("clarity", 0.7)
        math_rigor = paper_metrics.get("rigor", 0.7)

        score = (novelty + clarity + math_rigor) / 3

        rejection_prob = max(0, 1 - score)

        return {
            "score": score,
            "rejection_probability": rejection_prob,
            "decision": "accept" if rejection_prob < 0.3 else "revise"
        }
