A small project I made to
1. Try out leveraging Rust from Python
2. Test the performance difference between the languages (using naïve matrix multiplication as the test case)
3. Try out the new AI Assistant tool from JetBrains

All-in-all, as a Rust newbie who has never used PyO3 or any other way to leverage Rust functionality in Python, the 
AI Assistant was extremely helpful and allowed me to complete this project in less than half a day.

As for the performance, it was as you might expect:


| Matrix Size | Iterations | Avg. Python Time (sec) | Avg. Rust Time (sec) | Rust Time as % of Python Time |
|-------------|------------|------------------------|----------------------|-------------------------------|
| 3x3         | 10000      | 3.64e-06               | 1.23e-06             | 33.87%                        |
| 10x10       | 1000       | 6.71e-05               | 7.73e-06             | 11.53%                        |
| 100x100     | 100        | 5.64e-02               | 3.01e-03             | 5.33%                         |
| 1000x1000   | 3          | 6.26e+01               | 2.78e+00             | 4.44%                         |
