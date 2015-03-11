# -*- coding: utf-8 -*-
import random

def count_ngrams(tokens, n=3):
    "Returns dict of grams as keys and their counts as values"
    ngrams = {}

    if len(tokens) < n:
        return ngrams

    for i in range(len(tokens) - n + 1):
        gram = tuple(tokens[i:i+n])
        if gram not in ngrams:
            ngrams[gram] = 0
        ngrams[gram] += 1

    return ngrams

def merge_ngrams(ngrams_list):
    "Returns a merged counted ngrams from a list of ngrams counts."
    merged = {}

    for ngrams in ngrams_list:
        for key, val in ngrams.iteritems():
            if key not in merged:
                merged[key] = 0
            merged[key] += val

    return merged

def build_model(tokens, n=3):
    "Build a markov model (grams as keys and nextToken as values) from tokens."
    model = {}

    if len(tokens) < n:
        return model

    for i in range(len(tokens) - n):
        gram = tuple(tokens[i:i+n])
        next_token = tokens[i+n]

        if gram in model:
            model[gram].append(next_token)
        else:
            model[gram] = [next_token]

    final_gram = tuple(tokens[len(tokens) - n:])
    if final_gram in model:
        model[final_gram].append(None)
    else:
        model[final_gram] = [None]

    return model

def generate(model, n, seed=None, max_iter=100):
    "Generates text from markov model, starting at seed. Max_iter guarantees no infinite loops."

    if seed is None:
        seed = random.choice(model.keys())

    output = list(seed)

    current = tuple(seed)

    for i in range(max_iter):
        if current in model:
            possible_next_tokens = model[current]
            next_token = random.choice(possible_next_tokens)
            if next_token is None: break
            output.append(next_token)
            current = tuple(output[-n:])
        else:
            break

    return output

def merge_models(model_list):
    final_model = {}

    for model in model_list:
        for gram in model.keys():
            if gram in final_model:
                final_model[gram] += model[gram]
            else:
                final_model[gram] = model[gram]

    return final_model
