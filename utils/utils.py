import random
import numpy as np
import torch
import torch.nn as nn
from torch.nn import functional as F

def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def pickle(file_path, data=None):
    import bz2
    import pickle
    
    if data is not None:
        with bz2.BZ2File(file_path, 'wb') as f:
            pickle.dump(data, f)
            data = True
    else:
        with bz2.BZ2File(file_path, 'rb') as f:
            data = pickle.load(f)

    return data

def bleu_score(references, candidates):
    from nltk.translate.bleu_score import corpus_bleu

    # reference and candidate is list of strings
    references = [[sen.split(' ')] for sen in references]
    candidates = [sen.split(' ') for sen in candidates]
    bleu1 = corpus_bleu(references, candidates, weights=(1.0, 0, 0, 0)) * 100
    bleu2 = corpus_bleu(references, candidates, weights=(0.5, 0.5, 0, 0)) * 100
    bleu3 = corpus_bleu(references, candidates, weights=(0.33, 0.33, 0.33, 0)) * 100
    bleu4 = corpus_bleu(references, candidates, weights=(0.25, 0.25, 0.25, 0.25)) * 100

    score = corpus_bleu(references, candidates) * 100
    return bleu1, bleu2, bleu3, bleu4, score, references, candidates

