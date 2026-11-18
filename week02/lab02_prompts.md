# Lab 02 CLI comparison journal

Do not include passwords, tokens, API keys, or complete authentication output.

## Tool check

### GitHub Copilot CLI

I installed and authenticated GitHub Copilot CLI. I verified the installation using copilot --version, which returned version 1.0.82.

### Antigravity CLI

I installed and verified Antigravity CLI. I used agy --version, which returned version 1.1.23. The antigravity command was not recognized, but the agy command worked successfully.

## Shared task

### Shared prompt

```text
Review my Lab 02 Python code and its tests. Examine the functions, identify any potential errors or edge cases, and explain how you would improve the implementation. Do not modify any files yet. Explain your reasoning step by step and identify which tests should be used to verify the code.
```

### Copilot CLI observations

Copilot suggested reviewing the existing Python code and comparing each function against the requirements and tests. Its approach focused on identifying possible errors, checking whether the functions handled different inputs correctly, and making sure the implementation matched what the assignment expected. I thought this was helpful because it emphasized checking the code before making changes. I would still verify its suggestions by running the provided pytest tests and checking edge cases rather than assuming every recommendation was correct.


### Antigravity CLI observations

Antigravity also focused on reviewing the Python functions and identifying possible problems before changing the code. Its suggested approach involved looking at how the functions were written, considering different possible inputs, and using the tests to determine whether the code behaved as expected. I found this approach useful because it encouraged testing the code instead of immediately rewriting it. I would want to verify that its recommendations followed the assignment instructions and did not introduce unnecessary changes to working code.

### Comparison

Both tools were useful for reviewing code and thinking about possible errors before making changes. Copilot provided a way to examine the functions and consider how they should be tested. Antigravity also emphasized checking the implementation against the expected behavior and considering edge cases. Both approaches were helpful, but I would not automatically accept every suggestion from either tool. It is important to compare their recommendations with the actual assignment requirements and the tests provided. I would use the suggestions from both tools together, choosing the recommendations that make the most sense and are supported by the tests. Overall, I would use the tools as a starting point for understanding and improving my code rather than letting them make every decision for me.

## Test-guided implementation

The tests were an important part of checking whether my final code worked correctly. Instead of only relying on whether the code looked right, I used pytest to check the functions against the expected results. When a test failed, I used the error message to understand what needed to be corrected. I also considered different inputs and edge cases to make sure the functions would work beyond just one example. After making changes, I ran the tests again to check whether the problems had been resolved. This helped me understand that passing tests is important because it provides evidence that the code follows the expected function requirements. I used the test results and assignment instructions together to guide my final implementation.

## Preferred tool combination

I think using a combination of different tools is the most helpful because each one can support a different part of the coding process. Browser-based ChatGPT is useful when I need an explanation of a concept or help understanding an assignment step by step. GitHub Copilot in VS Code is convenient because it can provide suggestions while I am actually writing code. Copilot CLI and Antigravity CLI are useful for reviewing code and getting another perspective from the terminal. At this point, I prefer using ChatGPT to understand the assignment, VS Code to write and edit the code, and the CLI tools to review my work and consider possible improvements. I would change this combination if I were working on a larger project or a more complicated problem where one tool provided significantly better suggestions than the others. I think it is important to use these tools to learn and check my work rather than depend on them completely.