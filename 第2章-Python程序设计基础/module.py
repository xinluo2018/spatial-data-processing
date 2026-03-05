### 自动统计出超出某分数的科目数。
def num_higher_(s, s_high=90):
  num = 0
  for score in s:
    # print(score)
    if score >= s_high:
      num=num+1
  return num 
