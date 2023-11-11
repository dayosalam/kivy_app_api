import tkinter as tk
from tkinter import filedialog
import requests
import json
from dd import InfaktAPIClient

class ApiDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("API Data Downloader")

        # self.label = tk.Label(root, text="Enter API URL:")
        # self.label.pack(pady=10)

        # self.api_url_entry = tk.Entry(root, width=50)
        # self.api_url_entry.pack(pady=10)

        self.download_button = tk.Button(root, text="Download Data", command=self.download_data)
        self.download_button.pack(pady=10)

    def download_data(self):
        api_key = "7834d6a3c32107f015127e06cd8c95f7c5b5b015"
        infakt_api_client = InfaktAPIClient(api_key)

        try:
                # Get data from the API
            api_response_data = infakt_api_client.get_clients_data()

            data = infakt_api_client.extract_data(api_response_data)


            file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
            df = infakt_api_client.create_dataframe(data)

        # Save the DataFrame to a CSV file
            infakt_api_client.save_to_csv(df, file_path)

            tk.messagebox.showinfo("Success", "Data downloaded successfully!")

        except requests.exceptions.RequestException as e:
            tk.messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ApiDownloaderApp(root)
    root.mainloop()
