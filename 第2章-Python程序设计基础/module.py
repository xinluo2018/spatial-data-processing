### 自动统计出超出某分数的科目数。
def num_higher_(s, s_high=90):
  num = 0
  for score in s:
    # print(score)
    if score >= s_high:
      num=num+1
  return num 

### 自动统计出超出某分数的科目数。
def num_lower_(s, s_low=60):
  num = 0
  for score in s:
    # print(score)
    if score < s_low:
      num=num+1
  return num 



