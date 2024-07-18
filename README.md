# Порівняльний аналіз алгоритмів пошуку підрядка

### Результати вимірювань часу виконання:
**boyer_moore**:
- article1_existing: 0.000809 seconds
- article1_non_existing: 0.000164 seconds
- article2_existing: 0.001090 seconds
- article2_non_existing: 0.000235 seconds
**kmp_search**:
- article1_existing: 0.001837 seconds
- article1_non_existing: 0.001878 seconds
- article2_existing: 0.002363 seconds
- article2_non_existing: 0.002732 seconds
**rabin_karp**:
- article1_existing: 0.003266 seconds
- article1_non_existing: 0.003446 seconds
- article2_existing: 0.004320 seconds
- article2_non_existing: 0.005009 seconds

### Підсумки аналізу ###
Найшвидший алгоритм для article1_existing: boyer_moore з часом 0.000809 секунд
Найшвидший алгоритм для article1_non_existing: boyer_moore з часом 0.000164 секунд
Найшвидший алгоритм для article2_existing: boyer_moore з часом 0.001090 секунд
Найшвидший алгоритм для article2_non_existing: boyer_moore з часом 0.000235 секунд
