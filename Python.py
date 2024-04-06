import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

# Create the main application window
root = tk.Tk()
root.title("Ebook Reader")

# Create a notebook widget to manage tabs
notebook = ttk.Notebook(root)
notebook.pack(fill=tk.BOTH, expand=True)

# Function to open and display an ebook
def open_ebook():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as ebook_file:
            ebook_content = ebook_file.read()
            text_widget.delete(1.0, tk.END)
            text_widget.insert(tk.END, ebook_content)

# Create a tab for text files
text_tab = tk.Frame(notebook)
notebook.add(text_tab, text="Text Files")

# Create a text widget in the text tab with a white background
text_widget = tk.Text(text_tab, wrap=tk.WORD, bg="white")
text_widget.pack(fill=tk.BOTH, expand=True)

# Create an "Open" button in the text tab with a blue background
open_button = tk.Button(text_tab, text="Open Ebook", command=open_ebook, bg="blue", fg="white")
open_button.pack()

# Function to create a document file and save it
def create_document():
    document_content = text_widget.get(1.0, tk.END)
    document_path = filedialog.asksaveasfilename(defaultextension=".doc", filetypes=[("Document Files", "*.doc")])
    if document_path:
        with open(document_path, 'w', encoding='utf-8') as document_file:
            document_file.write(document_content)

            # Notify the user that the file has been saved
            tk.messagebox.showinfo("Saved", "Document saved successfully!")

# Create a tab for document creation
doc_tab = tk.Frame(notebook)
notebook.add(doc_tab, text="Create Document")

# Create a button to create a document from the displayed content with a green background
create_doc_button = tk.Button(doc_tab, text="Create Document", command=create_document, bg="green", fg="white")
create_doc_button.pack()

# Main loop
root.mainloop()
