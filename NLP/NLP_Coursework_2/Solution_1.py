import pandas as pd
import numpy as np
import re
import os
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


# Loading Dataset and converting in DataFrame
dt = pd.read_csv('dataset.csv', index_col = 0)
df=pd.DataFrame(dt)
print(df.head())
nltk.data.path.append(os.path.expanduser('~/nltk_data'))

# Download necessary NLTK resource
nltk.download('punkt',quiet=True)
nltk.download('stopwords',quiet=True)
nltk.download("wordnet",quiet=True)

TXT_COL= "sentence"
LABEL_COL = 'label'


# Text cleaning
def clean_text(text):
    if not isinstance(text,str):
        return ""

#     Lowercase
    text = text.lower()
    # Remove URLs
    text = re.sub(r"http\S+|www\S+", '',text)

    # Tokenize and clean
    tokens = re.findall(r'[a-z]+|\?',text)

    stop_words = set(stopwords.words('english'))
    question_words = {'what','why','how','when','where','who'}
    stop_words -= question_words

    lemmatizer = WordNetLemmatizer()
    cleaned_tokens = [lemmatizer.lemmatize(tokens) for token in tokens if not stop_words ]

    for token in tokens:
        if token != stop_words:
            if token != '?':
                cleaned_tokens.append(lemmatizer.lemmatize(token))
            else:
                cleaned_tokens.append(token)

    return " ".join(cleaned_tokens)

df['cleaned_text'] = df[TXT_COL].apply(clean_text)

df['target']= df[LABEL_COL].apply(lambda x:1 if 'question' in str(x).lower() else 0)

print(df[['cleaned_text','target']].head(2))


from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

x = df['cleaned_text']
y = df['target']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

print(f"training size: {len(x_train)}, testing size: {len(x_test)}")
print("First 5 rows of X_train:")
print(x_train.head())
print("\nAre there any empty strings?")
print(x_train[x_train == ""].count())

#
tfdif = TfidfVectorizer(max_features=5000,
                        ngram_range=(1,1),
                        min_df=1,
                        stop_words=None)
#
x_train_tfidf = tfdif.fit_transform(x_train)
x_test_tfidf = tfdif.transform(x_test)
#
print(f"TF-IDF matrix shape: {x_train_tfidf.shape}")


def load_glove(file_path):
    embedding_index = {}
    skipped = 0
    with open(file_path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f):
            try:
                values = line.split()
                if len(values) < 51:  # 1 word + 50 dimension
                    continue
                word = values[0]
                coefs = np.asarray(values[1:], dtype='float32')
                embedding_index[word] = coefs
            except (ValueError, IndexError) as e:
                skipped += 1
                if skipped <= 5:
                    print(f"Skipping line {line_num}: {e}")
        return embedding_index


glove_path = '/kaggle/input/models/mayankrajoriya2004/glove-2024-wikigiga/keras/default/1/wiki_giga_2024_50_MFT20_vectors_seed_123_alpha_0.75_eta_0.075_combined.txt'
glove_embeddings = load_glove(glove_path)


def sentence_to_glove(series, embeddings, dim=50):
    def vec_fn(s):
        words = str(s).lower().split()
        vectors = [embeddings[word] for word in words if word in embeddings]
        return np.mean(vectors, axis=0).astype(np.float32) if vectors else np.zeros(dim, dtype=np.float32)

    result = series.apply(vec_fn).values
    #

    return np.stack(result)


x_train_glove = sentence_to_glove(x_train, glove_embeddings)
x_test_glove = sentence_to_glove(x_test, glove_embeddings)

print(f"Glove semantic array shape: {x_train_glove.shape}")

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt

print("Training Logistic Regression......")
lr_model = LogisticRegression(
    max_iter=1000,
    random_state=42
)
lr_model.fit(x_train_tfidf,y_train)

y_pred_lr = lr_model.predict_proba(x_test_tfidf)[:,1]
fpr_lr,tpr_lr,_ = roc_curve(
    y_test,
    y_pred_lr)

auc_lr = auc(fpr_lr,tpr_lr)
print(f"Lr AUC: {auc_lr:.4f}")


print("Training Random Forest classifier......")
rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)
rf_model.fit(x_train_tfidf,y_train)

y_pred_rf = rf_model.predict_proba(x_test_tfidf)[:,1]
fpr_rf,tpr_rf,_ = roc_curve(
    y_test,
    y_pred_rf)

auc_rf = auc(fpr_rf,tpr_rf)
print(f"Lr AUC: {auc_rf:.4f}")