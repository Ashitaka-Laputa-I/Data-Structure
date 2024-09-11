import tensorflow as tf

# 获取 TensorFlow 版本和 GPU 可用性
tf_v = tf.__version__
gpu_ava = len(tf.config.list_physical_devices('GPU')) > 0

print('Tensorflow Version:', tf_v, '\tGPU Available:', gpu_ava)

# 创建两个常量向量
v1 = tf.constant([1.0, 2.0], name='v1')
v2 = tf.constant([2.0, 1.0], name='v2')

# 添加两个向量
result = tf.add(v1, v2, name='add')

print(result)


