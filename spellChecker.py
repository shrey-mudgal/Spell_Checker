
import tkinter as tk
from tkinter import scrolledtext, messagebox
from textblob import TextBlob
import language_tool_python

# Initialize grammar tool
tool = language_tool_python.LanguageTool('en-US')

# Function to perform spelling and grammar check
def check_text():
    original = input_text.get("1.0", tk.END)
    if not original.strip():
        messagebox.showwarning("Empty Input", "Please enter some text to check.")
        return

    # Spelling correction using TextBlob
    corrected_blob = TextBlob(original)
    corrected_text = str(corrected_blob.correct())

    # Grammar correction using LanguageTool
    matches = tool.check(corrected_text)
    corrected_text = language_tool_python.utils.correct(corrected_text, matches)

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, corrected_text)

# GUI setup
root = tk.Tk()
root.title("Spelling and Grammar Checker")
root.geometry("800x500")
root.configure(bg="#f0f0f0")

# Input Label
tk.Label(root, text="Enter your text:", font=("Arial", 14), bg="#f0f0f0").pack(pady=5)

# Input Text Box
input_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=90, height=10, font=("Arial", 12))
input_text.pack(padx=10, pady=10)

# Check Button
tk.Button(root, text="Check Spelling & Grammar", command=check_text, font=("Arial", 12), bg="#4CAF50", fg="white").pack(pady=10)

# Output Label
tk.Label(root, text="Corrected text:", font=("Arial", 14), bg="#f0f0f0").pack(pady=5)

# Output Text Box
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=90, height=10, font=("Arial", 12))
output_text.pack(padx=10, pady=10)

# Start the GUI loop
root.mainloop()
