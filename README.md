# goit-algo-hw-04
Результати тестування
--------------------------- TESTS ----------------------------------
--------------------------------------------------------------------

Tests on random datas...
--------------------------------------------------
| Timsort (sorted)     | Size 10000    | Time: 7.0858 ms |
| Merge Sort           | Size 10000    | Time: 18.5643 ms |
| Insertion Sort       | Size 10000    | Time: 1882.2356 ms |
| Timsort (sorted)     | Size 50000    | Time: 12.9098 ms |
| Merge Sort           | Size 50000    | Time: 98.8268 ms |
| Insertion Sort       | Size 50000    | Time: 46710.4304 ms |
| Timsort (sorted)     | Size 100000   | Time: 27.1025 ms |
| Merge Sort           | Size 100000   | Time: 209.9388 ms |
| Insertion Sort       | Size 100000   | Time: 187464.5485 ms |

Tests on sorted datas...
--------------------------------------------------
| Timsort (sorted)     | Size 10000    | Time: 1.6737 ms |
| Merge Sort           | Size 10000    | Time: 14.6597 ms |
| Insertion Sort       | Size 10000    | Time: 2.4160 ms |
| Timsort (sorted)     | Size 50000    | Time: 8.2005 ms |
| Merge Sort           | Size 50000    | Time: 81.4702 ms |
| Insertion Sort       | Size 50000    | Time: 11.8653 ms |
| Timsort (sorted)     | Size 100000   | Time: 16.2336 ms |
| Merge Sort           | Size 100000   | Time: 172.4509 ms |
| Insertion Sort       | Size 100000   | Time: 24.0088 ms |

Tests on random datas...
--------------------------------------------------
| Timsort (sorted)     | Size 100      | Time: 0.0199 ms |
| Merge Sort           | Size 100      | Time: 0.1058 ms |
| Insertion Sort       | Size 100      | Time: 0.1493 ms |
| Timsort (sorted)     | Size 500      | Time: 0.1024 ms |
| Merge Sort           | Size 500      | Time: 0.6423 ms |
| Insertion Sort       | Size 500      | Time: 4.0567 ms |
| Timsort (sorted)     | Size 1000     | Time: 0.2208 ms |
| Merge Sort           | Size 1000     | Time: 1.4221 ms |
| Insertion Sort       | Size 1000     | Time: 16.8376 ms |
| Timsort (sorted)     | Size 2000     | Time: 0.4550 ms |
| Merge Sort           | Size 2000     | Time: 2.9267 ms |
| Insertion Sort       | Size 2000     | Time: 68.2322 ms |

Tests on reversed datas...
--------------------------------------------------
| Timsort (sorted)     | Size 10000    | Time: 1.7193 ms |
| Merge Sort           | Size 10000    | Time: 14.7939 ms |
| Insertion Sort       | Size 10000    | Time: 3637.3982 ms |
| Timsort (sorted)     | Size 50000    | Time: 8.2895 ms |
| Merge Sort           | Size 50000    | Time: 83.3411 ms |
| Insertion Sort       | Size 50000    | Time: 93268.2467 ms |
| Timsort (sorted)     | Size 100000   | Time: 16.6550 ms |
| Merge Sort           | Size 100000   | Time: 174.8038 ms |
| Insertion Sort       | Size 100000   | Time: 376424.2295 ms |

Tests on reversed datas...
--------------------------------------------------
| Timsort (sorted)     | Size 100      | Time: 0.0303 ms |
| Merge Sort           | Size 100      | Time: 0.1102 ms |
| Insertion Sort       | Size 100      | Time: 0.3009 ms |
| Timsort (sorted)     | Size 500      | Time: 0.0870 ms |
| Merge Sort           | Size 500      | Time: 0.5850 ms |
| Insertion Sort       | Size 500      | Time: 8.4107 ms |
| Timsort (sorted)     | Size 1000     | Time: 0.1708 ms |
| Merge Sort           | Size 1000     | Time: 1.3426 ms |
| Insertion Sort       | Size 1000     | Time: 33.2115 ms |
| Timsort (sorted)     | Size 2000     | Time: 0.3275 ms |
| Merge Sort           | Size 2000     | Time: 2.4850 ms |
| Insertion Sort       | Size 2000     | Time: 136.2247 ms |


Відповідно до проведених тестувань, можна зробити наступні висновки:
Timsort (Python sorted) та Merge Sort демонструють лінійний ріст часу відносно NlogN. Вони є найкращими для великих наборів даних.
Insertion Sort на великих масивах катастрофічно повільний, що підтверджує його квадратичну складність O(N2).
Insertion Sort має низькі витрати і є дуже швидким для малих масивів.
На відсортованих масивах для розміру даних 100 000 Timsort та Insertion Sort є надзвичайно швидкими (O(N)), тоді як Merge Sort залишається в O(NlogN), оскільки йому завжди потрібно ділити та зливати масиви, незалежно від їх впорядкованості.

Емпіричні дані підтверджують теоретичні оцінки та доводять перевагу Timsort:
Найкращий Випадок (O(N)): Timsort виявляє, що дані вже відсортовані (або майже відсортовані) і працює з тією ж швидкістю, що й O(N) Insertion Sort, залишаючи Merge Sort позаду.
Середній/Найгірший Випадок (O(NlogN)): На великих випадкових масивах Timsort працює трохи швидше, ніж класичний Merge Sort, завдяки низьким витратам Insertion Sort на початкових етапах.

Саме завдяки цій гібридній стратегії та експлуатації властивостей реальних даних, Timsort є швидким як для вже впорядкованих, так і для випадкових великих масивів, що робить його універсальним переможцем. 
