import os
import datetime

class File:
    def __init__(self, directory):
        self.dir = directory

    def getMaxSizeFile(self, n=1):
        files = []
        for f in os.listdir(self.dir):
            filepath = os.path.join(self.dir, f)
            if os.path.isfile(filepath):
                files.append((f, os.path.getsize(filepath)))
        files.sort(key=lambda x: x[1], reverse=True)
        return [f[0] for f in files[:n]]
        
    def getLatestFiles(self, date):
        latest_files = []
        for f in os.listdir(self.dir):
            filepath = os.path.join(self.dir, f)
            if os.path.isfile(filepath):
                timestamp = os.path.getmtime(filepath)
                file_date = datetime.datetime.fromtimestamp(timestamp).date()
                if file_date >= date:
                    latest_files.append(f)
                       
        return latest_files
