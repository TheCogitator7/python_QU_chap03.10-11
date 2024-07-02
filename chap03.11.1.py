#데이터프레임에 함수 적용하기
#apply() 메서드를 사용하면 시리즈나 데이터프레임의 개별 원소에 함수를 적용할 수 있다.
#
#시리즈 객체에 apply() 메서드를 적용하면 모든 원소를 함수에 적용하여 결과값을 반환한다.

#series.apply(함수)

#먼저, 펭귄 데이터에서 'bill_length_mm' 열만 선택해 샘플 시리즈 객체를 만들어보자

import seaborn as sns
import numpy as np

df=sns.load_dataset('penguins')
bill_length_mm=df['bill_length_mm']

print(bill_length_mm.head())
print()
print()


#해당 시리즈의 제곱근을 구해보자

result=bill_length_mm.apply(np.sqrt)
print(result.head())
print()
print()


#함수를 적용해서 구해보면
def mm_to_cm(num):
    return num/10

result_2=bill_length_mm.apply(mm_to_cm)
print(result_2.head())
print()
print()


