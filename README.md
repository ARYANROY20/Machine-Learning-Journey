# Machine Learning Journey

This repository documents my learning journey as I study the theory, practice, and mathematics behind Data Science, Machine Learning, Deep Learning, and Natural Language Processing (NLP). It grows alongside my progress, from Python foundations to end-to-end projects, with notes, notebooks, exercises, and practical implementations.

## Learning progress

The sections below reflect what I have organized in the repository so far. I continue to expand the repository as I learn new topics and build small projects.

| Section | Topics |
|---|---|
| [1. Introduction](./1-Introduction/) | Python basics, environment setup, and a linear regression notebook |
| [2. Python Programming Language](./2-Python%20Programming%20Language/) | Python fundamentals, collections, functions, exception handling, packages, and file handling |
| [3. Object-Oriented Programming](./3-Object%20Oriented%20Programming/) | Classes, objects, inheritance, and OOP exercises |
| [4. Advanced Python](./4-Advance%20Python/) | Iterators, generators, decorators, and advanced Python patterns |
| [5. Data Analysis in Python](./5-Data%20Analysis%20In%20Python/) | NumPy, Pandas, data manipulation, file reading, and visualization with Matplotlib and Seaborn |
| [6. SQLite3](./6-SQLITE3/) | Databases, queries, transactions, relations, indexing, and backup/restore workflows |
| [7. Logging in Python](./7-Logging%20In%20Python/) | Basic and advanced logging patterns, rotating handlers, exception logging, and performance logging |
| [8. Multithreading & Multiprocessing](./8-Multithreading%20%26%20Multiprocessing/) | Threading and multiprocessing concepts, parallel processing, and concurrent task execution |
| [9. Memory Management](./9-Memory%20Management/) | Memory allocation, object lifecycle, references, and Python memory awareness |
| [10. Flask Framework](./10-Flask%20Framework/) | Web application basics with Flask, routing, and API development |
| [11. Streamlit](./11-Streamlit/) | Interactive dashboards and UI components with Streamlit |

## Areas I am exploring

- Strengthen my programming and data analysis foundations.
- Understand the mathematics and theory behind data science and machine learning methods.
- Explore classical Machine Learning, Deep Learning, and NLP.
- Learn modern Python application development with Flask and Streamlit.
- Understand memory behavior and efficient resource usage in Python.
- Apply what I learn through exercises, experiments, and end-to-end projects.
- Document notes, implementations, and project work as I progress.

## Getting started

1. Clone the repository:

   ```bash
   git clone https://github.com/ARYANROY20/Machine-Learning-Journey.git
   cd Machine-Learning-Journey
   ```

2. Open a notebook in VS Code or Jupyter Notebook, or run a standalone Python script from its section folder.

3. If the section provides a `requirements.txt`, create a virtual environment and install its dependencies. For example, on Windows:

   ```powershell
   cd "5-Data Analysis In Python"
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   python -m pip install -r requirements.txt
   ```

   Each section's dependencies are listed separately where applicable. Install the requirements for the section whose notebooks or scripts you want to run.

4. Run notebook cells in order. Some notebooks read data using relative paths, so set the notebook's working directory to its section folder.

To run the multiprocessing factorial example:

```powershell
cd "8-Multithreading & Multiprocessing"
python Factorial_multiprocessing.py
```

This script uses a multiprocessing pool to compute factorials in parallel and prints the results and elapsed time.

To run the Flask API example:

```powershell
cd "10-Flask Framework"
python api.py
```

To run the Streamlit app example:

```powershell
cd "11-Streamlit"
streamlit run app.py
```

## Repository structure

```text
Machine-Learning-Journey/
├── 1-Introduction/
├── 2-Python Programming Language/
├── 3-Object Oriented Programming/
├── 4-Advance Python/
├── 5-Data Analysis In Python/
├── 6-SQLITE3/
├── 7-Logging In Python/
├── 8-Multithreading & Multiprocessing/
├── 9-Memory Management/
├── 10-Flask Framework/
├── 11-Streamlit/
└── venv/
```

## Notes

- This is a personal learning repository, not a formal course; content is added as I progress and may include exercises, experiments, and work in progress.
- Some notebooks use CSV, Excel, or other data files stored alongside them.
- Virtual environments are not included in the repo; create one locally and install the dependencies you need for the section you are working on.
- The project now includes both backend/web-development learning (Flask) and interactive app development (Streamlit) alongside the core Python and data-science topics.
