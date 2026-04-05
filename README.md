# Control Flow & Functions — Week 2 Assignment
**Due:** Next weekly class

The files `Q01.py`, `Q02.py`, … `Q10.py` are already created in this repository. Open each file, write your solution where it says `# --- YOUR CODE HERE ---`, and commit your changes.

> **Auto-grading is enabled.** Every time you push your code, GitHub will automatically run tests and show you how many you passed. You can push as many times as you want before the deadline.

## Running Tests Locally

To run all tests on your computer, first install `pytest`:

```powershell
python -m pip install pytest
```

Then run all tests from this assignment folder:

```powershell
python -m pytest tests -v
```

To run tests for only one question:

```powershell
python -m pytest tests/test_q01.py -v
```

This will show which tests passed and which tests failed, so you can fix your code before submitting.

## How to Submit

After you finish your work, run these commands from the assignment folder:

```powershell
git add .
git commit -m "Completed Week 2 assignment"
git push
```

This will upload your latest code to GitHub and trigger auto-grading.

---

## If-Else

**Q01.** Ask the user for a score (integer, 0–100). Print the letter grade using these rules:

| Score Range | Grade |
|-------------|-------|
| 90 – 100   | A     |
| 80 – 89    | B     |
| 70 – 79    | C     |
| 60 – 69    | D     |
| Below 60   | F     |

If the score is below 0 or above 100, print `Invalid score`.

**Sample Input 1:**
```
Enter your score: 85
```
**Sample Output 1:**
```
Grade: B
```

**Sample Input 2:**
```
Enter your score: 105
```
**Sample Output 2:**
```
Invalid score
```

---

**Q02.** Ask the user for a year (integer). Print whether it is a **leap year** or not.

**Rules:**
- A year is a leap year if it is divisible by 4
- BUT not if it is divisible by 100
- UNLESS it is also divisible by 400

**Sample Input 1:**
```
Enter a year: 2024
```
**Sample Output 1:**
```
2024 is a leap year
```

**Sample Input 2:**
```
Enter a year: 1900
```
**Sample Output 2:**
```
1900 is not a leap year
```

---

## For Loop

**Q03.** Ask the user for a positive integer `n`. Print its multiplication table from 1 to 10.

**Sample Input:**
```
Enter a number: 5
```
**Sample Output:**
```
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
```

---

**Q04.** Ask the user for a positive integer `n`. Print a right-angled triangle pattern of `*` with `n` rows.

**Sample Input:**
```
Enter number of rows: 5
```
**Sample Output:**
```
*
**
***
****
*****
```

---

**Q05.** Ask the user for a positive integer `n`. Print all numbers from 1 to `n`, but:
- For multiples of 3, print `Fizz` instead of the number
- For multiples of 5, print `Buzz` instead of the number
- For multiples of both 3 and 5, print `FizzBuzz` instead of the number

**Sample Input:**
```
Enter n: 15
```
**Sample Output:**
```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
```

---

**Q06.** Ask the user for a positive integer `n`. Compute and print its **factorial** (n!) using a `for` loop.

Recall: `5! = 5 × 4 × 3 × 2 × 1 = 120` and `0! = 1`.

**Sample Input 1:**
```
Enter a number: 5
```
**Sample Output 1:**
```
5! = 120
```

**Sample Input 2:**
```
Enter a number: 0
```
**Sample Output 2:**
```
0! = 1
```

---

## While Loop

**Q07.** Ask the user for a positive integer. Print the **reverse** of the number using a while loop.

**Sample Input 1:**
```
Enter a number: 1234
```
**Sample Output 1:**
```
Reversed: 4321
```

**Sample Input 2:**
```
Enter a number: 5000
```
**Sample Output 2:**
```
Reversed: 5
```

---

**Q08.** Ask the user for a positive integer. Print the **sum of its digits** using a while loop.

**Sample Input:**
```
Enter a number: 9876
```
**Sample Output:**
```
Sum of digits of 9876 = 30
```

---

## Functions

**Q09.** Write the following two functions:

1. `greet(name, greeting="Hello")` — returns the string `"{greeting}, {name}!"`
2. `power(base, exp=2)` — returns `base` raised to `exp`

Then in the `if __name__ == "__main__":` block, demonstrate them:
- Call `greet("Alice")` and `greet("Bob", "Hi")`
- Call `power(5)` and `power(2, 10)`
- Print all four results.

**Expected Output:**
```
Hello, Alice!
Hi, Bob!
25
1024
```

---

**Q10.** Write the following two functions that demonstrate **call by reference** (mutating a list in-place):

1. `add_element(lst, element)` — appends `element` to `lst` (modifies the original list, returns nothing)
2. `double_elements(lst)` — multiplies every element in `lst` by 2 **in-place** (returns nothing)

Then in the `if __name__ == "__main__":` block, demonstrate:
- Create a list `numbers = [1, 2, 3]`
- Call `add_element(numbers, 4)` and print the list
- Call `double_elements(numbers)` and print the list

**Expected Output:**
```
[1, 2, 3, 4]
[2, 4, 6, 8]
```