import os
from pathlib import Path

DIRECTORIES = { "IMAGES": [".jpeg", ",jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
                           ".heif", ".psd"],
                "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
			   ".qt", ".mpg", ".mpeg", ".3gp"],
                "DOCUMENTS": [".docx", ".doc", ".rtf", ".wpd", ".xps", ".xls", ".xlsx",
                              ".ppt", ".pptx", ".txt"],
                "AUDIO": [".aac", ".aa", ".dvf", ".m4a", ".dvf", ".mp3", ".m4p", ".wav",
                          ".wma", ".msv"],
                "PDF": [".pdf"],
                "PYTHON": [".py", ".ipynb"],
                "EXE": [".exe"]}

FILE_FORMATS = {file_format: directory
				for directory, file_formats in DIRECTORIES.items()
				for file_format in file_formats}

def organize_junk():
	for entry in os.scandir():
		if entry.is_dir():
			continue
		file_path = Path(entry)
		file_format = file_path.suffix.lower()
		if file_format in FILE_FORMATS:
			directory_path = Path(FILE_FORMATS[file_format])
			directory_path.mkdir(exist_ok=True)
			file_path.rename(directory_path.joinpath(file_path))

		for dir in os.scandir():
			try:
				os.rmdir(dir)
			except:
				pass

if __name__ == "__main__":
	organize_junk()
