import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from config import *
from text_preprocessing import PreprocessText

class Train:
    def __init__(self):
        pass
    def TrainTensorflow():
        article , labels = PreprocessText.PreProcessDataset()
        article_length = len(article)
        training_size = int(article_length * TRAINING_PORTION)
        train_article =  article[0:training_size]
        train_label = labels[0:training_size]
        valid_article = article[training_size:]
        valid_label = labels[training_size:]
        print(len(article),len(labels))
        tokenizer = Tokenizer(num_words=VOCAB_SIZE, oov_token=OOV_TOK)
        tokenizer.fit_on_texts(train_article)

        # For Training
        train_sequences = tokenizer.texts_to_sequences(train_article)
        train_padded = pad_sequences(train_sequences,
                                     maxlen=MAX_LENGTH,
                                     padding=PADDING_TYPE,
                                     truncating=TRUNC_TYPE)

        # For Validation
        validation_sequences = tokenizer.texts_to_sequences(valid_article)
        validation_padded = pad_sequences(validation_sequences,
                                          maxlen=MAX_LENGTH,
                                          padding=PADDING_TYPE,
                                          truncating=TRUNC_TYPE)

        # Labels tokenizer
        label_tokenizer = Tokenizer()
        label_tokenizer.fit_on_texts(labels)
        training_label_seq = np.array(label_tokenizer.texts_to_sequences(train_label))
        validation_label_seq = np.array(label_tokenizer.texts_to_sequences(valid_label))

        # model
        model = tf.keras.Sequential([
            tf.keras.layers.Embedding(VOCAB_SIZE, EMBEDDING_DIM),
            #tf.keras.layers.LSTM(64,return_sequences=True),
            #tf.keras.layers.Dropout(0.2),
            #tf.keras.layers.LSTM(128),
            tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64)),
            #tf.keras.layers.GRU(64),
            # tf.keras.layers.Dense(64),
            # tf.keras.layers.Dropout(0.2),

            tf.keras.layers.Dense(5, activation='softmax')
        ])

        print(model.summary())
        model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        history = model.fit(train_padded,
                            training_label_seq,
                            epochs=EPOCHS,
                            validation_data=(validation_padded, validation_label_seq),
                            verbose=1)
        model.save('news.h5')
        return history

