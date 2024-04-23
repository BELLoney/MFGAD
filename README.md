# MFGAD
**Zhong Yuan**, Hongmei Chen, Chuan Luo, Dezhong Peng*, [MFGAD: Multi-Fuzzy Granules Anomaly Detection](Paper/2023-MFGAD.pdf), Information Fusion, vol. 95, no. 3, pp. 17-25, 
8 February 2023, DOI: [10.1016/j.inffus.2023.02.007](https://doi.org/10.1016/j.inffus.2023.02.007). (Code)

## Abstract
Unsupervised anomaly detection is an important research direction in the process of unsupervised knowledge acquisition. It has been successfully applied in many fields, such as online fraud identification, loan approval, and medical diagnosis. Multi-granularity thinking is an effective information fusion method for solving problems in a multi-granular environment, which allows people to understand and analyze problems from multiple perspectives. However, there are few studies on building anomaly detection models using the idea of multi-fuzzy granules. To this end, this paper constructs a multi-fuzzy granules anomaly detection method by using a fuzzy rough computing model. In this method, a hybrid metric is first used to calculate the fuzzy relations. Then, two ranking sequences are constructed based on the significance of attributes. Furthermore, forward and reverse multi-fuzzy granules are constructed to define anomaly scores based on the ranking sequences. Finally, a multi-fuzzy granules-based anomaly detection algorithm is designed to detect anomalies. The experimental results compared with existing algorithms show the effectiveness of the proposed algorithm.

## Usage
You can run Demo_MFGAD.m or MFGAD.py:
```
clear all
clc
format short

load Example.mat
Dataori=Example;
trandata=Dataori;

trandata(:,2:3)=normalize(trandata(:,2:3),'range');
sigma=1;

out_scores=MFGAD(trandata,sigma)

```
You can get outputs as follows:
```
out_scores =

    0.8289
    0.7698
    0.8564
    0.7486
    0.8045
    0.8880
```

## Citation
If you find MFGAD useful in your research, please consider citing:
```
@article{yuan2023MFGAD,
title = {MFGAD: Multi-fuzzy granules anomaly detection},
author = {Yuan, Zhong  and Chen, Hong Mei and Luo, Chuan  and Peng, De Zhong},
journal = {Information Fusion},
volume = {95},
pages = {17-25},
year = {2023},
doi={10.1016/j.inffus.2023.02.007},
publisher={Elsevier}
}
```

## Contact
If you have any questions, please contact yuanzhong@scu.edu.cn.
