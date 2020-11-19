Status: published
Date: 2020-11-19 08:55:27
Author: Jerry Su
Slug: CMRC-Metric
Title: CMRC Metric
Category: 
Tags: Deep Learning, NLP 

## F1

```
# find longest common string
def find_lcs(s1, s2):
	m = [[0 for i in range(len(s2)+1)] for j in range(len(s1)+1)]
	mmax = 0
	p = 0
	for i in range(len(s1)):
		for j in range(len(s2)):
			if s1[i] == s2[j]:
				m[i+1][j+1] = m[i][j]+1
				if m[i+1][j+1] > mmax:
					mmax=m[i+1][j+1]
					p=i+1
	return s1[p-mmax:p], mmax
    
 
def calc_f1_score(answers, prediction):
	f1_scores = []
	for ans in answers:
		ans_segs = mixed_segmentation(ans, rm_punc=True)
		prediction_segs = mixed_segmentation(prediction, rm_punc=True)
		lcs, lcs_len = find_lcs(ans_segs, prediction_segs)
		if lcs_len == 0:
			f1_scores.append(0)
			continue
		precision 	= 1.0 * lcs_len / len(prediction_segs)
		recall 		= 1.0 * lcs_len / len(ans_segs)
		f1 			= (2 * precision*recall) / (precision + recall)
		f1_scores.append(f1)
	return max(f1_scores)
```

## EM

```
# remove punctuation
def remove_punctuation(in_str):
	in_str = in_str.lower().strip()
	sp_char = ['-', ':', '_', '*', '^', '/', '\\', '~', '`', '+', '=', '，', '。', '：', '？', '！', '“', '”', '；', '’',
			   '《', '》', '……', '·', '、', '「', '」', '（', '）', '－', '～', '『', '』']
	out_segs = []
	for char in in_str:
		if char in sp_char:
			continue
		else:
			out_segs.append(char)
	return ''.join(out_segs)


def calc_em_score(answers, prediction):
	em = 0
	for ans in answers:
		ans_ = remove_punctuation(ans)
		prediction_ = remove_punctuation(prediction)
		if ans_ == prediction_:
			em = 1
			break
	return em
```