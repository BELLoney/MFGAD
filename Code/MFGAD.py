## Multi-Fuzzy Granules Anomaly Detection (MFGAD) algorithm
## Please refer to the following papers:
## Yuan Zhong et al. Multi-Fuzzy Granules Anomaly Detection,2023.
## Uploaded by Yuan Zhong on July 24, 2023. E-mail:yuanzhong2799@foxmail.com.

import numpy as np
from scipy.io import loadmat
from scipy.spatial.distance import cdist
from sklearn.preprocessing import MinMaxScaler

def MFGAD(data, delta):
    ##input:
    # Data is data matrix without decisions, where rows for samples and columns for attributes.
    # Numeric attribute data is normalized to [0, 1].
    # delta is used to adjust the adaptive fuzzy radius.
    ## output
    # multi-fuzzy granules anomaly factor.

    n, m = data.shape
    varepsilon = np.zeros(m)
    for j in range(m):
        if np.min(data[:, j]) == 0 and np.max(data[:, j]) == 1:
            varepsilon[j] = np.std(data[:, j]) / delta

    E = np.zeros(m)
    for j in range(m):
        r1 = mfgad_rm(data[:, j], varepsilon[j])
        E[j] = -(1 / n) * np.sum(np.log2(np.sum(r1, axis=1) / n))

    b_de = np.argsort(E)[::-1]
    b_as = np.argsort(E)

    weight = np.zeros((n, m))
    FG_de = np.zeros((n, m))
    FG_as = np.zeros((n, m))

    for k in range(m):
        FSet = mfgad_rm(data[:, k], varepsilon[k])
        FSet_de = mfgad_rm(data[:, b_de[:m - k]], varepsilon[b_de[:m - k]])
        FSet_as = mfgad_rm(data[:, b_as[:m - k]], varepsilon[b_as[:m - k]])
        for i in range(n):
            # weight[i, k] = np.sqrt(np.sum(FSet[i, :]) / n)
            weight[i, k] = np.sum(FSet[i, :]) / n
            FG_de[i, k] = np.sum(FSet_de[i, :])
            FG_as[i, k] = np.sum(FSet_as[i, :])

    FGS_de = np.zeros((n, m - 1))
    FGS_as = np.zeros((n, m - 1))
    for k in range(1, m):
        FGS_de_temp = (FG_de[:, k] - FG_de[:, k - 1]) / FG_de[:, k]
        FGS_as_temp = (FG_as[:, k] - FG_as[:, k - 1]) / FG_as[:, k]
        FGS_de[: len(FGS_de_temp), k - 1] = FGS_de_temp
        FGS_as[: len(FGS_as_temp), k - 1] = FGS_as_temp

    MFGAF = np.zeros(n)
    for j in range(n):
        MFGAF[j] = 1 - (np.sum(weight[j, :]) / m) * np.sqrt((np.sum(FGS_de[j, :]) + np.sum(FGS_as[j, :])) / (2 * m - 2))
    return MFGAF

def mfgad_rm(subdata,e):
    if subdata.ndim==1:
        e = np.array([e])
        subdata = subdata.reshape(-1, 1)
    if all(e==0):
        rm = cdist(subdata, subdata,metric='cityblock') == 0
    else:
        temp1 = cdist(subdata[:,[0]], subdata[:,[0]], metric='cityblock')
        temp1[temp1 > e[0]] = 1
        rm = 1 - temp1
        for j in range(1,len(e)):
            temp = cdist(subdata[:,[j]], subdata[:,[j]], metric='cityblock')
            temp[temp > e[j]] = 1
            rm = np.minimum(rm, 1 - temp)
    return rm

if __name__ == "__main__":
    load_data = loadmat('Example.mat')
    trandata = load_data['Example']
    scaler = MinMaxScaler()
    trandata[:, 1:3] = scaler.fit_transform(trandata[:, 1:3])

    sigma = 1
    out_factors = MFGAD(trandata, sigma)
    print(out_factors)