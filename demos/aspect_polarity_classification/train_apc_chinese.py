# -*- coding: utf-8 -*-
# file: training.py
# time: 2021/5/26 0026
# author: yangheng <yangheng@m.scnu.edu.cn>
# github: https://github.com/yangheng95
# Copyright (C) 2021. All Rights Reserved.

########################################################################################################################
#                    train and evaluate on your own apc_datasets (need train and test apc_datasets)                    #
########################################################################################################################

from pyabsa.functional import Trainer
from pyabsa.functional import APCConfigManager
from pyabsa.functional import ABSADatasetList
from pyabsa.functional import APCModelList

config = APCConfigManager.get_apc_config_chinese()
config.evaluate_begin = 4
config.dropout = 0.5
config.l2reg = 1e-8
config.model = APCModelList.FAST_LCF_BERT
# config.spacy_model = 'zh_core_web_sm'
# chinese_sets = ABSADatasetList.Chinese
# chinese_sets = ABSADatasetList.Chinese
chinese_sets = 'mooc'
sent_classifier = Trainer(config=config,  # set config=None to use default model
                          dataset=chinese_sets,  # train set and test set will be automatically detected
                          checkpoint_save_mode=1,
                          auto_device=True  # automatic choose CUDA or CPU
                          ).load_trained_model()
