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
