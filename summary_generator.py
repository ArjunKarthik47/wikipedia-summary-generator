import wikipedia
import pyttsx3
import tkinter as tk
from tkinter import messagebox, scrolledtext
import os

def fetch_summary():
    topic = topic_entry.get().strip()
    if not topic:
        print("Input Error: Please enter a topic.")  # Terminal output
        return

    try:
        summary = wikipedia.summary(topic, sentences=10)
        summary_box.delete(1.0, tk.END)
        summary_box.insert(tk.END, summary)
    except wikipedia.DisambiguationError as e:
        print(f"Disambiguation Error: Topic is ambiguous. Try one of: {', '.join(e.options[:5])}")
    except wikipedia.PageError:
        print("Page Error: Page not found. Please try another topic.")
    except Exception as ex:
        print(f"Unexpected Error: {ex}")

def save_to_file():
    topic = topic_entry.get().strip()
    summary = summary_box.get(1.0, tk.END).strip()
    
    if not topic or not summary:
        messagebox.showwarning("Save Error", "Nothing to save. Please enter a topic and fetch the summary first.")
        return

    safe_topic = "".join(c for c in topic if c.isalnum() or c in (' ', '_')).rstrip()
    filename = f"{safe_topic}.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(summary)
    
    messagebox.showinfo("Success", f"Summary saved as '{filename}' in the current folder.")

def speak_summary():
    summary = summary_box.get(1.0, tk.END).strip()
    if not summary:
        messagebox.showwarning("No Summary", "Nothing to read aloud.")
        return

    engine = pyttsx3.init()
    engine.say(summary)
    engine.runAndWait()

# GUI Setup
root = tk.Tk()
root.title("Wikipedia Summary Tool")
root.geometry("700x500")
root.configure(bg="#f2f2f2")

# Layout
tk.Label(root, text="Wikipedia Topic:", font=("Segoe UI", 12), bg="#f2f2f2").pack(pady=(20, 5))
topic_entry = tk.Entry(root, width=50, font=("Segoe UI", 12))
topic_entry.pack(pady=(0, 10))

tk.Button(root, text="Fetch Summary", command=fetch_summary, font=("Segoe UI", 11), bg="#4CAF50", fg="white", width=20).pack()

summary_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=15, font=("Segoe UI", 11))
summary_box.pack(pady=15, padx=10)

# Action Buttons
button_frame = tk.Frame(root, bg="#f2f2f2")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Save as Topic File", command=save_to_file, font=("Segoe UI", 10), bg="#2196F3", fg="white", width=20).grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="Speak Summary", command=speak_summary, font=("Segoe UI", 10), bg="#FF5722", fg="white", width=20).grid(row=0, column=1, padx=10)

root.mainloop()
