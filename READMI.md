# 🎨 ASCII Art Generator (KL Rahul Edition)

This project is a Python-based application that converts a digital image of Indian Cricketer **KL Rahul** into ASCII art. It utilizes pixel brightness mapping to generate a text-based representation of the image.

## 📋 Project Overview
* **Student Name:** Vipin Kumar
* **Course:** B.Tech CSE (AIML)
* **Group:** G4 (SN 95)
* **Project Type:** Minor Project II
* **Objective:** To demonstrate logic building, loops, and image processing concepts using Python.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Library:** Pillow (PIL) for image manipulation.
* **Tools:** Google Colab, VS Code.

## ⚙️ How It Works
The program follows these steps:
1.  **Image Loading:** Opens the source image (`kl rahul2.jpg`).
2.  **Resizing:** Adjusts dimensions to match text aspect ratio (height is reduced by factor 0.5) to prevent the image from looking stretched.
3.  **Grayscale Conversion:** Converts the colored image into black and white (L mode) to calculate pixel brightness.
4.  **ASCII Mapping:** Maps every pixel's brightness value (0-255) to a specific character in the ASCII string (`@`, `#`, `S`, `%`, etc.). Darker pixels get denser characters (`@`), and lighter pixels get empty spaces.

## 🚀 How to Run

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/vipincoder95/ASCII-Art-KL-Rahul.git](https://github.com/vipincoder95/ASCII-Art-KL-Rahul.git)
    cd ASCII-Art-KL-Rahul
    ```

2.  **Install Dependencies**
    You need to install the `Pillow` library:
    ```bash
    pip install pillow
    ```

3.  **Run the Script**
    Make sure your image is in the same folder.
    ```bash
    python main.py
    ```

4.  **Output**
    * The ASCII art will be displayed in the terminal.
    * A text file named `project_kl_rahul.txt` will be generated with the output.

## 📂 Project Structure
## 👨‍💻 Author
**Vipin Kumar**
B.Tech CSE (AIML) Student
Rungta College Of Engineering & Technology
