## DDISuccess/Data
resultant representation of drug properties: drug_#{drug_property}_matrix_dict.pickle

Here is an expamle to load data:
```python    
with open("DDISuccess/Data/drug_SIDER_matrix_dict.pickle", 'rb') as rf:
     drug_SIDER_dict = pickle.load(rf) # key is drug name, value is the representation of side effect
drug_names = list(drug_SIDER_dict.keys())
print(drug_SIDER_dict[drug_names[0]) # get value
```

## ./DDISuccess/BaseHierarchyContext/all_feature_classifier.py
Our model for DDI classifier

## vae/M2
Vae model for DDI classifier.
First run ddi_train_vae.py, then run ddi_train_classifier.py

## antibioitc_1326_sim.csv
commonly used antibiotic semantic similarity labeled dataset

We select 52 most commonly used antibiotics of 10 categories in hospital with the combination of which we get 1326 antibiotic pairs. From the perspective of clinical application, doctors score the similarity between two antibiotics, which ranges in [0, 1] (unsimilar, 0; extremely similar, 1), according to both antibacteria spectrum and efficacies of medicine. To make antibiotic pairs labeling more accurate, each pair is labeled by at least 3 doctors and finally the average is taken.

Each row represents an antibiotic pair and the simiality score annotated by doctors in the dataset(antibioitc_1326_sim.csv).

**[Ref]**
1. [Semi-Supervised Learning with Deep Generative Models](http://arxiv.org/abs/1406.5298)
2. [Code for reproducing results of NIPS 2014 paper "Semi-Supervised Learning with Deep Generative Models"](https://github.com/dpkingma/nips14-ssl)
