# -------------------------arg-------------------------
SOURCES_FILE = '../data/input/dev.csv'
ids_file = '../data/input/ids.txt'
answers_file = '../data/input/answers.txt'
questions_file = '../data/input/questions.txt'
labels_file = '../data/input/labels.txt'

# directory for input data
in_dir = '../data'
# directory for output pickles
out_dir = '../data/output'
# decide portion to spare for training and validation
portion = 0.8
# type of word embeddings baike
emb = "baike"
# baike_50 vector path
baike_dir = '../data/input/baike-50.vec.txt'
# all of labels
labels = ['AGAINST', 'NONE', 'FAVOR']
# use the all vocabulary
big_voc = False
# max time step of sentence sequence
sen_max_len = 50
# max time step of sentence sequence
ask_max_len = 25

# ############################### dataset dir
# location of dataset
input = 'input'
# model save dir
model_dir = './NNET/data/model/'
# features baike dir
features_baike_dir = './NNET/data/output/features_baike.pkl'
# features baike training dir
features_baike_training_dir = '/home/wjunneng/Ubuntu/2019-FlyAI-Chinese-Weibo-s-Position-Detection/NNET/data/output/features_baike_training.pkl'
# features baike validation dir
features_baike_validation_dir = './NNET/data/output/features_baike_validation.pkl'
# word2idx baike dir
word2idx_baike_dir = './NNET/data/output/word2idx_baike.pkl'
# embeddings baike dir
embeddings_baike_dir = './NNET/data/output/embeddings_baike.pkl'

# ############################### model parameters
# type of model to use for Stance Project
model = "Net"
# type of word embeddings
embtype = "baike"
# number of classes to predict
nclass = 3
# size of RNN hidden layer
nhid = 50
# number of layers of LSTM
nlayers = 1
# learning rate
lr = 1e-4
# number of training epoch
epochs = 10
# batch size
batch_size = 8
# dropout rate
dropout = 0.5
# max time step of answer sequence
ans_len = 50
# max time step of question sequence
ask_len = 25
# number of attention hops for RoomConditional models
nhops = 3

# ############################## test purpose
# random seed for reproduction
seed = 123456
# use CUDA
cuda = False
# flag for training model or only test
is_test = False
# flag for testing correctness of program on 10 training records
verify = False
# flag for continue training on current model
proceed = False