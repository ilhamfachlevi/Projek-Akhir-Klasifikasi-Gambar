{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPfuLiSzYtXmhh8Kr6rh2k7",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ilhamfachlevi/Projek-Akhir-Klasifikasi-Gambar/blob/main/Muhammad_Ilham_Fachlevi_Dicoding_Klasifikasi_Gambar.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "mTz1trPHMxCY"
      },
      "outputs": [],
      "source": [
        "import tensorflow as tf"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(tf.__version__)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "k8yAGjgmMrKC",
        "outputId": "f94b56bd-16a4-43c4-9f06-2366c86065a7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2.8.2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!wget --no-check-certificate \\\n",
        "  https://github.com/dicodingacademy/assets/releases/download/release/rockpaperscissors.zip \\\n",
        "  -O /tmp/rockpaperscissors.zip"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nZJ0u9zANMFG",
        "outputId": "ad9fdaa3-9b45-4c03-b6b9-e2939920dd7d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "--2022-09-02 13:48:36--  https://github.com/dicodingacademy/assets/releases/download/release/rockpaperscissors.zip\n",
            "Resolving github.com (github.com)... 140.82.114.3\n",
            "Connecting to github.com (github.com)|140.82.114.3|:443... connected.\n",
            "HTTP request sent, awaiting response... 302 Found\n",
            "Location: https://objects.githubusercontent.com/github-production-release-asset-2e65be/391417272/7eb836f2-695b-4a46-9c78-b65867166957?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20220902%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220902T134836Z&X-Amz-Expires=300&X-Amz-Signature=14dea959815dcdc5729dcb799a75960ea04f01ea930f663e9d84a3f7523e2f3d&X-Amz-SignedHeaders=host&actor_id=0&key_id=0&repo_id=391417272&response-content-disposition=attachment%3B%20filename%3Drockpaperscissors.zip&response-content-type=application%2Foctet-stream [following]\n",
            "--2022-09-02 13:48:36--  https://objects.githubusercontent.com/github-production-release-asset-2e65be/391417272/7eb836f2-695b-4a46-9c78-b65867166957?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20220902%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220902T134836Z&X-Amz-Expires=300&X-Amz-Signature=14dea959815dcdc5729dcb799a75960ea04f01ea930f663e9d84a3f7523e2f3d&X-Amz-SignedHeaders=host&actor_id=0&key_id=0&repo_id=391417272&response-content-disposition=attachment%3B%20filename%3Drockpaperscissors.zip&response-content-type=application%2Foctet-stream\n",
            "Resolving objects.githubusercontent.com (objects.githubusercontent.com)... 185.199.109.133, 185.199.108.133, 185.199.110.133, ...\n",
            "Connecting to objects.githubusercontent.com (objects.githubusercontent.com)|185.199.109.133|:443... connected.\n",
            "HTTP request sent, awaiting response... 200 OK\n",
            "Length: 322873683 (308M) [application/octet-stream]\n",
            "Saving to: ‘/tmp/rockpaperscissors.zip’\n",
            "\n",
            "/tmp/rockpapersciss 100%[===================>] 307.92M   133MB/s    in 2.3s    \n",
            "\n",
            "2022-09-02 13:48:38 (133 MB/s) - ‘/tmp/rockpaperscissors.zip’ saved [322873683/322873683]\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# melakukan ekstraksi pada file zip\n",
        "import zipfile, os\n",
        "local_zip = '/tmp/rockpaperscissors.zip'\n",
        "zip_ref = zipfile.ZipFile(local_zip,'r')\n",
        "zip_ref.extractall('/tmp')\n",
        "zip_ref.close()\n",
        "\n",
        "# membuat nama direktori\n",
        "base_dir = '/tmp/rockpaperscissors'\n",
        "train_dir = os.path.join(base_dir,'train')\n",
        "validation_dir = os.path.join(base_dir,'valid')"
      ],
      "metadata": {
        "id": "S9vvSaw8NVGk"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# membuat direktori train dan validation\n",
        "os.mkdir(train_dir)\n",
        "os.mkdir(validation_dir)"
      ],
      "metadata": {
        "id": "BfS8M-RgNjgB"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "os.listdir('/tmp/rockpaperscissors')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PfD3EgucNnb3",
        "outputId": "fcb6db6b-0729-4289-e9ea-1ac88a08f897"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['paper',\n",
              " 'valid',\n",
              " 'rps-cv-images',\n",
              " 'scissors',\n",
              " 'README_rpc-cv-images.txt',\n",
              " 'train',\n",
              " 'rock']"
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# mengetahui banyaknya berkas gambar pada folder\n",
        "print(len(os.listdir('/tmp/rockpaperscissors/rock')))\n",
        "print(len(os.listdir('/tmp/rockpaperscissors/paper')))\n",
        "print(len(os.listdir('/tmp/rockpaperscissors/scissors')))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vBV8Q_utNpBI",
        "outputId": "5e52a8d5-6c6b-4324-af01-052f5c048ed5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "726\n",
            "712\n",
            "750\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# menentukan lokasi path direktori\n",
        "rock_dir = os.path.join(base_dir,'rock')\n",
        "paper_dir = os.path.join(base_dir,'paper')\n",
        "scissors_dir = os.path.join(base_dir,'scissors')"
      ],
      "metadata": {
        "id": "Rk6-QrtCNsrn"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.model_selection import train_test_split\n",
        "# membagi direktori masing-masing kelas data dengan train_test_split (validation set 40% = 0.4)\n",
        "train_rock_dir, valid_rock_dir = train_test_split(os.listdir(rock_dir), test_size=0.4)\n",
        "train_paper_dir, valid_paper_dir = train_test_split(os.listdir(paper_dir), test_size=0.4)\n",
        "train_scissors_dir, valid_scissors_dir = train_test_split(os.listdir(scissors_dir), test_size=0.4)"
      ],
      "metadata": {
        "id": "RuMyWEfMNxgv"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# menentukan direktori training dan validation \n",
        "train_rock = os.path.join(train_dir,'rock')\n",
        "train_paper = os.path.join(train_dir,'paper')\n",
        "train_scissors = os.path.join(train_dir,'scissors')\n",
        "valid_rock = os.path.join(validation_dir,'rock')\n",
        "valid_paper = os.path.join(validation_dir,'paper')\n",
        "valid_scissors = os.path.join(validation_dir,'scissors')"
      ],
      "metadata": {
        "id": "uapO8v5lOH0Q"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# membuat direktori baru di dalam direktori train\n",
        "if not os.path.exists(train_rock):\n",
        "  os.mkdir(train_rock)\n",
        "if not os.path.exists(train_paper):\n",
        "  os.mkdir(train_paper)\n",
        "if not os.path.exists(train_scissors):\n",
        "  os.mkdir(train_scissors)\n",
        "\n",
        "# membuat direktori baru di dalam direktori validation\n",
        "if not os.path.exists(valid_rock):\n",
        "  os.mkdir(valid_rock)\n",
        "if not os.path.exists(valid_paper):\n",
        "  os.mkdir(valid_paper)\n",
        "if not os.path.exists(valid_scissors):\n",
        "  os.mkdir(valid_scissors)"
      ],
      "metadata": {
        "id": "Ff2Xiw7cN2et"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import shutil\n",
        "# membuat salinan data train ke direktori baru\n",
        "for i in train_rock_dir:\n",
        "  shutil.copy(os.path.join(rock_dir, i), os.path.join(train_rock, i))\n",
        "for i in train_paper_dir:\n",
        "  shutil.copy(os.path.join(paper_dir,i), os.path.join(train_paper,i))\n",
        "for i in train_scissors_dir:\n",
        "  shutil.copy(os.path.join(scissors_dir,i), os.path.join(train_scissors,i))\n",
        "\n",
        "# membuat salinan data validation ke direktori baru\n",
        "for i in valid_rock_dir:\n",
        "  shutil.copy(os.path.join(rock_dir, i), os.path.join(valid_rock,i))\n",
        "for i in valid_paper_dir:\n",
        "  shutil.copy(os.path.join(paper_dir,i), os.path.join(valid_paper,i))\n",
        "for i in valid_scissors_dir:\n",
        "  shutil.copy(os.path.join(scissors_dir,i), os.path.join(valid_scissors,i))"
      ],
      "metadata": {
        "id": "_moP46IfOKgD"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(len(os.listdir('/tmp/rockpaperscissors/train/rock')))\n",
        "print(len(os.listdir('/tmp/rockpaperscissors/valid/rock')))\n",
        "print(len(os.listdir('/tmp/rockpaperscissors/train/scissors')))\n",
        "print(len(os.listdir('/tmp/rockpaperscissors/valid/scissors')))\n",
        "print(len(os.listdir('/tmp/rockpaperscissors/train/paper')))\n",
        "print(len(os.listdir('/tmp/rockpaperscissors/valid/paper')))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "W-5OHfCrONeb",
        "outputId": "d00f658d-7ca5-4bc9-af73-a047269a6042"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "435\n",
            "291\n",
            "450\n",
            "300\n",
            "427\n",
            "285\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from tensorflow.keras.preprocessing.image import ImageDataGenerator\n",
        "train_datagen = ImageDataGenerator(\n",
        "    rescale = 1./225,\n",
        "    rotation_range = 20,\n",
        "    horizontal_flip = True,\n",
        "    shear_range = 0.2,\n",
        "    fill_mode = 'nearest')\n",
        "\n",
        "test_datagen = ImageDataGenerator(\n",
        "    rescale = 1./225,\n",
        "    rotation_range = 20,\n",
        "    horizontal_flip = True,\n",
        "    shear_range = 0.2,\n",
        "    fill_mode = 'nearest')"
      ],
      "metadata": {
        "id": "U4w3qAl5O369"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "train_generator = train_datagen.flow_from_directory(\n",
        "    train_dir, # direktori data latih\n",
        "    target_size =(150,150), # mengubah resolusi seluruh gambar menjadi 150x150 piksel\n",
        "    batch_size = 32, \n",
        "    class_mode = 'categorical' # merupakan masalah klasifikasi multi kelas maka menggunakan class_mode = 'categorical'\n",
        ")\n",
        "\n",
        "validation_generator = test_datagen.flow_from_directory(\n",
        "    validation_dir, # direktori data latih\n",
        "    target_size = (150,150), # mengubah resolusi seluruh gambar menjadi 150x150 piksel\n",
        "    batch_size = 32,\n",
        "    class_mode = 'categorical' # merupakan masalah klasifikasi multi kelas maka menggunakan class_mode = 'categorical'\n",
        ")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PHE95B9OO6OP",
        "outputId": "c6f26b52-9bf2-4b09-e029-b99b4569cf53"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Found 1312 images belonging to 3 classes.\n",
            "Found 876 images belonging to 3 classes.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "class myCallback(tf.keras.callbacks.Callback):\n",
        "  def on_epoch_end(self, epoch, logs={}):\n",
        "    if (logs.get('loss') < 0.1):\n",
        "      print()     \n",
        "      self.model.stop_training = True\n",
        "\n",
        "callbacks = myCallback()"
      ],
      "metadata": {
        "id": "5PtesYWwXtq0"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model = tf.keras.models.Sequential([\n",
        "  tf.keras.layers.Conv2D(32, (3,3), padding='same', activation = 'relu', input_shape= (150,150,3)),\n",
        "  tf.keras.layers.MaxPooling2D(2,2),\n",
        "  tf.keras.layers.Conv2D(64,(3,3), padding='same', activation= 'relu'),\n",
        "  tf.keras.layers.MaxPooling2D(2,2),\n",
        "  tf.keras.layers.Conv2D(128,(3,3), padding='same', activation= 'relu'),\n",
        "  tf.keras.layers.MaxPooling2D(2,2),\n",
        "  tf.keras.layers.Conv2D(256,(3,3), padding='same', activation= 'relu'),\n",
        "  tf.keras.layers.MaxPooling2D(2,2),\n",
        "  tf.keras.layers.Flatten(),\n",
        "  tf.keras.layers.Dropout(0.5),\n",
        "  tf.keras.layers.Dense(512, activation= 'relu'),\n",
        "  tf.keras.layers.Dense(3, activation= 'softmax')\n",
        "])\n",
        "model.summary()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gOGH8Z7NO_A1",
        "outputId": "1cdd50a7-fc29-49ce-9b50-03cbb60510a4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Model: \"sequential_2\"\n",
            "_________________________________________________________________\n",
            " Layer (type)                Output Shape              Param #   \n",
            "=================================================================\n",
            " conv2d_8 (Conv2D)           (None, 150, 150, 32)      896       \n",
            "                                                                 \n",
            " max_pooling2d_8 (MaxPooling  (None, 75, 75, 32)       0         \n",
            " 2D)                                                             \n",
            "                                                                 \n",
            " conv2d_9 (Conv2D)           (None, 75, 75, 64)        18496     \n",
            "                                                                 \n",
            " max_pooling2d_9 (MaxPooling  (None, 37, 37, 64)       0         \n",
            " 2D)                                                             \n",
            "                                                                 \n",
            " conv2d_10 (Conv2D)          (None, 37, 37, 128)       73856     \n",
            "                                                                 \n",
            " max_pooling2d_10 (MaxPoolin  (None, 18, 18, 128)      0         \n",
            " g2D)                                                            \n",
            "                                                                 \n",
            " conv2d_11 (Conv2D)          (None, 18, 18, 256)       295168    \n",
            "                                                                 \n",
            " max_pooling2d_11 (MaxPoolin  (None, 9, 9, 256)        0         \n",
            " g2D)                                                            \n",
            "                                                                 \n",
            " flatten_2 (Flatten)         (None, 20736)             0         \n",
            "                                                                 \n",
            " dropout_2 (Dropout)         (None, 20736)             0         \n",
            "                                                                 \n",
            " dense_4 (Dense)             (None, 512)               10617344  \n",
            "                                                                 \n",
            " dense_5 (Dense)             (None, 3)                 1539      \n",
            "                                                                 \n",
            "=================================================================\n",
            "Total params: 11,007,299\n",
            "Trainable params: 11,007,299\n",
            "Non-trainable params: 0\n",
            "_________________________________________________________________\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from tensorflow.keras.optimizers import RMSprop\n",
        "# compile model dengan 'adam' optimizer loss function 'categorical_crossentropy' \n",
        "model.compile(loss = 'categorical_crossentropy',\n",
        "              optimizer = tf.optimizers.Adam(),\n",
        "              metrics=['accuracy'])\n"
      ],
      "metadata": {
        "id": "1dk4F_4lSK9B"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "history = model.fit(\n",
        "    train_generator,\n",
        "    steps_per_epoch = 25, # berapa batch yang akan dieksekusi pada setiap epoch\n",
        "    epochs = 20,\n",
        "    validation_data = validation_generator, # menampilkan akurasi pengujian data validasi\n",
        "    validation_steps = 5, # berapa batch yang akan dieksekusi pada setiap epoch\n",
        "    verbose =2,\n",
        "    callbacks=[callbacks]\n",
        ")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fHpfRyEFPCGA",
        "outputId": "099786ba-21a4-41b1-c9ee-260405e53780"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Epoch 1/20\n",
            "25/25 - 35s - loss: 1.1571 - accuracy: 0.3913 - val_loss: 1.0259 - val_accuracy: 0.4812 - 35s/epoch - 1s/step\n",
            "Epoch 2/20\n",
            "25/25 - 32s - loss: 0.8732 - accuracy: 0.6050 - val_loss: 0.8184 - val_accuracy: 0.6313 - 32s/epoch - 1s/step\n",
            "Epoch 3/20\n",
            "25/25 - 32s - loss: 0.6372 - accuracy: 0.7475 - val_loss: 0.3825 - val_accuracy: 0.8500 - 32s/epoch - 1s/step\n",
            "Epoch 4/20\n",
            "25/25 - 32s - loss: 0.3712 - accuracy: 0.8587 - val_loss: 0.2488 - val_accuracy: 0.9062 - 32s/epoch - 1s/step\n",
            "Epoch 5/20\n",
            "25/25 - 33s - loss: 0.2246 - accuracy: 0.9175 - val_loss: 0.2129 - val_accuracy: 0.9375 - 33s/epoch - 1s/step\n",
            "Epoch 6/20\n",
            "25/25 - 32s - loss: 0.2543 - accuracy: 0.9038 - val_loss: 0.2045 - val_accuracy: 0.9187 - 32s/epoch - 1s/step\n",
            "Epoch 7/20\n",
            "25/25 - 32s - loss: 0.2290 - accuracy: 0.9212 - val_loss: 0.2565 - val_accuracy: 0.9062 - 32s/epoch - 1s/step\n",
            "Epoch 8/20\n",
            "25/25 - 32s - loss: 0.2380 - accuracy: 0.9200 - val_loss: 0.2056 - val_accuracy: 0.9438 - 32s/epoch - 1s/step\n",
            "Epoch 9/20\n",
            "25/25 - 33s - loss: 0.2124 - accuracy: 0.9250 - val_loss: 0.1897 - val_accuracy: 0.9312 - 33s/epoch - 1s/step\n",
            "Epoch 10/20\n",
            "25/25 - 32s - loss: 0.1719 - accuracy: 0.9350 - val_loss: 0.1217 - val_accuracy: 0.9750 - 32s/epoch - 1s/step\n",
            "Epoch 11/20\n",
            "25/25 - 32s - loss: 0.1431 - accuracy: 0.9563 - val_loss: 0.1534 - val_accuracy: 0.9625 - 32s/epoch - 1s/step\n",
            "Epoch 12/20\n",
            "25/25 - 33s - loss: 0.1346 - accuracy: 0.9550 - val_loss: 0.0567 - val_accuracy: 0.9937 - 33s/epoch - 1s/step\n",
            "Epoch 13/20\n",
            "25/25 - 32s - loss: 0.1470 - accuracy: 0.9500 - val_loss: 0.1208 - val_accuracy: 0.9438 - 32s/epoch - 1s/step\n",
            "Epoch 14/20\n",
            "25/25 - 32s - loss: 0.1063 - accuracy: 0.9613 - val_loss: 0.0682 - val_accuracy: 0.9688 - 32s/epoch - 1s/step\n",
            "Epoch 15/20\n",
            "\n",
            "25/25 - 32s - loss: 0.0832 - accuracy: 0.9787 - val_loss: 0.1619 - val_accuracy: 0.9625 - 32s/epoch - 1s/step\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "from google.colab import files\n",
        "from tensorflow.keras.preprocessing import image\n",
        "import matplotlib.pyplot as plt\n",
        "import matplotlib.image as mpimg\n",
        "import matplotlib.pyplot as plt\n",
        "import matplotlib.image as mpimg\n",
        "%matplotlib inline\n",
        "\n",
        "uploaded = files.upload()\n",
        "\n",
        "for fn in uploaded.keys():\n",
        " \n",
        "  # predicting images\n",
        "  path = fn\n",
        "  img = image.load_img(path, target_size=(150,150))\n",
        "\n",
        "  imgplot = plt.imshow(img)\n",
        "  x = image.img_to_array(img)\n",
        "  x = np.expand_dims(x, axis=0)\n",
        "  images = np.vstack([x])\n",
        "\n",
        "  classes = model.predict(images, batch_size=10)  \n",
        "\n",
        "  print(fn)\n",
        "  if classes[0,0]!=0:\n",
        "    print('paper')\n",
        "  elif classes[0,1]!=0:\n",
        "    print('rock')\n",
        "  else:\n",
        "    print('scissors')"
      ],
      "metadata": {
        "colab": {
          "resources": {
            "http://localhost:8080/nbextensions/google.colab/files.js": {
              "data": "Ly8gQ29weXJpZ2h0IDIwMTcgR29vZ2xlIExMQwovLwovLyBMaWNlbnNlZCB1bmRlciB0aGUgQXBhY2hlIExpY2Vuc2UsIFZlcnNpb24gMi4wICh0aGUgIkxpY2Vuc2UiKTsKLy8geW91IG1heSBub3QgdXNlIHRoaXMgZmlsZSBleGNlcHQgaW4gY29tcGxpYW5jZSB3aXRoIHRoZSBMaWNlbnNlLgovLyBZb3UgbWF5IG9idGFpbiBhIGNvcHkgb2YgdGhlIExpY2Vuc2UgYXQKLy8KLy8gICAgICBodHRwOi8vd3d3LmFwYWNoZS5vcmcvbGljZW5zZXMvTElDRU5TRS0yLjAKLy8KLy8gVW5sZXNzIHJlcXVpcmVkIGJ5IGFwcGxpY2FibGUgbGF3IG9yIGFncmVlZCB0byBpbiB3cml0aW5nLCBzb2Z0d2FyZQovLyBkaXN0cmlidXRlZCB1bmRlciB0aGUgTGljZW5zZSBpcyBkaXN0cmlidXRlZCBvbiBhbiAiQVMgSVMiIEJBU0lTLAovLyBXSVRIT1VUIFdBUlJBTlRJRVMgT1IgQ09ORElUSU9OUyBPRiBBTlkgS0lORCwgZWl0aGVyIGV4cHJlc3Mgb3IgaW1wbGllZC4KLy8gU2VlIHRoZSBMaWNlbnNlIGZvciB0aGUgc3BlY2lmaWMgbGFuZ3VhZ2UgZ292ZXJuaW5nIHBlcm1pc3Npb25zIGFuZAovLyBsaW1pdGF0aW9ucyB1bmRlciB0aGUgTGljZW5zZS4KCi8qKgogKiBAZmlsZW92ZXJ2aWV3IEhlbHBlcnMgZm9yIGdvb2dsZS5jb2xhYiBQeXRob24gbW9kdWxlLgogKi8KKGZ1bmN0aW9uKHNjb3BlKSB7CmZ1bmN0aW9uIHNwYW4odGV4dCwgc3R5bGVBdHRyaWJ1dGVzID0ge30pIHsKICBjb25zdCBlbGVtZW50ID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgnc3BhbicpOwogIGVsZW1lbnQudGV4dENvbnRlbnQgPSB0ZXh0OwogIGZvciAoY29uc3Qga2V5IG9mIE9iamVjdC5rZXlzKHN0eWxlQXR0cmlidXRlcykpIHsKICAgIGVsZW1lbnQuc3R5bGVba2V5XSA9IHN0eWxlQXR0cmlidXRlc1trZXldOwogIH0KICByZXR1cm4gZWxlbWVudDsKfQoKLy8gTWF4IG51bWJlciBvZiBieXRlcyB3aGljaCB3aWxsIGJlIHVwbG9hZGVkIGF0IGEgdGltZS4KY29uc3QgTUFYX1BBWUxPQURfU0laRSA9IDEwMCAqIDEwMjQ7CgpmdW5jdGlvbiBfdXBsb2FkRmlsZXMoaW5wdXRJZCwgb3V0cHV0SWQpIHsKICBjb25zdCBzdGVwcyA9IHVwbG9hZEZpbGVzU3RlcChpbnB1dElkLCBvdXRwdXRJZCk7CiAgY29uc3Qgb3V0cHV0RWxlbWVudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKG91dHB1dElkKTsKICAvLyBDYWNoZSBzdGVwcyBvbiB0aGUgb3V0cHV0RWxlbWVudCB0byBtYWtlIGl0IGF2YWlsYWJsZSBmb3IgdGhlIG5leHQgY2FsbAogIC8vIHRvIHVwbG9hZEZpbGVzQ29udGludWUgZnJvbSBQeXRob24uCiAgb3V0cHV0RWxlbWVudC5zdGVwcyA9IHN0ZXBzOwoKICByZXR1cm4gX3VwbG9hZEZpbGVzQ29udGludWUob3V0cHV0SWQpOwp9CgovLyBUaGlzIGlzIHJvdWdobHkgYW4gYXN5bmMgZ2VuZXJhdG9yIChub3Qgc3VwcG9ydGVkIGluIHRoZSBicm93c2VyIHlldCksCi8vIHdoZXJlIHRoZXJlIGFyZSBtdWx0aXBsZSBhc3luY2hyb25vdXMgc3RlcHMgYW5kIHRoZSBQeXRob24gc2lkZSBpcyBnb2luZwovLyB0byBwb2xsIGZvciBjb21wbGV0aW9uIG9mIGVhY2ggc3RlcC4KLy8gVGhpcyB1c2VzIGEgUHJvbWlzZSB0byBibG9jayB0aGUgcHl0aG9uIHNpZGUgb24gY29tcGxldGlvbiBvZiBlYWNoIHN0ZXAsCi8vIHRoZW4gcGFzc2VzIHRoZSByZXN1bHQgb2YgdGhlIHByZXZpb3VzIHN0ZXAgYXMgdGhlIGlucHV0IHRvIHRoZSBuZXh0IHN0ZXAuCmZ1bmN0aW9uIF91cGxvYWRGaWxlc0NvbnRpbnVlKG91dHB1dElkKSB7CiAgY29uc3Qgb3V0cHV0RWxlbWVudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKG91dHB1dElkKTsKICBjb25zdCBzdGVwcyA9IG91dHB1dEVsZW1lbnQuc3RlcHM7CgogIGNvbnN0IG5leHQgPSBzdGVwcy5uZXh0KG91dHB1dEVsZW1lbnQubGFzdFByb21pc2VWYWx1ZSk7CiAgcmV0dXJuIFByb21pc2UucmVzb2x2ZShuZXh0LnZhbHVlLnByb21pc2UpLnRoZW4oKHZhbHVlKSA9PiB7CiAgICAvLyBDYWNoZSB0aGUgbGFzdCBwcm9taXNlIHZhbHVlIHRvIG1ha2UgaXQgYXZhaWxhYmxlIHRvIHRoZSBuZXh0CiAgICAvLyBzdGVwIG9mIHRoZSBnZW5lcmF0b3IuCiAgICBvdXRwdXRFbGVtZW50Lmxhc3RQcm9taXNlVmFsdWUgPSB2YWx1ZTsKICAgIHJldHVybiBuZXh0LnZhbHVlLnJlc3BvbnNlOwogIH0pOwp9CgovKioKICogR2VuZXJhdG9yIGZ1bmN0aW9uIHdoaWNoIGlzIGNhbGxlZCBiZXR3ZWVuIGVhY2ggYXN5bmMgc3RlcCBvZiB0aGUgdXBsb2FkCiAqIHByb2Nlc3MuCiAqIEBwYXJhbSB7c3RyaW5nfSBpbnB1dElkIEVsZW1lbnQgSUQgb2YgdGhlIGlucHV0IGZpbGUgcGlja2VyIGVsZW1lbnQuCiAqIEBwYXJhbSB7c3RyaW5nfSBvdXRwdXRJZCBFbGVtZW50IElEIG9mIHRoZSBvdXRwdXQgZGlzcGxheS4KICogQHJldHVybiB7IUl0ZXJhYmxlPCFPYmplY3Q+fSBJdGVyYWJsZSBvZiBuZXh0IHN0ZXBzLgogKi8KZnVuY3Rpb24qIHVwbG9hZEZpbGVzU3RlcChpbnB1dElkLCBvdXRwdXRJZCkgewogIGNvbnN0IGlucHV0RWxlbWVudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKGlucHV0SWQpOwogIGlucHV0RWxlbWVudC5kaXNhYmxlZCA9IGZhbHNlOwoKICBjb25zdCBvdXRwdXRFbGVtZW50ID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQob3V0cHV0SWQpOwogIG91dHB1dEVsZW1lbnQuaW5uZXJIVE1MID0gJyc7CgogIGNvbnN0IHBpY2tlZFByb21pc2UgPSBuZXcgUHJvbWlzZSgocmVzb2x2ZSkgPT4gewogICAgaW5wdXRFbGVtZW50LmFkZEV2ZW50TGlzdGVuZXIoJ2NoYW5nZScsIChlKSA9PiB7CiAgICAgIHJlc29sdmUoZS50YXJnZXQuZmlsZXMpOwogICAgfSk7CiAgfSk7CgogIGNvbnN0IGNhbmNlbCA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ2J1dHRvbicpOwogIGlucHV0RWxlbWVudC5wYXJlbnRFbGVtZW50LmFwcGVuZENoaWxkKGNhbmNlbCk7CiAgY2FuY2VsLnRleHRDb250ZW50ID0gJ0NhbmNlbCB1cGxvYWQnOwogIGNvbnN0IGNhbmNlbFByb21pc2UgPSBuZXcgUHJvbWlzZSgocmVzb2x2ZSkgPT4gewogICAgY2FuY2VsLm9uY2xpY2sgPSAoKSA9PiB7CiAgICAgIHJlc29sdmUobnVsbCk7CiAgICB9OwogIH0pOwoKICAvLyBXYWl0IGZvciB0aGUgdXNlciB0byBwaWNrIHRoZSBmaWxlcy4KICBjb25zdCBmaWxlcyA9IHlpZWxkIHsKICAgIHByb21pc2U6IFByb21pc2UucmFjZShbcGlja2VkUHJvbWlzZSwgY2FuY2VsUHJvbWlzZV0pLAogICAgcmVzcG9uc2U6IHsKICAgICAgYWN0aW9uOiAnc3RhcnRpbmcnLAogICAgfQogIH07CgogIGNhbmNlbC5yZW1vdmUoKTsKCiAgLy8gRGlzYWJsZSB0aGUgaW5wdXQgZWxlbWVudCBzaW5jZSBmdXJ0aGVyIHBpY2tzIGFyZSBub3QgYWxsb3dlZC4KICBpbnB1dEVsZW1lbnQuZGlzYWJsZWQgPSB0cnVlOwoKICBpZiAoIWZpbGVzKSB7CiAgICByZXR1cm4gewogICAgICByZXNwb25zZTogewogICAgICAgIGFjdGlvbjogJ2NvbXBsZXRlJywKICAgICAgfQogICAgfTsKICB9CgogIGZvciAoY29uc3QgZmlsZSBvZiBmaWxlcykgewogICAgY29uc3QgbGkgPSBkb2N1bWVudC5jcmVhdGVFbGVtZW50KCdsaScpOwogICAgbGkuYXBwZW5kKHNwYW4oZmlsZS5uYW1lLCB7Zm9udFdlaWdodDogJ2JvbGQnfSkpOwogICAgbGkuYXBwZW5kKHNwYW4oCiAgICAgICAgYCgke2ZpbGUudHlwZSB8fCAnbi9hJ30pIC0gJHtmaWxlLnNpemV9IGJ5dGVzLCBgICsKICAgICAgICBgbGFzdCBtb2RpZmllZDogJHsKICAgICAgICAgICAgZmlsZS5sYXN0TW9kaWZpZWREYXRlID8gZmlsZS5sYXN0TW9kaWZpZWREYXRlLnRvTG9jYWxlRGF0ZVN0cmluZygpIDoKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgJ24vYSd9IC0gYCkpOwogICAgY29uc3QgcGVyY2VudCA9IHNwYW4oJzAlIGRvbmUnKTsKICAgIGxpLmFwcGVuZENoaWxkKHBlcmNlbnQpOwoKICAgIG91dHB1dEVsZW1lbnQuYXBwZW5kQ2hpbGQobGkpOwoKICAgIGNvbnN0IGZpbGVEYXRhUHJvbWlzZSA9IG5ldyBQcm9taXNlKChyZXNvbHZlKSA9PiB7CiAgICAgIGNvbnN0IHJlYWRlciA9IG5ldyBGaWxlUmVhZGVyKCk7CiAgICAgIHJlYWRlci5vbmxvYWQgPSAoZSkgPT4gewogICAgICAgIHJlc29sdmUoZS50YXJnZXQucmVzdWx0KTsKICAgICAgfTsKICAgICAgcmVhZGVyLnJlYWRBc0FycmF5QnVmZmVyKGZpbGUpOwogICAgfSk7CiAgICAvLyBXYWl0IGZvciB0aGUgZGF0YSB0byBiZSByZWFkeS4KICAgIGxldCBmaWxlRGF0YSA9IHlpZWxkIHsKICAgICAgcHJvbWlzZTogZmlsZURhdGFQcm9taXNlLAogICAgICByZXNwb25zZTogewogICAgICAgIGFjdGlvbjogJ2NvbnRpbnVlJywKICAgICAgfQogICAgfTsKCiAgICAvLyBVc2UgYSBjaHVua2VkIHNlbmRpbmcgdG8gYXZvaWQgbWVzc2FnZSBzaXplIGxpbWl0cy4gU2VlIGIvNjIxMTU2NjAuCiAgICBsZXQgcG9zaXRpb24gPSAwOwogICAgZG8gewogICAgICBjb25zdCBsZW5ndGggPSBNYXRoLm1pbihmaWxlRGF0YS5ieXRlTGVuZ3RoIC0gcG9zaXRpb24sIE1BWF9QQVlMT0FEX1NJWkUpOwogICAgICBjb25zdCBjaHVuayA9IG5ldyBVaW50OEFycmF5KGZpbGVEYXRhLCBwb3NpdGlvbiwgbGVuZ3RoKTsKICAgICAgcG9zaXRpb24gKz0gbGVuZ3RoOwoKICAgICAgY29uc3QgYmFzZTY0ID0gYnRvYShTdHJpbmcuZnJvbUNoYXJDb2RlLmFwcGx5KG51bGwsIGNodW5rKSk7CiAgICAgIHlpZWxkIHsKICAgICAgICByZXNwb25zZTogewogICAgICAgICAgYWN0aW9uOiAnYXBwZW5kJywKICAgICAgICAgIGZpbGU6IGZpbGUubmFtZSwKICAgICAgICAgIGRhdGE6IGJhc2U2NCwKICAgICAgICB9LAogICAgICB9OwoKICAgICAgbGV0IHBlcmNlbnREb25lID0gZmlsZURhdGEuYnl0ZUxlbmd0aCA9PT0gMCA/CiAgICAgICAgICAxMDAgOgogICAgICAgICAgTWF0aC5yb3VuZCgocG9zaXRpb24gLyBmaWxlRGF0YS5ieXRlTGVuZ3RoKSAqIDEwMCk7CiAgICAgIHBlcmNlbnQudGV4dENvbnRlbnQgPSBgJHtwZXJjZW50RG9uZX0lIGRvbmVgOwoKICAgIH0gd2hpbGUgKHBvc2l0aW9uIDwgZmlsZURhdGEuYnl0ZUxlbmd0aCk7CiAgfQoKICAvLyBBbGwgZG9uZS4KICB5aWVsZCB7CiAgICByZXNwb25zZTogewogICAgICBhY3Rpb246ICdjb21wbGV0ZScsCiAgICB9CiAgfTsKfQoKc2NvcGUuZ29vZ2xlID0gc2NvcGUuZ29vZ2xlIHx8IHt9OwpzY29wZS5nb29nbGUuY29sYWIgPSBzY29wZS5nb29nbGUuY29sYWIgfHwge307CnNjb3BlLmdvb2dsZS5jb2xhYi5fZmlsZXMgPSB7CiAgX3VwbG9hZEZpbGVzLAogIF91cGxvYWRGaWxlc0NvbnRpbnVlLAp9Owp9KShzZWxmKTsK",
              "ok": true,
              "headers": [
                [
                  "content-type",
                  "application/javascript"
                ]
              ],
              "status": 200,
              "status_text": ""
            }
          },
          "base_uri": "https://localhost:8080/",
          "height": 362
        },
        "id": "2Ellv8OKZ0Tw",
        "outputId": "4b24f04a-a6ef-4bdc-d96a-b182aee7e3a3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "\n",
              "     <input type=\"file\" id=\"files-0a7cedc8-8bbb-4b0e-901a-a9b4104b7e2f\" name=\"files[]\" multiple disabled\n",
              "        style=\"border:none\" />\n",
              "     <output id=\"result-0a7cedc8-8bbb-4b0e-901a-a9b4104b7e2f\">\n",
              "      Upload widget is only available when the cell has been executed in the\n",
              "      current browser session. Please rerun this cell to enable.\n",
              "      </output>\n",
              "      <script src=\"/nbextensions/google.colab/files.js\"></script> "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Saving 0vugygEjxQJPr9yz.png to 0vugygEjxQJPr9yz (1).png\n",
            "0vugygEjxQJPr9yz.png\n",
            "paper\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    }
  ]
}