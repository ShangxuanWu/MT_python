data_header_basename = 'data_header'
train_data_basename = 'train_data'
train_label_basename = 'train_label'
config_basename = 'config'
model_fd_basename = 'model'
train_log_basename = 'train_log'

# TODO: what about test data?

init_fns = [
        data_header_basename, 
        train_data_basename,
        train_label_basename,
        config_basename,
        ]

full_fns = [ 
        data_header_basename,
        train_data_basename,
        train_label_basename,
        config_basename,
        train_log_basename,
        model_fd_basename,
        ]

train_val_split_portion = 0.9