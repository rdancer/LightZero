# mediumnet
cfg = {}
cfg['tokenizer'] = {'_target_': 'models.tokenizer.Tokenizer',
                    # 'vocab_size': 512, # TODO: for atari
                    # 'embed_dim': 512,
                    # 'vocab_size': 256,  # TODO: for atari debug
                    # 'embed_dim': 256,
                    # 'vocab_size': 64,  # TODO: for atari debug
                    # 'embed_dim': 64,
                    'vocab_size': 128,  # TODO: for atari debug
                    # 'embed_dim': 128, # z_channels
                    # 'embed_dim': 1024, # z_channels
                    'embed_dim': 256, # z_channels


                                        'encoder':
                               {'resolution': 64, 'in_channels': 3, 'z_channels': 128, 'ch': 64,
                                'ch_mult': [1, 1, 1, 1, 1], 'num_res_blocks': 2, 'attn_resolutions': [8, 16],
                                'out_ch': 3, 'dropout': 0.0},# TODO：for atari debug
                            'decoder':
                    {'resolution': 64, 'in_channels': 3, 'z_channels': 128, 'ch': 64,
                     'ch_mult': [1, 1, 1, 1, 1], 'num_res_blocks': 2, 'attn_resolutions': [8, 16],
                     'out_ch': 3, 'dropout': 0.0}}  # TODO：for atari debug
                    # 'vocab_size': 64,  # TODO: for atari debug
                    # 'embed_dim': 64, # z_channels
                    # 'encoder':
                    #            {'resolution': 64, 'in_channels': 3, 'z_channels': 64, 'ch': 64,
                    #             'ch_mult': [1, 1, 1, 1, 1], 'num_res_blocks': 2, 'attn_resolutions': [8, 16],
                    #             'out_ch': 3, 'dropout': 0.0},# TODO：for atari debug
                    #         'decoder':
                    # {'resolution': 64, 'in_channels': 3, 'z_channels': 64, 'ch': 64,
                    #  'ch_mult': [1, 1, 1, 1, 1], 'num_res_blocks': 2, 'attn_resolutions': [8, 16],
                    #  'out_ch': 3, 'dropout': 0.0}}  # TODO：for atari debug
                    # {'resolution': 64, 'in_channels': 1, 'z_channels': 512, 'ch': 64,
                    #             'ch_mult': [1, 1, 1, 1, 1], 'num_res_blocks': 2, 'attn_resolutions': [8, 16],
                    #             'out_ch': 3, 'dropout': 0.0},# TODO：for atari
                    #         'decoder':
                    # {'resolution': 64, 'in_channels': 1, 'z_channels': 512, 'ch': 64,
                    #  'ch_mult': [1, 1, 1, 1, 1], 'num_res_blocks': 2, 'attn_resolutions': [8, 16],
                    #  'out_ch': 3, 'dropout': 0.0}}  # TODO：for atari
cfg['world_model'] = {
                      # 'tokens_per_block': 17,
                      # 'max_blocks': 20,
                      #   "max_tokens": 17 * 20,  # TODO： horizon
                      # 'max_blocks': 5,
                      # "max_tokens": 17 * 5,  # TODO： horizon
                      # 'embed_dim': 128, # TODO：for atari

                      # 'tokens_per_block': 2,
                      # 'max_blocks': 10,
                      # "max_tokens": 2 * 10,  # TODO： horizon
                      # 'embed_dim': 1024, # TODO：for atari

                      'tokens_per_block': 2,
                      'max_blocks': 5,
                      "max_tokens": 2 * 5,  # TODO： horizon
                      # 'embed_dim':1024, # TODO：for atari
                      'embed_dim':256, # TODO：for atari


                      'attention': 'causal',
                      # 'num_layers': 10,# TODO：for atari
                      'num_layers': 2, # TODO：for atari debug
                      'num_heads': 2,

                      'embed_pdrop': 0.1,
                      'resid_pdrop': 0.1,
                      'attn_pdrop': 0.1,
                      "device": 'cuda:0',
                    #   "device": 'cpu',
                      'support_size': 21,
                      'action_shape': 6,# TODO：for atari
                      # 'max_cache_size':500,
                      'max_cache_size':1000,
                      "env_num":8,
                      }
from easydict import EasyDict
cfg = EasyDict(cfg)

# atari orignet
# cfg = {}
# cfg['tokenizer'] = {'_target_': 'models.tokenizer.Tokenizer',
#                     'vocab_size': 512, # TODO: for atari
#                     'embed_dim': 512,
#                     # 'vocab_size': 256,  # TODO: for atari debug
#                     # 'embed_dim': 256,
#                     # 'vocab_size': 128,  # TODO: for atari debug
#                     # 'embed_dim': 128,
#                     # 'encoder':
#                     #            {'resolution': 64, 'in_channels': 3, 'z_channels': 128, 'ch': 64,
#                     #             'ch_mult': [1, 1, 1, 1, 1], 'num_res_blocks': 2, 'attn_resolutions': [8, 16],
#                     #             'out_ch': 3, 'dropout': 0.0},# TODO：for atari debug
#                     #  'decoder':
#                     #       {'resolution': 64, 'in_channels': 3, 'z_channels': 128, 'ch': 64,
#                     #       'ch_mult': [1, 1, 1, 1, 1], 'num_res_blocks': 2, 'attn_resolutions': [8, 16],
#                     #       'out_ch': 3, 'dropout': 0.0}}  # TODO：for atari debug
#                     'encoder':
#                     {'resolution': 64, 'in_channels': 3, 'z_channels': 512, 'ch': 64,
#                                 'ch_mult': [1, 1, 1, 1, 1], 'num_res_blocks': 2, 'attn_resolutions': [8, 16],
#                                 'out_ch': 3, 'dropout': 0.0},# TODO：for atari
#                             'decoder':
#                     {'resolution': 64, 'in_channels': 3, 'z_channels': 512, 'ch': 64,
#                      'ch_mult': [1, 1, 1, 1, 1], 'num_res_blocks': 2, 'attn_resolutions': [8, 16],
#                      'out_ch': 3, 'dropout': 0.0}}  # TODO：for atari
# cfg['world_model'] = {
#                         'tokens_per_block': 17,
#                       # 'max_blocks': 20,
#                       #   "max_tokens": 17 * 20,  # TODO： horizon
#                         #   'max_blocks': 10,
#                         # "max_tokens": 17 * 10,  # TODO： horizon
#                       'max_blocks': 5,
#                       "max_tokens": 17 * 5,  # TODO： horizon
#                       'attention': 'causal',
#                       # 'num_layers': 10,# TODO：for atari
#                       'num_layers': 2, # TODO：for atari debug
#                       # 'num_heads': 4,
#                       # 'embed_dim': 256, # TODO：for atari

#                       'num_heads': 2,
#                       'embed_dim': 128, # TODO：for atari H5
#                       # 'embed_dim': 64, # TODO：for atari H10

#                       # 'num_heads': 4,
#                       # 'embed_dim': 256, # TODO：for atari H5

#                       'embed_pdrop': 0.1,
#                       'resid_pdrop': 0.1,
#                       'attn_pdrop': 0.1,
#                       "device": 'cuda:0',
#                     #   "device": 'cpu',
#                       # 'support_size': 601,
#                       'support_size': 21,
#                       'action_shape': 6,# TODO：for atari
#                       # 'max_cache_size':500,
#                       'max_cache_size':1000,
#                       # 'max_cache_size':5000,
#                       "env_num":8,
#                       }
# from easydict import EasyDict
# cfg = EasyDict(cfg)
