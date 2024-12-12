import threading
import time


def write_words(word_count, file_name) :
    for i in range(1, word_count +1) :
            with open(file_name, 'a', encoding='utf-8') as file :
                    file.write(f'Какое то слово № {i}\n')
                    time.sleep(0.1)
    file.close()
    print(f'Заверщилась запись в файл {file_name}')

started_at1 = time.time()


write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

ended_at1 = time.time()

elapsed1 = round(ended_at1 - started_at1)
print(f'Время работы функций : {elapsed1} сек')

started_at2 = time.time()

thread1 = threading.Thread(target=write_words,args=(10, 'example5.txt'))
thread2 = threading.Thread(target=write_words,args=(30, 'example6.txt'))
thread3 = threading.Thread(target=write_words,args=(200, 'example7.txt'))
thread4 = threading.Thread(target=write_words,args=(100, 'example8.txt'))

thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

ended_at2 = time.time()
elapsed2 = round(ended_at2 - started_at2)
print(f'Время работы потоков : {elapsed2} сек')
