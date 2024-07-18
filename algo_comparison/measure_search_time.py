import timeit
import gdown
import boyer_moore
import kmp_search
import rabin_karp

# Завантаження файлів із Google Drive
file1_url = 'https://drive.google.com/uc?id=18_R5vEQ3eDuy2VdV3K5Lu-R-B-adxXZh'
file2_url = 'https://drive.google.com/uc?id=13hSt4JkJc11nckZZz2yoFHYL89a4XkMZ'

gdown.download(file1_url, 'article1.txt', quiet=False)
gdown.download(file2_url, 'article2.txt', quiet=False)

# Функція для визначення кодування та завантаження тексту
def read_file(file_path):
    encodings = ['utf-8', 'latin-1', 'cp1252']
    for enc in encodings:
        try:
            with open(file_path, 'r', encoding=enc) as file:
                return file.read()
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError(f"Не вдалося прочитати файл {file_path} з використанням доступних кодувань.")

# Функція для вимірювання часу виконання
def measure_search_time(search_func, text, pattern):
    globals_dict = globals()
    globals_dict['text'] = text
    globals_dict['pattern'] = pattern
    setup_code = f'from __main__ import {search_func.__module__}'
    test_code = f'{search_func.__module__}.{search_func.__name__}(text, pattern)'
    times = timeit.repeat(setup=setup_code, stmt=test_code, globals=globals_dict, repeat=5, number=1)
    return min(times)

# Аналіз результатів та підсумки
def print_summary(results):
    summary = {}
    for case in ['article1_existing', 'article1_non_existing', 'article2_existing', 'article2_non_existing']:
        best_algo = min(results, key=lambda algo: results[algo][case])
        summary[case] = (best_algo, results[best_algo][case])
    
    print("\n### Підсумки аналізу ###")
    for case, (algo, time) in summary.items():
        print(f"Найшвидший алгоритм для {case}: {algo} з часом {time:.6f} секунд")
    return summary

if __name__ == "__main__":
    # Завантаження текстових файлів з визначенням кодування
    article1 = read_file('article1.txt')
    article2 = read_file('article2.txt')

    # Підрядки для пошуку
    existing_substring = "text"  # Замість цього підрядка вставте той, що дійсно існує в текстах
    non_existing_substring = "non_existing_substring"  # Замість цього підрядка вставте той, що не існує в текстах

    # Алгоритми пошуку
    search_algorithms = [boyer_moore.boyer_moore, kmp_search.kmp_search, rabin_karp.rabin_karp]

    # Вимірювання часу виконання
    results = {}
    for search_func in search_algorithms:
        results[search_func.__name__] = {}
        results[search_func.__name__]['article1_existing'] = measure_search_time(search_func, article1, existing_substring)
        results[search_func.__name__]['article1_non_existing'] = measure_search_time(search_func, article1, non_existing_substring)
        results[search_func.__name__]['article2_existing'] = measure_search_time(search_func, article2, existing_substring)
        results[search_func.__name__]['article2_non_existing'] = measure_search_time(search_func, article2, non_existing_substring)

    # Виведення результатів
    for algo_name, algo_results in results.items():
        print(f"{algo_name}:")
        for case, time_taken in algo_results.items():
            print(f"  {case}: {time_taken:.6f} seconds")

    # Виведення підсумків
    summary = print_summary(results)

    # Запис результатів в README.md
    with open('README.md', 'w') as f:
        f.write("# Порівняльний аналіз алгоритмів пошуку підрядка\n\n")
        f.write("### Результати вимірювань часу виконання:\n")
        for algo_name, algo_results in results.items():
            f.write(f"**{algo_name}**:\n")
            for case, time_taken in algo_results.items():
                f.write(f"- {case}: {time_taken:.6f} seconds\n")
        f.write("\n### Підсумки аналізу ###\n")
        for case, (algo, time) in summary.items():
            f.write(f"Найшвидший алгоритм для {case}: {algo} з часом {time:.6f} секунд\n")
