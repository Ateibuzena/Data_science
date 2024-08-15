import base64
import re

def download_file(df, ep_number):

    ep_number = re.sub("[^A-Za-z0-9]+", "", ep_number)

    csv = df.to_csv(index = False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f"<a href='data:file/csv;base64,{b64}' download='{ep_number}.csv'>Download CSV File</a>"

    return href