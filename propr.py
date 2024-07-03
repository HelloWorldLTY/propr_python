import numpy as np
from scipy.stats import gmean

#eps is used for numerical stability.
def clr(a1):
    gm =  gmean(a1)
    eps = 1e-8
    return np.log(a1 / gm + eps)

def alr(a1):
    x_d = a1[-1]
    eps = 1e-8
    return np.log(a1[0:len(a1)-1] / x_d + eps)

def phi(ai,aj):
    return np.var(ai-aj) / np.var(ai)

def propr_corr(ai,aj):
    return 1 - np.var(ai-aj) / (np.var(ai) + np.var(aj))

def phi_s(ai,aj):
    return np.var(ai-aj) / np.var(ai+aj)


def test_propr():
    a1 = np.array([1,2,3,4,5])
    a2 = np.array([1,2,3,4,1])

    p1 = propr_corr(clr(a1), clr(a2))
    p2 = phi(clr(a1), clr(a2))
    p3 = phi_s(clr(a1), clr(a2))

    p4 = propr_corr(alr(a1), alr(a2))
    p5 = phi(alr(a1), alr(a2))
    p6 = phi_s(alr(a1), alr(a2))

    print(p1,p2,p3,p4,p5,p6)


