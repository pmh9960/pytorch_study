# Inplace 연산

## 결론 : 쓰지마라.

Dirty 객체가 생기는데 backward에서 gradient를 계산하기 위한 context가 dirty 한 경우 gradient를 계산할 수 없다. (내용물이 바뀌었기 때문.)

정 쓰고 싶다면

1. Out-place로 일단 다 만들어라. (OOM이 떴다면)
2. 하나 씩 in-place로 바꿔가면서 오류가 나는지 확인 ;;

practical하게 inplace 연산을 했을 때 메모리 사용량
760.7 => 652.7

결론 : 그냥 쓰지 마라.
