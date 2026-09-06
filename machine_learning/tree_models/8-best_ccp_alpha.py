#!/usr/bin/env python3
"""Select the best ccp_alpha from a set of pruned trees."""


def get_best_alpha(clfs, train_scores, test_scores, ccp_alphas):
    """Pick the best (alpha, classifier) by test accuracy, then
    generalization gap, then simplicity.

    Returns:
        best_alpha: The chosen ccp_alpha value.
        best_clf: Its corresponding trained classifier.
    """
    max_test = max(test_scores)
    candidates = [i for i, s in enumerate(test_scores) if s == max_test]

    min_gap = min(train_scores[i] - test_scores[i] for i in candidates)
    candidates = [i for i in candidates
                  if train_scores[i] - test_scores[i] == min_gap]

    best_i = max(candidates, key=lambda i: ccp_alphas[i])
    return ccp_alphas[best_i], clfs[best_i]
