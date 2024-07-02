#데이터 재구조화

import seaborn as sns

#데이터프레임의 행과 열 구조를 변형하거나 특정 요인에 따라
#집계를 하는 방법
#pandas 에서 데이터 재구조화에 사용되는 함수는 melt(), pivot_table(), stack(), unstack()
#이 있다.

df=sns.load_dataset('penguins')

#species : 펭귄 종으로 Adelie, Gentoo, Chinstrap 세가지 종이 있다.
#island : 남극의 펭귄 서식지로 Torgersen, Biscoe, Dream 이 있다.
#bill_length_mm : 부리의 길이에 해당한다.
#bill_depth_mm : 부리의 위아래 두께에 해당한다.
#flipper_length_mm : 펭귄의 날개에 해당한다.
#body_mass_g : 몸무게에 해당한다.
#sex : 성별에 해당한다.

print(df.head())
print()
print()

#melt() 함수는 ID 변수를 기준으로 원본 데이터프레임의 열 이름들을 variable 열에 넣고
# 각 열에 있던 데이터는 value 열에 넣어 아래로 긴 형태로 만들어준다.

print(df.melt(id_vars=['species', 'island']).head(10))
print()
print()

#pivot_table() 함수는 엑셀의 피봇 테이블과 비슷하며 총 4개의 입력값이 필요하다.
#index : 행 인덱스
#columns : 열 인덱스
#values : 데이터 값
#aggfunc : 데이터 집계 함수

#펭귄 데이터의 species와 island 별로 bill_length_mm의 평균을 구해보자

df_pivot_1=df.pivot_table(index='species', columns='island', values='bill_length_mm', aggfunc='mean')
print(df_pivot_1)
print()
print()



#각 인덱스를 하나가 아닌 여러 개를 입력할 수 있으며, 데이터 값, 집계 함수 역시 여러 개를 입력할 수 있다.

df_pivot_2=df.pivot_table(index=['species', 'sex'], columns='island', values=['bill_length_mm', 'flipper_length_mm'], aggfunc=['mean', 'count'])
print(df_pivot_2)
print()
print()


#stack() 메서드와 unstack() 메서드는 열 인덱스를 행 인덱스로 바꾸거나
#반대로 행 인덱스를 열 인덱스로 변경한다.

#stack() : 열 인덱스를 행 인덱스로 변환
#unstack() : 행 인덱스를 열 인덱스로 변환

df_pivot_4=df.pivot_table(index=['species', 'sex'], columns='island', values='bill_length_mm', aggfunc='mean')
print(df_pivot_4)
print()
print()

#위 데이터프레임에 stack() 메서드를 적용해 보면
print(df_pivot_4.stack())
print()
print()

#위의 결과물은 시리즈 형태이며, 데이터프레임으로 변경하고 싶을 경우
#to_frame() 메서드를 추가한다.

print(df_pivot_4.stack().to_frame())
print()
print()

#unstack() 메서드를 적용해보면
print(df_pivot_4.unstack())
print()
print()





 
