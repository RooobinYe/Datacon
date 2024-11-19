import os

#数据目录，约定读取挂载数据的目录
data_path = "/datacon2024/AI"

#具体的文件目录
file_path=f"{data_path}/CQ1/Q.txt"


#输出答案的文件
result_path = "/result.txt"


# A(·)
def gen_Q_star(file_path, output_path='./result.txt'):
    """
    Generates a new file Q_star based on the content of the provided Q file.

    This function reads the content of the file specified by file_path, 
    processes it to generate a new file Q_star, and saves it to the location 
    specified by output_path.

    :param file_path: The path to the original Q file.
    :type file_path: str

    :param output_path: The path where the generated Q_star file will be saved.
    :type output_path: str

    :return: None
    """

    output_dir = os.path.dirname(output_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        with open(file_path, 'r', encoding='utf-8') as input_file, \
             open(output_path, 'a', encoding='utf-8') as output_file:
                
            # 逐行读取输入文件
                for q in input_file:
                    # induce hallucination for every query in Q.txt
                    q_star = q 
                    output_file.write(q_star.strip() + '\n')
                    
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print(f"File Q_star has been successfully generated at {output_path}")



if __name__ == "__main__": 

    gen_Q_star(file_path=file_path,
               output_path=result_path)





#A(.)
import nltk
from nltk.corpus import wordnet
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer

# 确保已经下载了NLTK的相关资源
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('averaged_perceptron_tagger')

def get_synonyms(word):
    """获取单词的同义词"""
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name().replace('_', ' ').lower())
    return list(synonyms)

def replace_with_synonyms(text, min_similarity=0.8):
    """用同义词替换文本中的单词"""
    lemmatizer = WordNetLemmatizer()
    words = word_tokenize(text)
    new_words = []
    for word in words:
        synonyms = get_synonyms(word)
        if synonyms:
            # 选择与原词最相似的同义词
            similar_synonyms = [syn for syn in synonyms if nltk.sentiment.vader.VADER().polarity_scores(syn)['compound'] >= min_similarity]
            if similar_synonyms:
                new_word = similar_synonyms[0]
            else:
                new_word = word
        else:
            new_word = word
        new_words.append(new_word)
    return ' '.join(new_words)

def insert_irrelevant_info(text, irrelevant_info):
    """在文本中插入无关信息"""
    sentences = sent_tokenize(text)
    new_sentences = []
    for i, sentence in enumerate(sentences):
        if i % 2 == 0:  # 每隔一句插入无关信息
            new_sentences.append(sentence)
            new_sentences.append(irrelevant_info)
        else:
            new_sentences.append(sentence)
    return ' '.join(new_sentences)

def generate_hallucination_trigger(text, irrelevant_info):
    """生成幻觉触发文本"""
    text = replace_with_synonyms(text)
    text = insert_irrelevant_info(text, irrelevant_info)
    return text

# 示例使用
original_text = "The quick brown fox jumps over the lazy dog."
irrelevant_info = "It was a sunny day at the park."
hallucination_trigger = generate_hallucination_trigger(original_text, irrelevant_info)
print("Original Text:", original_text)
print("Hallucination Trigger:", hallucination_trigger)
