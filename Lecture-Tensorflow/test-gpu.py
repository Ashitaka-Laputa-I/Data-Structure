import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np

# 检查 TensorFlow 是否可以使用 GPU
if not tf.test.is_gpu_available():
    print("没有找到可用的 GPU，程序将退出。")
    exit()

print("开始加载 MNIST 数据集...")
# 加载 MNIST 数据集
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 预处理数据
x_train, x_test = x_train / 255.0, x_test / 255.0
x_train = x_train[..., np.newaxis].astype("float32")
x_test = x_test[..., np.newaxis].astype("float32")

print(f"训练集大小: {x_train.shape}")
print(f"测试集大小: {x_test.shape}")

# 创建卷积神经网络模型
print("开始构建模型...")
model = models.Sequential([
    layers.Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D(pool_size=(2, 2)),
    layers.Conv2D(64, kernel_size=(3, 3), activation='relu'),
    layers.MaxPooling2D(pool_size=(2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# 编译模型
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 输出模型结构
model.summary()

print("开始训练模型...")
# 训练模型
model.fit(x_train, y_train, epochs=5, batch_size=64, verbose=2)

print("开始评估模型...")
# 评估模型
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print(f'\n测试准确率: {test_acc:.4f}')

print("程序运行结束，您可以使用 'nvidia-smi' 工具监控 GPU 使用情况。")
