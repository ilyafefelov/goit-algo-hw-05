import timeit
import requests
import boyer_moore
import kmp_search as kmp
import rabin_karp


def download_article(url, encodings=['utf-8', 'utf-16', 'cp1251']):
    response = requests.get(url)
    response.raise_for_status()
    
    for encoding in encodings:
        try:
            return response.content.decode(encoding)
        except UnicodeDecodeError:
            continue
    raise ValueError("Unable to decode the content with the provided encodings")

# Download and decode articles
article1_url = 'https://drive.google.com/uc?id=18_R5vEQ3eDuy2VdV3K5Lu-R-B-adxXZh'
article2_url = 'https://drive.google.com/uc?id=13hSt4JkJc11nckZZz2yoFHYL89a4XkMZ'

article1 = download_article(article1_url)
article2 = download_article(article2_url)

# Patterns to search
pattern_existing = "а"
pattern_non_existing = "неіснуючийпатерн"

# Function to test algorithms
def test_algorithms(article, pattern_existing, pattern_non_existing, repetitions=100):
    results = {
        'Boyer-Moore': {'Existing': 0, 'Non-existing': 0, 'Existing_time': 0, 'Non-existing_time': 0},
        'KMP': {'Existing': 0, 'Non-existing': 0, 'Existing_time': 0, 'Non-existing_time': 0},
        'Rabin-Karp': {'Existing': 0, 'Non-existing': 0, 'Existing_time': 0, 'Non-existing_time': 0},
    }
    
    def measure_time(func, *args):
        timer = timeit.Timer(lambda: func(*args))
        return timer.timeit(number=repetitions) / repetitions

    print("Testing Boyer-Moore on Existing Pattern")
    boyer_moore_result_existing = boyer_moore.boyer_moore(article, pattern_existing)
    results['Boyer-Moore']['Existing_time'] = measure_time(boyer_moore.boyer_moore, article, pattern_existing)
    results['Boyer-Moore']['Existing'] = 1 if boyer_moore_result_existing != -1 else 0

    print("Testing Boyer-Moore on Non-existing Pattern")
    boyer_moore_result_non_existing = boyer_moore.boyer_moore(article, pattern_non_existing)
    results['Boyer-Moore']['Non-existing_time'] = measure_time(boyer_moore.boyer_moore, article, pattern_non_existing)
    results['Boyer-Moore']['Non-existing'] = 1 if boyer_moore_result_non_existing != -1 else 0

    print("Testing KMP on Existing Pattern")
    kmp_result_existing = kmp.kmp_search(article, pattern_existing)
    results['KMP']['Existing_time'] = measure_time(kmp.kmp_search, article, pattern_existing)
    results['KMP']['Existing'] = 1 if kmp_result_existing != -1 else 0

    print("Testing KMP on Non-existing Pattern")
    kmp_result_non_existing = kmp.kmp_search(article, pattern_non_existing)
    results['KMP']['Non-existing_time'] = measure_time(kmp.kmp_search, article, pattern_non_existing)
    results['KMP']['Non-existing'] = 1 if kmp_result_non_existing != -1 else 0

    print("Testing Rabin-Karp on Existing Pattern")
    rabin_karp_result_existing = rabin_karp.rabin_karp(article, pattern_existing)
    results['Rabin-Karp']['Existing_time'] = measure_time(rabin_karp.rabin_karp, article, pattern_existing)
    results['Rabin-Karp']['Existing'] = 1 if rabin_karp_result_existing != -1 else 0

    print("Testing Rabin-Karp on Non-existing Pattern")
    rabin_karp_result_non_existing = rabin_karp.rabin_karp(article, pattern_non_existing)
    results['Rabin-Karp']['Non-existing_time'] = measure_time(rabin_karp.rabin_karp, article, pattern_non_existing)
    results['Rabin-Karp']['Non-existing'] = 1 if rabin_karp_result_non_existing != -1 else 0
    
    return results

# Run the tests
results_article1 = test_algorithms(article1, pattern_existing, pattern_non_existing)
results_article2 = test_algorithms(article2, pattern_existing, pattern_non_existing)

# Determine the quickest and slowest algorithms
def summarize_results(results):
    summary = {
        'quickest_existing': min(results, key=lambda x: results[x]['Existing_time']),
        'slowest_non_existing': max(results, key=lambda x: results[x]['Non-existing_time']),
    }
    return summary

summary_article1 = summarize_results(results_article1)
summary_article2 = summarize_results(results_article2)

# Write the results to readme.md
with open('./readme.md', 'w', encoding='utf-8') as file:
    file.write("# Comparative Analysis of Substring Search Algorithms\n\n")
    
    file.write("## Article 1 Results\n")
    for algo in results_article1:
        file.write(f"**{algo}:**\n")
        file.write(f"- Existing: {results_article1[algo]['Existing']} times, Time: {results_article1[algo]['Existing_time']} seconds\n")
        file.write(f"- Non-existing: {results_article1[algo]['Non-existing']} times, Time: {results_article1[algo]['Non-existing_time']} seconds\n")
    
    file.write("\n## Article 2 Results\n")
    for algo in results_article2:
        file.write(f"**{algo}:**\n")
        file.write(f"- Existing: {results_article2[algo]['Existing']} times, Time: {results_article2[algo]['Existing_time']} seconds\n")
        file.write(f"- Non-existing: {results_article2[algo]['Non-existing']} times, Time: {results_article2[algo]['Non-existing_time']} seconds\n")
    
    file.write("\n## Summary\n")
    file.write(f"Article 1: The quickest for existing was {summary_article1['quickest_existing']}\n")
    file.write(f"Article 1: The slowest for non-existing was {summary_article1['slowest_non_existing']}\n")
    file.write(f"Article 2: The quickest for existing was {summary_article2['quickest_existing']}\n")
    file.write(f"Article 2: The slowest for non-existing was {summary_article2['slowest_non_existing']}\n")

print("Results have been written to readme.md")
