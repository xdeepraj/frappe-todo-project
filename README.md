# 📋 todo_app

A simple task management app built with the Frappe Framework.

---

## 🚀 Features

- Create, update, and delete tasks  
- Mark tasks as **Done** from the list view via an action button  
- Track:
  - **Status**
  - **Due Date**
  - **Priority**
- View a report of all tasks  
- UI enhancements using:
  - Frappe Desk customizations
  - List View customizations
- Includes fixtures:
  - Custom DocType: `Task`
  - Client Script: "Mark as Done" button
  - Report: Task Summary
  - Custom List View with extra columns

---

## 🛠 Installation

Clone your bench and get the app:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app https://github.com/xdeepraj/frappe-todo-project.git --branch main
bench --site yoursite.local install-app todo_app
```

---

## 🔄 Run Migrations

Make sure to apply the necessary database migrations:

```bash
bench --site yoursite.local migrate
```

---

## 💡 Usage

Start your bench:

```bash
bench start
```

Then open in your browser:

[http://localhost:8000](http://localhost:8000)

Navigate to the **Task** module and create a new Task.

---

## 📁 Fixtures

The following customizations are included as fixtures:

- **Custom Doctype** → `Task`
- **Client Script** → List view button for "Mark as Done"
- **Report** → Task Summary
- **List View** → Custom columns:
  - Status
  - Due Date
  - Priority

To export updated fixtures:

```bash
bench --site yoursite.local export-fixtures
```

Fixtures are stored in:

```bash
todo_app/todo_app/fixtures/
```

---

## 👤 Author

**Deepraj**  
📧 [iamdeeprajsarkar@gmail.com](mailto:iamdeeprajsarkar@gmail.com)
