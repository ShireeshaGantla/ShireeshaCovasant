from pkg.file import File
import datetime

fs = File(".")
max_files = fs.getMaxSizeFile(1)
print(f"The two largest files are: {max_files}")
latest_files = fs.getLatestFiles(datetime.date(2025,3,1))
print(latest_files)
    
