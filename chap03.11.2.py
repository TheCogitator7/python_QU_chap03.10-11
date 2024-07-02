#데이터프레임에 함수 적용하기
#
#데이터프레임에 apply() 메서드를 적용하면
#모든 열 또는 행을 하나씩 분리하여 함수에 각 원소가 전달된 후 값이 반환된다.

#각 열에 적용 : DataFrame.apply(함수) 또는 DataFrame.apply(함수, axis=0)
#각 행에 적용 : DataFrame.apply(함수, axis=1)

#먼저 펭귄 데이터셋에서 숫자로만 이루어진 열을 선택해보자

import seaborn as sns
import pandas as pd
import numpy as np


df=sns.load_dataset('penguins')
df_num=df[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']]

print(df_num.head())
print()
print()

#DataFrame에 apply() 메소를 이용해 최대값을 구하는 max 함수를 적용해본다.
#apply(max) 또는 apply(max, axis=0)을 입력하면 각 열 별로 최대값을 구한다.
print(df_num.apply(max))
#df_num.apply(max, axis=0)
print()
print()

#각 행의 최대값을 구하면
print(df_num.apply(max, axis=1))
print()
print()
#첫 번째 행에서 최대값은 3750.0, 두 번째 행에서 최대값은 3800.0 이 된다.

#각 열에서 결측치가 얼마나 있는지 확인하면

def num_null(data):
    null_vec=pd.isnull(data) #결측치 여부를 판단, 결측치면 True, 아니면 False
    null_count=np.sum(null_vec) #True면 1, False 면 0 에 해당하는 값을 더함

    return null_count

print(df_num.apply(num_null))
print()
print()
