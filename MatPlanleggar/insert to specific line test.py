import tkinter as tk

def insert_text():
    specific_line = 3  # The line number where you want to insert the text (starting from 1)
    text_to_insert = "This text was inserted into line 3."
    index = f"{specific_line}.0"
    text_widget.insert(index, text_to_insert)

# Create the main application window
root = tk.Tk()
root.geometry("300x200")

# Create a Text widget
text_widget = tk.Text(root, wrap="word")
text_widget.pack(expand=True, fill="both")

# Insert some initial text
text_widget.insert("end", "Line 1\nLine 2\nLine 3\nLine 4")

# Create a button to insert text into a specific line
insert_button = tk.Button(root, text="Insert Text", command=insert_text)
insert_button.pack()

# Start the main event loop
root.mainloop()