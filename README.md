# FINANCE TRACKER

An offline desktop-based application designed for students to monitor their daily spending habits, budget allocation, and overall financial health. With an intuitive user interface and insightful analytics, the tool simplifies financial management for users who may lack extensive budgeting experience.

> **Project Info:**  
> This project was developed as a final requirement for the course _Object-Oriented Programming_ (1st Year, 2nd Semester).
>
> **School Project:** Yes

---

| Name          | GitHub Username                                          | Role(s)                             |
| ------------- | -------------------------------------------------------- | ----------------------------------- |
| [Denver S.]   | _(No GitHub)_                                            | Project Manager                     |
| [Harvy Z.]    | _(No GitHub)_                                            | Lead Engineer                       |
| [Stella S.]   | _(No GitHub)_                                            | Quality Tester                      |
| [Eger M.]     | [@ItIsMeMyselfAndI](https://github.com/ItIsMeMyselfAndI) | Senior Developer (Backend/Frontend) |
| [Leilan A.]   | _(No GitHub)_                                            | Junior Developer (Backend)          |
| [Nouville N.] | _(No GitHub)_                                            | Junior Developer (Backend)          |

---

# INSTRUCTIONS

1. **Clone the repository**## Contributors & Roles

   ```bash
   git clone https://github.com/ItIsMeMyselfAndI/finance-tracker.git
   ```

2. **Navigate to the created folder**

   ```bash
   cd finance-tracker
   ```

3. **Install the dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

---

## Compile to an executable

1. Compile using pyinstaller

   ```bash
   pyinstaller main.spec
   ```

2. Executable location
   ```bash
   cd dist/main
   ls
   # Output: Finance-Tracker.exe
   ```

---

# FEATURES

1. **Login/Sign up**
   - User authentication
2. **Summary report**
   - Total balance, income, expenses, savings, investment
3. **Adding new transactions**
   - Date, category, description, amount (required)
4. **Editing existing transactions**
   - Date, category, description, amount (optional)
5. **Analytics**
   - Recent transactions, monthly/quarterly graph
6. **Transaction history**
   - Filter by type/category, paginated table
