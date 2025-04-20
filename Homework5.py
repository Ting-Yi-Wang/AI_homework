# ✅ STEP 1: 安裝需要的套件

!pip install -q sentence-transformers faiss-cpu requests
# ✅ STEP 2: 載入必要模組

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import requests
import pandas as pd
!gdown 1AF2g2WTtXQwb02S5EAD7aL48c9BkV1ed
# ✅ STEP 3: 準備你的語料

import pandas as pd # Make sure pandas is imported
docs_df = pd.read_csv("dcard-top100.csv")

documents = docs_df["content"].tolist()
docs_df
