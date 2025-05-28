# Amazon Web Scoping Script 🔎

This project is a browser automation script that performs **web scoping** on the Amazon website. It discovers and classifies **unique internal links** into categories such as product pages, category pages, and others.

> 📁 File: `webscoping.py`  
> 🧠 Submitted for: SaralX Internship Assignment  
> 🧑‍💻 Author: Divyesh Vadher  
> 🔗 [GitHub](https://github.com/DivyeshVadher) | [LinkedIn](https://linkedin.com/in/imdivyeshvadher)

---

## 🚀 Features

- ✅ Crawls internal links starting from `https://www.amazon.in`
- ✅ Uses **Selenium + BeautifulSoup** for JS-rendered page support
- ✅ Identifies and classifies links as:
  - 📦 Product pages
  - 📚 Category pages
  - 🧩 Other pages
- ✅ Layout-based clustering using DOM structure
- ✅ Output is saved in neatly separated `.txt` files

---

## 🧰 Tech Stack

- **Python 3.x**
- **Selenium** (for browser automation)
- **BeautifulSoup** (for HTML parsing)
- **Chrome WebDriver** (auto-managed via Selenium Manager)

---

## 📦 Installation

### 1. Clone the repository or extract the zip
```bash
cd webscoping
py webscoping.py
```


### 2. Run the python file
```bash
py webscoping.py
